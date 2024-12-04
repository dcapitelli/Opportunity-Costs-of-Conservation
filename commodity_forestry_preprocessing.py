import pandas as pd

# input files
INPUT_DATA_FOLDER = "./in/"
COMMODITY_PRICES_FORESTRY_FOLDER = "commodity_prices/forestry/"
COMMON_FOLDER = "common/"

FORESTRY_ROUNDWOOD_PRICES_INPUT_FILE = INPUT_DATA_FOLDER + COMMODITY_PRICES_FORESTRY_FOLDER + "forestry_roundwood_prices.csv"
COUNTRIES_FILE = INPUT_DATA_FOLDER + COMMON_FOLDER + "NaturaConnect_Countries.csv"

# country names and codes
countries_df = pd.read_csv(COUNTRIES_FILE, encoding='utf-8')

# forestry prices
forestry_prices_df = pd.read_csv(FORESTRY_ROUNDWOOD_PRICES_INPUT_FILE, encoding='utf-8')
forestry_prices_df = forestry_prices_df.rename(columns={'Country': 'Country_Name'})

# merge dataframes on country df
forestry_prices_df = countries_df.merge(forestry_prices_df, how='left', on=['Country_Name'])
forestry_prices_df.set_index('Country_ISO_Code', inplace=True)

print(forestry_prices_df)

forestry_prices_df.to_csv("./out/forestry_prices_sanitized.csv", encoding='utf-8')