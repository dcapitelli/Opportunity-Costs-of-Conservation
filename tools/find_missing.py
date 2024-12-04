import pandas as pd

# which file you want to check
FILE = "out/commodity_livestock_sanitized.csv"
# column name where the country names are
COUNTRY_COLUMN = "Country_Name"

# adapt this function based on what columns you want to ignore
def canIgnore(column_name : str):
    return column_name.endswith("production_value_eur2021") or column_name.endswith("source")

df = pd.read_csv(FILE, encoding='utf-8')

print(f"Missing values in {FILE}, per country:")

for index, row in df.iterrows():
    country = row[COUNTRY_COLUMN]
    country_missing = list()
    for name, value in row.items():
        if canIgnore(name):
            continue
        if pd.isna(value):
            country_missing.append(name)
    print(f"{country}: {country_missing}")


    