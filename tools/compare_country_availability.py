import pandas as pd

DATASET_TO_COMPARE = "in\commodity_prices\livestock\EUROSTAT Production of raw cow's milk_1000t.csv"

nc_countries = pd.read_csv('in/common/NaturaConnect_Countries.csv', encoding='utf-8')
all_nc_countries = set(nc_countries['Country_Name'].unique())

other = pd.read_csv(DATASET_TO_COMPARE, encoding='utf-8')
other_countries = set(other['GEO (Labels)'].unique())

print("Is a NaturaConnect country, but not in provided dataset:")
print(sorted(all_nc_countries.difference(other_countries)))

print("Is provided, but is not a NaturaConnect country:")
print(sorted(other_countries.difference(all_nc_countries)))