import pandas as pd
import numpy as np
import warnings

# pandas does not like repeated insertion of new columns in a for loop, but we do it anyway
warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)

# constants
# the following spam codes can be ignored since their production is assumed negligible in Europe
IGNORE_SPAM_CODES = ['cass', 'orts', 'acof', 'rcof', 'coco']

# input file paths
INPUT_DATA_FOLDER = "./in/"
COMMODITY_PRICES_CROPS_FOLDER = "commodity_prices/crops/"
COMMON_FOLDER = "common/"

# inflation rates
inflation_to_2021_df = pd.read_csv(INPUT_DATA_FOLDER + COMMON_FOLDER + "Inflation_rate_to_2021.csv", encoding='utf-8')
inflation_to_2021_df = inflation_to_2021_df.set_index('Year')

# usd-eur yearly conversion rates
usd_to_eur_df = pd.read_csv(INPUT_DATA_FOLDER + COMMON_FOLDER + "USD-EUR_annual_conversion_eu_bank.csv", encoding='utf-8')
usd_to_eur_df = usd_to_eur_df.set_index('Year')

countries_df = pd.read_csv(INPUT_DATA_FOLDER + COMMON_FOLDER + "NaturaConnect_Countries.csv", encoding='utf-8')
# use countries as a basis
eurostat_out_df = countries_df.copy()

# eurostat prices
eurostat_crop_prices_df = pd.read_csv(INPUT_DATA_FOLDER + COMMODITY_PRICES_CROPS_FOLDER + "aact_uv02.csv", encoding='utf-8')
eurostat_crop_prices_df.drop(eurostat_crop_prices_df[eurostat_crop_prices_df['unit'] != 'EUR_T'].index, inplace=True)

def convertUSDtoEUR(usd : float, year : int) -> float:
    if year > 2021:
        raise ValueError(f"Can only convert USD to EUR up to 2021 (given year: {year})")
    if year < 2000:
        raise ValueError(f"Can only convert USD to EUR from 2000 (given year: {year})")
    rate = float(usd_to_eur_df.at[year,'USD_to_EUR'])
    return usd * rate

# corrects inflation to the year 2021
def correctForInflation(value : float, year : int) -> float:
    if year == 2021:
        return value
    inflation_rate = float(inflation_to_2021_df.at[year,'Inflation_rate_to_2021'])
    inflated_value = value * inflation_rate
    # print(f"{value}*{inflation_rate}={inflated_value}")
    return inflated_value

def checkYear(df : pd.DataFrame, year : int):
    year_df = df[df['TIME_PERIOD'] == year]
    if not year_df.empty and not pd.isna(year_df['OBS_VALUE'].iloc[0]):
        value = float(year_df['OBS_VALUE'].iloc[0])
        inflated_value = correctForInflation(value, year)
        return inflated_value
    return None

def findMostRecentAndCorrectForInflation(df : pd.DataFrame, startYear : int, stopYear : int):
    for year in range(startYear, stopYear - 1, -1):
        value = checkYear(df, year)
        if value != None:
            return (value, year)
    return (np.nan, np.nan)

print("Sanitizing EUROSTAT crop price data and correcting for inflation...")

for crop_code in eurostat_crop_prices_df['itm_newa'].unique():
    crop_column = f"{str(crop_code).zfill(5)}_price_eur2021/kg"
    crop_year_column = f"{str(crop_code).zfill(5)}_source_year"
    eurostat_out_df[crop_column] = np.nan
    selected_crop_prices_df = eurostat_crop_prices_df[eurostat_crop_prices_df['itm_newa'] == crop_code]
    for geo in selected_crop_prices_df['geo'].unique():
        selected_geo_crop_prices_df = selected_crop_prices_df[selected_crop_prices_df['geo'] == geo]
        value, year = findMostRecentAndCorrectForInflation(selected_geo_crop_prices_df, 2021, 1985)
        geo_mask = eurostat_out_df['Country_NUTS_Code'] == geo
        eurostat_out_df.loc[geo_mask, [crop_column]] = value / 1000 # from eur2021/tonne to eur2021/kg
        eurostat_out_df.loc[geo_mask, [crop_year_column]] = year

# intermediate result
eurostat_out_df.to_csv("out/eurostat_crop_prices_sanitized.csv", encoding='utf-8')

fao_crop_prices_df = pd.read_csv(INPUT_DATA_FOLDER + COMMODITY_PRICES_CROPS_FOLDER + "fao\Prices_E_Europe_NOFLAG.csv", encoding='utf-8')
fao_crop_prices_df.drop(fao_crop_prices_df[fao_crop_prices_df['Unit'] != 'USD'].index, inplace=True)

spam_to_eurostat_df = pd.read_csv(INPUT_DATA_FOLDER + COMMODITY_PRICES_CROPS_FOLDER + "SPAM_crops_to_EUROSTAT_code_crop_prices.csv")
spam_national_out_df = countries_df.copy()

