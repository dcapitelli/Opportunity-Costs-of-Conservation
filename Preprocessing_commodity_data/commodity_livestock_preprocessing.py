import pandas as pd
import numpy as np
import warnings

warnings.simplefilter(action='ignore', category=RuntimeWarning) # np.nanmean will throw this warning sometimes

# input files
INPUT_DATA_FOLDER = "./in/"
COMMODITY_PRICES_LIVESTOCK_FOLDER = "commodity_prices/livestock/"
COMMON_FOLDER = "common/"

# countries
countries_df = pd.read_csv(INPUT_DATA_FOLDER + COMMON_FOLDER + "NaturaConnect_countries.csv")
# use countries df as basis for output
out_df  = countries_df

# dict for keeping track of missing stuff per country
missing = dict()

# inflation rates
inflation_to_2021_df = pd.read_csv(INPUT_DATA_FOLDER + COMMON_FOLDER + "Inflation_rate_to_2021.csv", encoding='utf-8')
inflation_to_2021_df = inflation_to_2021_df.set_index('Year')

# usd-eur yearly conversion rates
usd_to_eur_df = pd.read_csv(INPUT_DATA_FOLDER + COMMON_FOLDER + "USD-EUR_annual_conversion_eu_bank.csv", encoding='utf-8')
usd_to_eur_df = usd_to_eur_df.set_index('Year')

def convertUSDtoEUR(usd : float, year : int) -> float:
    if year > 2021:
        raise ValueError(f"Can only convert USD to EUR up to 2021 (given year: {year})")
    if year < 2000:
        raise ValueError(f"Can only convert USD to EUR from 2000 (given year: {year})")
    rate = float(usd_to_eur_df.at[year,'USD_to_EUR'])
    return usd * rate

# corrects inflation to the year 2021
def correctForInflation(value : float, year : int) -> float:
    if np.isnan(value) or np.isnan(year):
        return np.nan
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
        return value
    return None

def findMostRecent(df : pd.DataFrame, startYear : int, stopYear : int):
    for year in range(startYear, stopYear - 1, -1):
        value = checkYear(df, year)
        if value != None:
            return (value, year)
    return (np.nan, np.nan)

products = ['meat', 'milk']
animals = ['cattle', 'sheep', 'goat']
animal_products = [f"{animal}_{product}" for product in products for animal in animals]

eurostat_animal_product_price_codes = {
    'cattle_meat': [11110000, 11112000, 11113000, 11114000, 11120000],
    'sheep_meat': [11410000],
    'goat_meat': [11420000],
    'cattle_milk': [12112000],
    'sheep_milk': [12191000],
    'goat_milk': [12192000]
}

fao_animal_product_codes = {
    'cattle_meat': "21111.01",
    'sheep_meat': "21115",
    'goat_meat': "21116",
    'cattle_milk': "2211",
    'sheep_milk': "2291",
    'goat_milk': "2292"
}

eurostat_animal_product_production_codes = {
    'cattle_meat': "B1000",
    'sheep_meat': "B4100",
    'goat_meat': "B4200",
    'cattle_milk': "D1110D",
    'sheep_milk': "D1120D",
    'goat_milk': "D1130D"
}

# load population tables
population_file_names = {
    'cattle': "glw4_nuts0_cattle_population_.csv",
    'sheep': "glw4_nuts0_sheep_population_.csv",
    'goat': "glw4_nuts0_goat_population_.csv",
}

print("Loading population data...")
for animal in animals:
    population_column_name = f"{animal}_population_heads"
    population_df = pd.read_csv(INPUT_DATA_FOLDER + COMMODITY_PRICES_LIVESTOCK_FOLDER + population_file_names[animal], encoding='utf-8')
    population_df.rename(columns={"NUTS_ID": "Country_NUTS_Code"}, inplace=True)
    out_df = pd.merge(out_df, population_df[['Country_NUTS_Code', 'population']], on='Country_NUTS_Code', how='left')
    out_df.rename(columns={'population': population_column_name}, inplace=True)

