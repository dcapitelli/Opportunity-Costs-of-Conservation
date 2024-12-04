import pandas as pd
import numpy as np

# constants
# NUTS2 codes to be ignored for aggregation of populations. Usually outdated regions after re-allocation
IGNORE_NUTS2_CODES = [
    'EL11', 'EL12', 'EL13', 'EL14', 'EL21', 'EL22', 'EL23', 'EL24', 'EL25',
    'FR91', 'FR93', 'FR94'
    'HR01', 'HR02', 'HR05', 'HR06',
    'HU10',
    'IE01', 'IE02', 'IE03',
    'ITD5', 'ITE3',
    'LT00',
    'PL11', 'PL12', 'PL31', 'PL32', 'PL33', 'PL34',
    'SI01', 'SI02'
]

# input files
INPUT_DATA_FOLDER = "./in/"
COMMODITY_PRICES_LIVESTOCK_FOLDER = "commodity_prices/livestock/"
COMMON_FOLDER = "common/"

# countries
countries_df = pd.read_csv(INPUT_DATA_FOLDER + COMMON_FOLDER + "NaturaConnect_countries.csv")
# use countries df as basis for output
out_df  = countries_df

# inflation rates
inflation_to_2021_df = pd.read_csv(INPUT_DATA_FOLDER + COMMON_FOLDER + "Inflation_rate_to_2021.csv", encoding='utf-8')
inflation_to_2021_df = inflation_to_2021_df.set_index('Year')

# corrects inflation to the year 2021
def correctForInflation(value : float, year : int) -> float:
    if year == 2021:
        return value
    inflation_rate = float(inflation_to_2021_df.at[year,'Inflation_rate_to_2021'])
    inflated_value = value * inflation_rate
    # print(f"{value}*{inflation_rate}={inflated_value}")
    return inflated_value

# chicken population
chicken_population_df = pd.read_csv(INPUT_DATA_FOLDER + COMMODITY_PRICES_LIVESTOCK_FOLDER + "Chicken_population_glw4.csv", encoding='utf-8')
# aggregate all nuts2 regional populations in out_df
out_df['chicken_population_x1000_heads'] = np.nan
for index, row in chicken_population_df.iterrows():
    nuts2_code = row['NUTS_ID']
    # ignore outdated nuts2 regions
    if nuts2_code in IGNORE_NUTS2_CODES:
        continue
    country_code = row['CNTR_CODE']
    country_mask = out_df['Country_NUTS_Code'] == country_code
    if country_code in out_df['Country_NUTS_Code'].values:
        if pd.isna(out_df.loc[country_mask, 'chicken_population_x1000_heads'].iloc[0]):
            out_df.loc[country_mask, ['chicken_population_x1000_heads']] = 0.0
        out_df.loc[country_mask, ['chicken_population_x1000_heads']] += row['Chicken_population'] / 1000

# bovine, swine/domestic and sheep populations
for livestock_type in ["bovine", "sheep", "swine_domestic"]:
    out_df[f"{livestock_type}_population_x1000_heads"] = np.nan
    population_file = "tgs00045_" + livestock_type + ".csv"
    population_df = pd.read_csv(INPUT_DATA_FOLDER + COMMODITY_PRICES_LIVESTOCK_FOLDER + population_file, encoding='utf-8')
    # aggregate all nuts2 regional populations in out_df
    for nuts2_code in population_df['geo'].unique():
        # ignore outdated codes
        if nuts2_code in IGNORE_NUTS2_CODES:
            continue
        country_code = nuts2_code[:2]
        country_mask = out_df['Country_NUTS_Code'] == country_code
        if not out_df.loc[country_mask, f"{livestock_type}_population_x1000_heads"].empty and pd.isna(out_df.loc[country_mask, f"{livestock_type}_population_x1000_heads"].iloc[0]):
            out_df.loc[out_df['Country_NUTS_Code'] == country_code, [f"{livestock_type}_population_x1000_heads"]] = 0.0
        # select slice with all rows for specific nuts2 region, and exclude data more recent than 2021
        population_region_df = population_df[(population_df['geo'] == nuts2_code) & (population_df['TIME_PERIOD'] <= 2021)]
        # take the most recent year available
        index = population_region_df['TIME_PERIOD'].idxmax()
        value = population_region_df.at[index, 'OBS_VALUE']
        # add to national aggregate
        
        out_df.loc[country_mask, [f"{livestock_type}_population_x1000_heads"]] += value

