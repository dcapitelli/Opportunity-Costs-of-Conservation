import pandas as pd
import numpy as np

# input files
INPUT_DATA_FOLDER = "./in/"
LAND_RENT_ARABLE_PASTORAL_FOLDER = "land_rent/arable_pastoral/"
COMMON_FOLDER = "common/"

NUTS2_REGION_FILE = INPUT_DATA_FOLDER + COMMON_FOLDER + "NUTS2_regions.csv"
INFLATION_RATE_INPUT_FILE = INPUT_DATA_FOLDER + COMMON_FOLDER + "Inflation_rate_to_2021.csv"
ARABLE_OR_PASTORAL_RENTS_INPUT_FILE = INPUT_DATA_FOLDER + LAND_RENT_ARABLE_PASTORAL_FOLDER + "apri_lrnt_arable_or_pastoral_linear.csv"
ARABLE_RENTS_INPUT_FILE = INPUT_DATA_FOLDER + LAND_RENT_ARABLE_PASTORAL_FOLDER + "apri_lrnt_arable_linear.csv"
PASTORAL_RENTS_INPUT_FILE = INPUT_DATA_FOLDER + LAND_RENT_ARABLE_PASTORAL_FOLDER + "apri_lrnt_pastoral_linear.csv"

# nuts2 regions
nuts2_regions_df = pd.read_csv(NUTS2_REGION_FILE, encoding='utf-8')

print(nuts2_regions_df.head())

# inflation rates
inflation_to_2021_df = pd.read_csv(INFLATION_RATE_INPUT_FILE, encoding='utf-8')
inflation_to_2021_df = inflation_to_2021_df.set_index('Year')

# arable or pastoral rent
arable_rents_df = pd.read_csv(ARABLE_RENTS_INPUT_FILE, encoding='utf-8')
pastoral_rents_df = pd.read_csv(PASTORAL_RENTS_INPUT_FILE, encoding='utf-8')
a_or_p_rents_df = pd.read_csv(ARABLE_OR_PASTORAL_RENTS_INPUT_FILE, encoding='utf-8')

print(arable_rents_df.head())

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

def findValue(nuts_level_codes, arable_dfs, pastoral_dfs, a_or_p_dfs, arable_or_pastoral):
    year = 2021
    value = None
    source = None
    if arable_or_pastoral != "arable" and arable_or_pastoral != "pastoral":
        raise Exception(f"Invalid argument {arable_or_pastoral}: argument arable_or_pastoral has to be either 'arable' or 'pastoral'")
    while year > 2010:
        # print(year)
        for nuts_level, nuts_code in enumerate(nuts_level_codes):
            # print(f"Checking at NUTS level {nuts_level}")
            # first check: is the year directly available in the df?
            if arable_or_pastoral == "arable":
                value = checkYear(arable_dfs[nuts_code], year)
            else:
                value = checkYear(pastoral_dfs[nuts_code], year)
            if value is not None:
                source = f"{arable_or_pastoral}_{year}_{nuts_code}"
                return (value, source)
            # second check: is the year available in the arable/pastoral df of the nuts2 region?
            value = checkYear(a_or_p_dfs[nuts_code], year)
            if value is not None:
                # option 1: directly return the arable/pastoral value
                source = f"arable/pastoral_{year}_{nuts_code}"
                return (value, source)
                # option 2: first check if not also in opposite df (not used any more)
                # before we celebrate, check if the value in the opposite df is the same as that in arable/pastoral.
                # if so, we consider the arable/pastoral value to be incorrect and move on
                # if arable_or_pastoral == "arable":
                #     opposite = pastoral_dfs[nuts_code]
                # else:
                #     opposite = arable_dfs[nuts_code]
                # if checkYear(opposite, year) is not value:
                #     # if the two values are different, we are happy to take the arable/pastoral value
                #     source = f"arable/pastoral_{year}_{nuts_code}"
                #     return (value, source)
                # raise Exception(f"Found the same value {value} while finding {arable_or_pastoral} for {nuts_code} at {year}")
        year = year - 1
    return (None, None)

