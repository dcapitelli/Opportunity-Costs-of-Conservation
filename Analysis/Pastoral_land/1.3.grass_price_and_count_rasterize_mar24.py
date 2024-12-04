## notes for optimising workflow for this script: adjust the raster output names to the following burn name: catt_val, goat_val, shee_val.
## do this by changing the column name of the csv livestock price doc

# Vectorize the grass prices
import pandas as pd
import numpy as np
import geopandas as gpd

livestock_prices_national_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Livestock prices/commodity_livestock_sanitized_IMAGE_rescaled_mar24.csv"
#updated path
livestock_prices_national_check = pd.read_csv(livestock_prices_national_path)

## for exchanging 0's and NaN's with each other
# livestock_price_0nan = livestock_prices_national_check.replace(0.000000, np.nan, inplace=True)
# livestock_price_nan0 = livestock_prices_national_check['rice_price_eur2021/kg'].replace(0, np.nan, inplace=True)
# livestock_prices_national_check['rice_price_eur2021/kg']
# livestock_price_nan0 = livestock_prices_national_check.mask(np.isclose(livestock_prices_national_check.values, 0.000000))
# livestock_prices_national_check_nan_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Crop_prices/livestock_prices_national_check_nan.csv"
# livestock_prices_national_check.to_csv(livestock_prices_national_check_nan_path)
# vector0 = vector.fillna(0)


# clean up and remove columns
livestock_prices_national_check.columns
dropcols = ['cattle_population_heads','sheep_population_heads',
            'goat_population_heads','cattle_meat_price_eur2021/tonne','cattle_meat_price_source', 
            'sheep_meat_price_eur2021/tonne','sheep_meat_price_source', 'goat_meat_price_eur2021/tonne',
            'goat_meat_price_source', 'cattle_milk_price_eur2021/tonne','cattle_milk_price_source', 
            'sheep_milk_price_eur2021/tonne','sheep_milk_price_source', 'goat_milk_price_eur2021/tonne',
            'goat_milk_price_source', 'cattle_meat_production_tonnes','cattle_meat_production_source', 'WRONGcattle_meat_production_tonnes','WRONGsheep_meat_production_tonnes','WRONGgoat_meat_production_tonnes',
            'sheep_meat_production_tonnes','sheep_meat_production_source', 'goat_meat_production_tonnes',
            'goat_meat_production_source', 'cattle_milk_production_tonnes','cattle_milk_production_source', 
            'sheep_milk_production_tonnes','sheep_milk_production_source', 'goat_milk_production_tonnes','OLD_cattle_value_eur2021/head',
            'OLD_sheep_value_eur2021/head', 'OLD_goat_value_eur2021/head',
            'goat_milk_production_source', 'cattle_meat_production_value_eur2021','sheep_meat_production_value_eur2021',
            'goat_meat_production_value_eur2021']
livestock_prices_national_cleaned = livestock_prices_national_check.drop(columns= dropcols)
livestock_prices_national_cleaned = livestock_prices_national_cleaned.rename(columns={'Country_NUTS_Code': 'CNTR_COD_1'}) #
livestock_prices_national_cleaned['Num_rows'] = (livestock_prices_national_cleaned[['cattle_value_eur2021/head','sheep_value_eur2021/head','goat_value_eur2021/head']] > 0).sum(axis=1)
livestock_prices_national_cleaned.to_csv("C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Livestock prices/mar24_livestock_prices_national_check_nan.csv")



# Merge the nuts0 and crop price count datasets
nuts0_polygon_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/NUTS_regions_missing_countries/reference_vector_feb_24/reference_vector_mar_24_cleaned.shp"
nuts0_polygon = gpd.read_file(nuts0_polygon_path)
nuts0_polygon.columns
nuts0_polygon_livestock_price_count = nuts0_polygon.merge(livestock_prices_national_cleaned, on="CNTR_COD_1")

nuts0_polygon_livestock_price_count.columns
dropcols = ['cattle_milk_production_value_eur2021',
            'sheep_milk_production_value_eur2021',
            'goat_milk_production_value_eur2021']
