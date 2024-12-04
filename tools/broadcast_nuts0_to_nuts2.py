"""
Script that can be used to convert from country-level data to NUTS2 region data
The country-level data has to have a column with the NUTS0 ID / country code specified
Based on that and the NUTS2_regions.csv file, the national data is broadcast over its NUTS2 regions
"""

import pandas as pd

# file with national values
NUTS0_FILE = "out/spam_crop_prices_national_sanitized.csv"
NUTS0_FILE_COUNTRY_CODE_NAME = "Country_NUTS_Code"
# file to be created
NUTS2_FILE = "out/tmp_to_nuts2.csv"

print("Broadcasting NUTS0 data to NUTS2 regions...")

nuts2_regions_df = pd.read_csv("in/common/NUTS2_regions.csv", encoding='utf-8')
national_df = pd.read_csv(NUTS0_FILE, encoding='utf-8')

nuts2_regions_df = nuts2_regions_df.filter(['NUTS_ID', 'LEVL_CODE', 'CNTR_CODE', 'NUTS_NAME'])
nuts2_regions_df = nuts2_regions_df.sort_values(by=['NUTS_ID'])

nuts2_out_df = nuts2_regions_df.merge(national_df.rename(columns={NUTS0_FILE_COUNTRY_CODE_NAME: 'CNTR_CODE'}), how='left', on='CNTR_CODE')

# final result
nuts2_out_df.to_csv(NUTS2_FILE, encoding='utf-8')