# this function works for tables with columns that are years
# i.e., the "Unit values...", "Selling prices...", "EUROSTAT..." csv files
def getMostRecentValueAndCorrectForInflation(df : pd.DataFrame, country_column : str, output_column : str, start_year : int, end_year : int):
    out_df[output_column] = np.nan
    for index, row in df.iterrows():
        country_name = row[country_column]
        # print(f"\n{country_name}:")
        year = start_year
        corrected_value = np.nan
        while year > end_year:
            year_column = f"{year}"
            if year_column in row.index and not pd.isna(row[year_column]):
                # print(f"{year}: {row[year_column]}")
                try:
                    # remove thousands separator
                    value = float(str(row[year_column]).replace(',',''))
                except:
                    year = year - 1
                    continue
                # correct for inflation
                corrected_value = correctForInflation(value, year)
                # print(f"{country_name} result {corrected_value}")
                break
            year = year - 1
        # if pd.isna(corrected_value):
        #     print(f"Couldn't find value for {country_name}")
        out_df.loc[out_df['Country_Name'] == country_name, output_column] = corrected_value

# load price tables
bovine_meat_prices_df = pd.read_csv(INPUT_DATA_FOLDER + COMMODITY_PRICES_LIVESTOCK_FOLDER + "Unit values at producer prices of Cattle euro per tonne.csv", encoding='utf-8')
chicken_meat_prices_df = pd.read_csv(INPUT_DATA_FOLDER + COMMODITY_PRICES_LIVESTOCK_FOLDER + "Unit values at producer prices of Poultry euro per tonne.csv", encoding='utf-8')
pig_meat_prices_df = pd.read_csv(INPUT_DATA_FOLDER + COMMODITY_PRICES_LIVESTOCK_FOLDER + "Unit values at producer prices of Pigs euro per tonne.csv", encoding='utf-8')
sheep_meat_prices_df = pd.read_csv(INPUT_DATA_FOLDER + COMMODITY_PRICES_LIVESTOCK_FOLDER + "Unit values at producer prices of Sheep and goats euro per tonne.csv", encoding='utf-8')
chicken_eggs_prices_df = pd.read_csv(INPUT_DATA_FOLDER + COMMODITY_PRICES_LIVESTOCK_FOLDER + "Selling prices of fresh eggs TAG00071 euro per 100 items.csv", encoding='utf-8')
bovine_milk_prices_df = pd.read_csv(INPUT_DATA_FOLDER + COMMODITY_PRICES_LIVESTOCK_FOLDER + "Selling prices of raw cow's milk TAG00070 euro per 100kg.csv", encoding='utf-8')

getMostRecentValueAndCorrectForInflation(bovine_meat_prices_df, 'GEO (Labels)', "bovine_meat_price_eur2021/tonne", 2021, 1990)
getMostRecentValueAndCorrectForInflation(chicken_meat_prices_df, 'GEO (Labels)', "chicken_meat_price_eur2021/tonne", 2021, 1990)
getMostRecentValueAndCorrectForInflation(pig_meat_prices_df, 'GEO (Labels)', "pig_meat_price_eur2021/tonne", 2021, 1990)
getMostRecentValueAndCorrectForInflation(sheep_meat_prices_df, 'GEO (Labels)', "sheep_meat_price_eur2021/tonne", 2021, 1990)
getMostRecentValueAndCorrectForInflation(chicken_eggs_prices_df, 'GEO (Labels)', "eggs_price_eur2021/100items", 2021, 1990)
getMostRecentValueAndCorrectForInflation(bovine_milk_prices_df, 'GEO (Labels)', "milk_price_eur2021/100kg", 2021, 1990)

# convert from eur/100kg to eur/tonne for milk
out_df['milk_price_eur2021/tonne'] = out_df['milk_price_eur2021/100kg'] * 10 # 100kg/tonne
out_df = out_df.drop('milk_price_eur2021/100kg', axis=1)