out_df = nuts2_regions_df.filter(['NUTS_ID', 'CNTR_CODE', 'NUTS_NAME'])
out_df['ARABLE_LAND_RENT_EUR2021/HA'] =np.nan
out_df['ARABLE_LAND_RENT_ORIGIN'] = np.nan
out_df['PASTORAL_LAND_RENT_EUR2021/HA'] = np.nan
out_df['PASTORAL_LAND_RENT_ORIGIN'] = np.nan

for index, row in out_df.iterrows():
    nuts2_region_code = row['NUTS_ID']
    nuts1_region_code = nuts2_region_code[:-1]
    nuts0_region_code = row['CNTR_CODE']
    print(f"Processing {nuts2_region_code} ({nuts1_region_code}/{nuts0_region_code})")

    nuts2_region_arable = arable_rents_df[arable_rents_df['geo'] == nuts2_region_code]
    nuts1_region_arable = arable_rents_df[arable_rents_df['geo'] == nuts1_region_code]
    nuts0_region_arable = arable_rents_df[arable_rents_df['geo'] == nuts0_region_code]
    nuts2_region_pastoral = pastoral_rents_df[pastoral_rents_df['geo'] == nuts2_region_code]
    nuts1_region_pastoral = pastoral_rents_df[pastoral_rents_df['geo'] == nuts1_region_code]
    nuts0_region_pastoral = pastoral_rents_df[pastoral_rents_df['geo'] == nuts0_region_code]
    nuts2_region_a_or_p = a_or_p_rents_df[a_or_p_rents_df['geo'] == nuts2_region_code]
    nuts1_region_a_or_p = a_or_p_rents_df[a_or_p_rents_df['geo'] == nuts1_region_code]
    nuts0_region_a_or_p = a_or_p_rents_df[a_or_p_rents_df['geo'] == nuts0_region_code]

    nuts_level_codes = [nuts2_region_code, nuts1_region_code, nuts0_region_code]
    arable_dfs = {nuts2_region_code: nuts2_region_arable, nuts1_region_code: nuts1_region_arable, nuts0_region_code: nuts0_region_arable}
    pastoral_dfs = {nuts2_region_code: nuts2_region_pastoral, nuts1_region_code: nuts1_region_pastoral, nuts0_region_code: nuts0_region_pastoral}
    a_or_p_dfs = {nuts2_region_code: nuts2_region_a_or_p, nuts1_region_code: nuts1_region_a_or_p, nuts0_region_code: nuts0_region_a_or_p}

    # arable
    value, source = findValue(nuts_level_codes, arable_dfs, pastoral_dfs, a_or_p_dfs, "arable")
    if value is None:
        print(f"Failed to find arable value for {nuts2_region_code}")
    else:
        print(f"Found arable {value} from {source}")
        out_df.at[index, "ARABLE_LAND_RENT_EUR2021/HA"] = value
        out_df.at[index, "ARABLE_LAND_RENT_ORIGIN"] = source

    # pastoral
    value, source = findValue(nuts_level_codes, arable_dfs, pastoral_dfs, a_or_p_dfs, "pastoral")
    if value is None:
        print(f"Failed to find pastoral value for {nuts2_region_code}")
    else:
        print(f"Found pastoral {value} from {source}")
        out_df.at[index, "PASTORAL_LAND_RENT_EUR2021/HA"] = value
        out_df.at[index, "PASTORAL_LAND_RENT_ORIGIN"] = source

out_df.to_csv("out/arable_pastoral_rents_sanitized.csv", encoding='utf-8')

missing_arable = out_df['ARABLE_LAND_RENT_ORIGIN'].isna()
missing_pastoral = out_df['PASTORAL_LAND_RENT_ORIGIN'].isna()
print(f"Missing {missing_arable.sum()} NUTS2 regions for arable land rent (out of {len(out_df)} total NUTS2 regions)")
print(f"Missing {missing_pastoral.sum()} NUTS2 regions for pastoral land rent (out of {len(out_df)} total NUTS2 regions)")

out_df[missing_arable].to_csv('out/arable_pastoral_rents_missing.csv', encoding='utf-8')