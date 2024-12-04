import pandas as pd

DATASET_TO_COMPARE = 'in/commodity_prices/livestock/tgs00045_swine_domestic.csv'
NUTS2_KEY = 'geo'

nuts2 = pd.read_csv('in/common/NUTS2_regions.csv', encoding='utf-8')
all_nuts2 = set(nuts2['NUTS_ID'].unique())

other = pd.read_csv(DATASET_TO_COMPARE, encoding='utf-8')
other_nuts2 = set(other[NUTS2_KEY].unique())

print("In NUTS2_Regions, but not in provided dataset")
print(sorted(all_nuts2.difference(other_nuts2)))

print("In provided dataset, but not a valid NUTS2 Region")
print(sorted(other_nuts2.difference(all_nuts2)))