# load production tables
bovine_meat_production_df = pd.read_csv(INPUT_DATA_FOLDER + COMMODITY_PRICES_LIVESTOCK_FOLDER + "Production of meat cattle TAG00044 Thousand tonnes.csv", encoding='utf-8')
chicken_meat_production_df = pd.read_csv(INPUT_DATA_FOLDER + COMMODITY_PRICES_LIVESTOCK_FOLDER + "Production of meat Poultry thousand tonnes.csv", encoding='utf-8')
pig_meat_production_df = pd.read_csv(INPUT_DATA_FOLDER + COMMODITY_PRICES_LIVESTOCK_FOLDER + "EUROSTAT Production of meat Pigs_thousand tonnes.csv", encoding='utf-8')
sheep_meat_production_df = pd.read_csv(INPUT_DATA_FOLDER + COMMODITY_PRICES_LIVESTOCK_FOLDER + "Production of meat Sheep and goats thousand tonnes.csv", encoding='utf-8')
chicken_eggs_production_df = pd.read_csv(INPUT_DATA_FOLDER + COMMODITY_PRICES_LIVESTOCK_FOLDER + "EUROSTAT Total Production of eggs for consumption and number of laying hens APRO_EC_EGGHEN in millions.csv", encoding='utf-8')
bovine_milk_production_df = pd.read_csv(INPUT_DATA_FOLDER + COMMODITY_PRICES_LIVESTOCK_FOLDER + "EUROSTAT Production of raw cow's milk_1000t.csv", encoding='utf-8')

getMostRecentValueAndCorrectForInflation(bovine_meat_production_df, 'GEO (Labels)', "bovine_meat_production_x1000tonne", 2021, 1990)
getMostRecentValueAndCorrectForInflation(chicken_meat_production_df, 'GEO (Labels)', "chicken_meat_production_x1000tonne", 2021, 1990)
getMostRecentValueAndCorrectForInflation(pig_meat_production_df, 'GEO (Labels)', "pig_meat_production_x1000tonne", 2021, 1990)
getMostRecentValueAndCorrectForInflation(sheep_meat_production_df, 'GEO (Labels)', "sheep_meat_production_x1000tonne", 2021, 1990)
getMostRecentValueAndCorrectForInflation(chicken_eggs_production_df, 'GEO (Labels)', "eggs_production_x1000000items", 2021, 1990)
getMostRecentValueAndCorrectForInflation(bovine_milk_production_df, 'GEO (Labels)', "milk_production_x1000tonne", 2021, 1990)

# calculate national production values
out_df['bovine_meat_production_value_eur2021'] = out_df['bovine_meat_production_x1000tonne'] * 1000 * out_df['bovine_meat_price_eur2021/tonne']
out_df['chicken_meat_production_value_eur2021'] = out_df['chicken_meat_production_x1000tonne'] * 1000 * out_df['chicken_meat_price_eur2021/tonne']
out_df['pig_meat_production_value_eur2021'] = out_df['pig_meat_production_x1000tonne'] * 1000 * out_df['pig_meat_price_eur2021/tonne']
out_df['sheep_meat_production_value_eur2021'] = out_df['sheep_meat_production_x1000tonne'] * 1000 * out_df['sheep_meat_price_eur2021/tonne']
out_df['eggs_production_value_eur2021'] = out_df['eggs_production_x1000000items'] * 10000 * out_df['eggs_price_eur2021/100items'] # note different conversion factor
out_df['milk_production_value_eur2021'] = out_df['milk_production_x1000tonne'] * 1000 * out_df['milk_price_eur2021/tonne']

# calculate national value per head
# for cows, add the value of meat to the value of milk
out_df['bovine_value_eur2021/head'] = (out_df['bovine_meat_production_value_eur2021'] + out_df['milk_production_value_eur2021']) / (out_df['bovine_population_x1000_heads'] * 1000)
# for chicken, add the value of meat to the value of eggs
out_df['chicken_value_eur2021/head'] = (out_df['chicken_meat_production_value_eur2021'] + out_df['eggs_production_value_eur2021']) / (out_df['chicken_population_x1000_heads'] * 1000)
out_df['pig_value_eur2021/head'] = out_df['pig_meat_production_value_eur2021'] / (out_df['swine_domestic_population_x1000_heads'] * 1000)
out_df['sheep_value_eur2021/head'] = out_df['sheep_meat_production_value_eur2021'] / (out_df['sheep_population_x1000_heads'] * 1000)

print(out_df)

out_df.to_csv("./out/commodity_livestock_sanitized.csv", encoding='utf-8')