# load price tables
print("Loading price data...")
# start with eurostat, then take fao if not available
eurostat_prices_df = pd.read_csv(INPUT_DATA_FOLDER + COMMODITY_PRICES_LIVESTOCK_FOLDER + "EUROSTAT_price_per_100kg_apri_ap_anouta.csv", encoding='utf-8')
fao_prices_df = pd.read_csv(INPUT_DATA_FOLDER + COMMODITY_PRICES_LIVESTOCK_FOLDER + "Prices_Cattle_Sheep_Goat_meat_and_milk_FAOSTAT.csv", encoding='utf-8')
fao_prices_df['Item Code (CPC)'] = fao_prices_df['Item Code (CPC)'].astype(str)
for animal_product in animal_products:
    animal_product_price_column_name = f"{animal_product}_price_eur2021/tonne"
    animal_product_price_source_column_name = f"{animal_product}_price_source"
    eurostat_product_codes = eurostat_animal_product_price_codes[animal_product]
    animal_product_price = np.nan
    source = np.nan
    for nuts0 in countries_df['Country_NUTS_Code'].unique():
        selected_country_prices_df = eurostat_prices_df[eurostat_prices_df['geo'] == nuts0]
        animal_product_prices = list() # list of all eurostat product prices belonging to this animal product
        for eurostat_product_code in eurostat_product_codes:
            selected_country_product_prices_df = selected_country_prices_df[selected_country_prices_df['prod_ani'] == eurostat_product_code]
            value, year = findMostRecent(selected_country_product_prices_df, startYear=2021, stopYear=2013)
            corrected_value = correctForInflation(value, year)
            animal_product_prices.append(value * 10) # from eur2021/100kg to eur2021/tonne
        # take the mean price of all eurostat product types belonging to 
        animal_product_price = np.nanmean(animal_product_prices) # ignoring nans for the mean
        if not np.isnan(animal_product_price):
            source = "eurostat"
        else:
            # apparently there are no available values in the eurostat table
            # try the fao table instead
            country_name = countries_df.loc[countries_df['Country_NUTS_Code'] == nuts0, 'Country_Name'].item()
            selected_country_prices_df = fao_prices_df[fao_prices_df['Area'] == country_name]
            fao_product_price_code = fao_animal_product_codes[animal_product]
            selected_country_product_prices_df = selected_country_prices_df[selected_country_prices_df['Item Code (CPC)'] == fao_product_price_code]
            # get most recent year
            for year in range(2021, 2010, -1):
                if not year in selected_country_product_prices_df['Year'].unique():
                    continue
                fao_price_usd = float(selected_country_product_prices_df.loc[selected_country_product_prices_df['Year'] == year, 'Value'].item())
                fao_price_eur = convertUSDtoEUR(fao_price_usd, year)
                fao_price_eur2021 = correctForInflation(fao_price_eur, year)
                animal_product_price = fao_price_eur2021
                source = "fao"
                break
        if np.isnan(animal_product_price):
            # print(f"COULD NOT FIND price for country {nuts0} and product {animal_product}")
            if nuts0 not in missing:
                missing[nuts0] = list()
            missing[nuts0].append(f"{animal_product}_price")
        else:
            # print(f"Found price {animal_product_price} from {source} for country {nuts0} and product {animal_product}")
            country_mask = out_df['Country_NUTS_Code'] == nuts0
            out_df.loc[country_mask, [animal_product_price_column_name]] = animal_product_price
            out_df.loc[country_mask, [animal_product_price_source_column_name]] = source

