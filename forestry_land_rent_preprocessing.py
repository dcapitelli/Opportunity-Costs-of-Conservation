"""
Script which preprocesses the various data inputs and creates a forestry_rent_sanitized.csv with land rents for forestry

"""

import pandas as pd
from math import isclose

# constants
USD2023_TO_EUR2021_EXCHANGE_RATE = 0.751424

# input files
INPUT_DATA_FOLDER = "./in/"
LAND_RENT_FORESTRY_FOLDER = "land_rent/forestry/"
COMMON_FOLDER = "common/"

FORESTRY_RENTS_INPUT_FILE = INPUT_DATA_FOLDER + LAND_RENT_FORESTRY_FOLDER + "Forest_rent_per_GDP.csv"
FORESTRY_AREA_INPUT_FILE = INPUT_DATA_FOLDER + LAND_RENT_FORESTRY_FOLDER + "Forest_cells_in_hectares.csv"
COUNTRIES_FILE = INPUT_DATA_FOLDER + COMMON_FOLDER + "NaturaConnect_Countries.csv"
GDP_FILE = INPUT_DATA_FOLDER + COMMON_FOLDER + "GDP_country.csv"

# countries relevant to the project with NUTS codes (where applicable) and ISO three-letter codes
countries_df = pd.read_csv(COUNTRIES_FILE, encoding='utf-8')

# forestry rent
with open(FORESTRY_RENTS_INPUT_FILE, 'r') as f:
    forestry_rents_df = pd.read_csv(f, encoding='utf-8')
    forestry_rents_df = forestry_rents_df.rename(columns={'Country Code': 'Country_ISO_Code'})
    # get latest rent value
    forestry_rents_df['Forestry_rent_%GDP'] = 0
    for index, row in forestry_rents_df.iterrows():
        # we only really need to do this for countries in europe that we're interested in, skip the rest
        if row['Country_ISO_Code'] not in countries_df['Country_ISO_Code'].values:
            continue
        # start with 2022, then decrease year by year
        year = 2022
        while True:
            # print(f"Try year {year} for country {row['Country_Name']}")
            year_column = f"{year}"
            try:
                # if no value exists or it is not a float, we cause an exception/let it happen, and catch it
                if pd.isna(row[year_column]):
                    raise ValueError("NaN value")
                # if the rent value is zero, check if it was non-zero in the past, and if so take the most recent non-zero value
                elif isclose(float(row[year_column]), 0.0):
                    raise ValueError("Zero value")
                forestry_rents_df.at[index,'Forestry_rent_%GDP'] = float(row[year_column])
            except:
                year = year - 1
                # if we don't have a value by 1960, we give up...
                if year < 1960:
                    # apparently only ever zero or NaN, so let's take zero
                    forestry_rents_df.at[index,'Forestry_rent_%GDP'] = 0.0
                    break
                continue
            else:
                break
    forestry_rents_df = forestry_rents_df.filter(['Country_ISO_Code', 'Forestry_rent_%GDP'])
    # merge with the countries_df and keep only the relevant countries by doing a left join
    forestry_rents_df = countries_df.merge(forestry_rents_df, how='left', on='Country_ISO_Code')
    # set the ISO code as the index
    forestry_rents_df = forestry_rents_df.set_index('Country_ISO_Code')

# forestry area
with open(FORESTRY_AREA_INPUT_FILE, 'r') as f:
    forestry_area_df = pd.read_csv(f, encoding='utf-8')
    forestry_area_df = forestry_area_df.filter(['Country_NUTS_ID', 'Ha_forest_cells'])
    forestry_area_df = forestry_area_df.rename(columns={
        'Country_NUTS_ID': 'Country_NUTS_Code',
        'Ha_forest_cells': 'Forestry_area_ha'
    })
    # merge with the countries_df and keep only the relevant countries by doing a left join
    forestry_area_df = countries_df.merge(forestry_area_df, how='left', on='Country_NUTS_Code')
    # forestry_area_df = forestry_area_df.set_index('Country_NUTS_Code')

# gdp
with open(GDP_FILE, 'r') as f:
    gdp_df = pd.read_csv(f, encoding='utf-8')
    gdp_df = gdp_df.rename(columns={'Country Code': 'Country_ISO_Code'})
    gdp_df = gdp_df.set_index('Country_ISO_Code')
    # get latest gdp
    gdp_df['GDP_USD2023'] = 0
    for index, row in gdp_df.iterrows():
        year = 2022
        while True:
            # print(f"Try year {year} for country {row['Country_Name']}")
            year_column = f"{year} [YR{year}]"
            try:
                gdp_df.at[index,'GDP_USD2023'] = float(row[year_column])
            except Exception as e:
                year = year - 1
                # if we don't have a value by 1990, we give up...
                if year < 1990:
                    raise Exception(f"No GDP value was found for country {row['Country_ISO_Code']}")
                continue
            else:
                break
    gdp_df['GDP_EUR2021'] = gdp_df['GDP_USD2023'] * USD2023_TO_EUR2021_EXCHANGE_RATE
    gdp_df = gdp_df.filter(['Country_ISO_Code', 'GDP_USD2023', 'GDP_EUR2021'])
    # merge with the countries_df and keep only the relevant countries by doing a left join
    gdp_df = countries_df.merge(gdp_df, how='left', on='Country_ISO_Code')
    # set the ISO code as the index
    gdp_df = gdp_df.set_index('Country_ISO_Code')

# merge forestry rents with the forestry area
forestry_df = forestry_rents_df.merge(forestry_area_df, how='left', on=['Country_Name','Country_ISO_Code','Country_NUTS_Code'])
# merge forestry rents + area with the gdp dataframe
forestry_df = forestry_df.merge(gdp_df, how='left', on=['Country_Name','Country_ISO_Code','Country_NUTS_Code'])
# convert %gdp to eur
forestry_df['Forestry_rent_EUR2021'] = forestry_df['Forestry_rent_%GDP'] * forestry_df['GDP_EUR2021'] / 100
# calculate eur/ha based on total ha forestry and total eur per country
forestry_df['Forestry_rent_EUR2021/ha'] = forestry_df['Forestry_rent_EUR2021'] / forestry_df['Forestry_area_ha']
# possibly set nans to zero since countries with zero hectares of forestry could have led to divisions by zero
# forestry_df['Forestry_rent_EUR2021/ha'].fillna(0, inplace=True)
forestry_df.set_index('Country_ISO_Code',inplace=True)

print(forestry_df)

forestry_df.to_csv("./out/forestry_rent_sanitized.csv", encoding='utf-8')