nuts0_polygon_livestock_price_count_clean = nuts0_polygon_livestock_price_count.drop(columns= dropcols)

# Rasterize the ['Num_rows']
import rasterio
from rasterio import features
from rasterio.enums import MergeAlg
from rasterio.plot import show
from numpy import int16

# Read in vector
vector = nuts0_polygon_livestock_price_count_clean
livestock_price_count_vector_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/mar24_eu_nuts0_livestock_prices.shp"
vector.to_file(livestock_price_count_vector_path)


# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

# create tuples of geometry, value pairs, where value is the attribute value you want to burn
geom_value = ((geom,value) for geom, value in zip(vector.geometry, vector['Num_rows']))

# Rasterize vector using the shape and transform of the raster
rasterized = features.rasterize(geom_value,
                                out_shape = raster.shape,
                                transform = raster.transform,
                                all_touched = False,
                                fill = -99,   # background value
                                merge_alg = MergeAlg.replace,
                                dtype = float)


# save the rasterized vector out
with rasterio.open(
        'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/mar24_eu_nuts0_livestock_price_count.tif', "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)



## end of vectorize script


# Rasterize the grass prices
import geopandas as gpd
import rasterio
from rasterio import features
from rasterio.enums import MergeAlg
from rasterio.plot import show
from numpy import int16



# Read in vector
vector = gpd.read_file(livestock_price_count_vector_path)
print(vector.columns)

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'cattle_val'

burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

# create tuples of geometry, value pairs, where value is the attribute value you want to burn

geom_value = ((geom,value) for geom, value in zip(vector.geometry, burn_value))

# Rasterize vector using the shape and transform of the raster
rasterized = features.rasterize(geom_value,
                                out_shape = raster.shape,
                                transform = raster.transform,
                                all_touched = False,
                                fill = -99,   # background value
                                merge_alg = MergeAlg.replace,
                                dtype = float)


# save the rasterized vector out
with rasterio.open(
        f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/grass_biomass_eu/grass_prices/MAR24_eu_nuts0_livestock_price_{burn_name}_euros_heads.tif', "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/grass_biomass_eu/grass_prices/eu_nuts0_livestock_price_{burn_name}_euros_heads.tif ')


#################################
### repeatable section of code ##
#################################

burn_name ='sheep_valu'

burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

# create tuples of geometry, value pairs, where value is the attribute value you want to burn

geom_value = ((geom,value) for geom, value in zip(vector.geometry, burn_value))

# Rasterize vector using the shape and transform of the raster
rasterized = features.rasterize(geom_value,
                                out_shape = raster.shape,
                                transform = raster.transform,
                                all_touched = False,
                                fill = -99,   # background value
                                merge_alg = MergeAlg.replace,
                                dtype = float)


# save the rasterized vector out
with rasterio.open(
        f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/grass_biomass_eu/grass_prices/MAR24_eu_nuts0_livestock_price_{burn_name}_euros_heads.tif', "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/grass_biomass_eu/grass_prices/MAR24_eu_nuts0_livestock_price_{burn_name}_euros_heads.tif ')


#################################
### repeatable section of code ##
#################################

burn_name ='goat_value'

burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

# create tuples of geometry, value pairs, where value is the attribute value you want to burn

geom_value = ((geom,value) for geom, value in zip(vector.geometry, burn_value))

# Rasterize vector using the shape and transform of the raster
rasterized = features.rasterize(geom_value,
                                out_shape = raster.shape,
                                transform = raster.transform,
                                all_touched = False,
                                fill = -99,   # background value
                                merge_alg = MergeAlg.replace,
                                dtype = float)


# save the rasterized vector out
with rasterio.open(
        f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/grass_biomass_eu/grass_prices/MAR24_eu_nuts0_livestock_price_{burn_name}_euros_heads.tif', "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/grass_biomass_eu/grass_prices/eu_nuts0_livestock_price_{burn_name}_euros_heads.tif ')

print("#~~~~~End~~of~~script~~~~~~~#")