# load production tables
print("Loading production data...")
eurostat_milk_production_df = pd.read_csv(INPUT_DATA_FOLDER + COMMODITY_PRICES_LIVESTOCK_FOLDER + "EUROSTAT_milk_production_1000tonnes_apro_mk_pobta.csv", encoding='utf-8')
eurostat_meat_production_df = pd.read_csv(INPUT_DATA_FOLDER + COMMODITY_PRICES_LIVESTOCK_FOLDER + "EUROSTAT_slaughterings1000tonnes_apro_mt_pann.csv", encoding='utf-8')
eurostat_production_dfs = {
    'milk': eurostat_milk_production_df,
    'meat': eurostat_meat_production_df
}
eurostat_code_columns = {
    'milk': "dairyprod",
    'meat': "meat"
}
fao_production_df = pd.read_csv(INPUT_DATA_FOLDER + COMMODITY_PRICES_LIVESTOCK_FOLDER + "Production_Cattle_Sheep_Goat_meat_and_milk_FAOSTAT.csv", encoding='utf-8', dtype={'Item Code (CPC)': str})
fao_production_df.drop(fao_production_df[fao_production_df['Unit'] != 't'].index, inplace=True)

for product in products:
    eurostat_production_df = eurostat_production_dfs[product]
    eurostat_code_column = eurostat_code_columns[product]
    for animal in animals:
        animal_product = f"{animal}_{product}"
        animal_product_production_column_name = f"{animal_product}_production_tonnes"
        animal_product_production_source_column_name = f"{animal_product}_production_source"
        animal_product_production = np.nan
        source = np.nan
        eurostat_animal_product_production_code = eurostat_animal_product_production_codes[animal_product]
        eurostat_animal_product_production_df = eurostat_production_df[eurostat_production_df[eurostat_code_column] == eurostat_animal_product_production_code]
        for nuts0 in countries_df['Country_NUTS_Code'].unique():
            selected_country_production_df = eurostat_animal_product_production_df[eurostat_animal_product_production_df['geo'] == nuts0]
            value, year = findMostRecent(selected_country_production_df, startYear=2021, stopYear=2013)
            animal_product_production = value
            if not np.isnan(animal_product_production):
                source = "eurostat"
            else:
                # check fao table
                fao_animal_product_code = fao_animal_product_codes[animal_product]
                country_name = countries_df.loc[countries_df['Country_NUTS_Code'] == nuts0, 'Country_Name'].item()
                selected_country_production_df = fao_production_df[fao_production_df['Area'] == country_name]
                selected_country_product_production_df = selected_country_production_df[selected_country_production_df['Item Code (CPC)'].astype(str) == fao_animal_product_code]
                # get most recent year
                for year in range(2021, 2010, -1):
                    if not year in selected_country_product_production_df['Year'].unique():
                        continue
                    fao_production = float(selected_country_product_production_df.loc[selected_country_product_production_df['Year'] == year, 'Value'].item())
                    animal_product_production = fao_production
                    source = "fao"
                    break
            if np.isnan(animal_product_production):
                # print(f"COULD NOT FIND production value for country {nuts0} and product {animal_product}")
                if nuts0 not in missing:
                    missing[nuts0] = list()
                missing[nuts0].append(f"{animal_product}_production")
            else:
                # print(f"Found production value {animal_product_production} from {source} for country {nuts0} and product {animal_product}")
                country_mask = out_df['Country_NUTS_Code'] == nuts0
                out_df.loc[country_mask, [animal_product_production_column_name]] = animal_product_production
                out_df.loc[country_mask, [animal_product_production_source_column_name]] = source

# calculate national production values
print("Calculating production values and value per head...")
for animal_product in animal_products:
    out_df[f"{animal_product}_production_value_eur2021"] = out_df[f"{animal_product}_production_tonnes"] * out_df[f"{animal_product}_price_eur2021/tonne"]

for animal in animals:
    value_sum = 0
    for product in products:
        value_sum += out_df[f"{animal}_{product}_production_value_eur2021"].fillna(0.0)
    out_df[f"{animal}_value_eur2021/head"] = value_sum / out_df[f"{animal}_population_heads"]

out_df.to_csv("out/commodity_livestock_sanitized.csv", encoding='utf-8')

print("Missing data inputs per country:")
for k, v in missing.items():
    print(f"{k}: {v}")