print("Reclassifying the crop price data to SPAM categories...")

for spam_code in spam_to_eurostat_df['Short Name  SPAM'].unique():
    if pd.isna(spam_code):
        continue
    spam_column = f"{str(spam_code).strip()}_price_eur2021/kg"
    spam_source_column = f"{str(spam_code).strip()}_source"
    # convert the eurostat codes in the conversion table to the column names in the eurostat df
    eurostat_codes_raw = spam_to_eurostat_df.loc[spam_to_eurostat_df['Short Name  SPAM'] == spam_code, 'Code EUROSTAT AACT_UV01'].item()
    if pd.notna(eurostat_codes_raw):
        eurostat_columns = [f"{c.strip().zfill(5)}_price_eur2021/kg" for c in str(eurostat_codes_raw).split(sep=';')]
        spam_national_out_df[spam_column] = eurostat_out_df[eurostat_columns].mean(axis=1)
        # spam_out_df[spam_source_column] = "eurostat"
        spam_national_out_df.loc[pd.notna(spam_national_out_df[spam_column]), [spam_source_column]] = "eurostat"
        continue
    # if eurostat codes not found, check if the spam code is marked to be ignored
    if str(spam_code).strip() in IGNORE_SPAM_CODES:
        spam_national_out_df[spam_column] = np.nan
        spam_national_out_df[spam_source_column] = np.nan
        continue
    # else, check if fao codes are available
    fao_codes_raw = spam_to_eurostat_df.loc[spam_to_eurostat_df['Short Name  SPAM'] == spam_code, 'Code FAO'].item()
    if pd.notna(fao_codes_raw):
        fao_codes = [c.strip() for c in str(fao_codes_raw).split(sep=',')]
        # print(fao_codes)
        # a dict with countries as keys, and lists of found prices for the different fao codes as values
        spam_category_fao_prices = dict()
        for fao_code in fao_codes:
            selected_fao_crop_prices_df = fao_crop_prices_df[fao_crop_prices_df['Item Code'] == int(fao_code)]
            for index, row in selected_fao_crop_prices_df.iterrows():
                # check if the country is one we're interested in
                if row['Area'] not in countries_df['Country_Name'].unique():
                    continue
                # print(f"spam_code={spam_code}, fao_code={fao_code}, area={row['Area']}")
                # find most recent value
                for year in range(2021, 1991, -1):
                    year_column = f"Y{year}"
                    if pd.notna(row[year_column]):
                        # found a value!
                        # correct for inflation, go back from usd to eur and go to /kg instead of /tonne
                        value_usd_per_tonne = float(row[year_column])
                        value_usd_per_kg = value_usd_per_tonne / 1000
                        value_eur_per_kg = convertUSDtoEUR(value_usd_per_kg, year)
                        value_eur2021_per_kg = correctForInflation(value_eur_per_kg, year)
                        if row['Area'] not in spam_category_fao_prices:
                            spam_category_fao_prices[row['Area']] = list()
                        spam_category_fao_prices[row['Area']].append(value_eur2021_per_kg)
                        # do not look further back in time if we have a value
                        break
        # print(spam_category_fao_prices)
        for country in countries_df['Country_Name'].unique():
            if country in spam_category_fao_prices:
                spam_national_out_df.loc[spam_national_out_df['Country_Name'] == country, [spam_column]] = np.mean(spam_category_fao_prices[country])
                spam_national_out_df.loc[spam_national_out_df['Country_Name'] == country, [spam_source_column]] = "fao"
            else:
                spam_national_out_df.loc[spam_national_out_df['Country_Name'] == country, [spam_column]] = np.nan
                spam_national_out_df.loc[spam_national_out_df['Country_Name'] == country, [spam_source_column]] = np.nan
        continue
    # no options left (neither EUROSTAT nor FAO)
    spam_national_out_df[spam_column] = np.nan
    spam_national_out_df[spam_source_column] = np.nan
        
# intermediate result
spam_national_out_df.to_csv("out/spam_crop_prices_national_sanitized.csv", encoding='utf-8')

print("Broadcasting SPAM crop price data to NUTS2 regions...")

nuts2_regions_df = pd.read_csv(INPUT_DATA_FOLDER + COMMON_FOLDER + "NUTS2_regions.csv", encoding='utf-8')
nuts2_regions_df = nuts2_regions_df.filter(['NUTS_ID', 'LEVL_CODE', 'CNTR_CODE', 'NUTS_NAME'])
nuts2_regions_df = nuts2_regions_df.sort_values(by=['NUTS_ID'])

spam_nuts2_out_df = nuts2_regions_df.merge(spam_national_out_df.rename(columns={'Country_NUTS_Code': 'CNTR_CODE'}), how='left', on='CNTR_CODE')

# final result
spam_nuts2_out_df.to_csv("out/spam_crop_prices_nuts2_sanitized.csv", encoding='utf-8')