

# Import libraries
import os 
# 1.0
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import rasterio
from rasterio import features
from rasterio.enums import MergeAlg
from rasterio.plot import show
from numpy import int16
#1.1.
import numpy as np
from numpy import float32
from numpy import inf
#1.2.0.
from rasterio.merge import merge
#1.2.2.
# no new libraries
#1.3.
import rasterstats
#1.4.
# no new libraries

# housekeeping
# checking whether file paths exist
def check_file_exists(filepath):
    if os.path.exists(filepath):
        print(f"The file at '{filepath}' exists.")
    else:
        print(f"The file at '{filepath}' does not exist.")

# basic version control
old_version = 'mar24_master_run_1_'
version = 'oct24_master_run_1_'
print(f" run = {version}")
# mar24_master_run__ = first run with the whole of the forest run
        # IN_wood_product_prices_path = project_path + /Input_datasets/forestry_prices_with_nuts0_codes_used_ changed to include neighbour average.csv
# mar24_master_run_1_ = run with update of forestry prices and forest rents (new LULC forestry area: forestry_rent_sanitized_KO_MT.csv)

# Set file paths
project_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries"

#1.0. paths
# static paths
IN_master_vector_path = project_path + "/NUTS_regions_missing_countries/reference_vector_feb_24/reference_vector_mar_24_cleaned.shp"
IN_woody_biomass_production_path = project_path + "/NUTS_regions_missing_countries/forest_production_IMAGE_average.csv"

# dynamic paths
IN_wood_product_prices_path = project_path + "/Input_datasets/forestry_prices_with_nuts0_codes_used_ changed to include neighbour average_mar24.csv" 
IN_forestry_rent_path = project_path + "/Input_datasets/Silvicultural_land_rents/Oct24_forest_rents.csv" # UPDATED for Oct

OUT_rent_price_prod_refvector_path = project_path + f"/Throughput_datasets/{version}eu_nuts0_for_rents_prices_production.shp"

#1.1. paths
# static paths
IN_lulc = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif"

# dynamic paths
IN_master_vector_rent_woodprice_woodprod = project_path + f"/Throughput_datasets/{version}eu_nuts0_for_rents_prices_production.shp"

OUT_price_raster = project_path + f"/Throughput_datasets/{version}eu_nuts0_for_rasterize_price.tif"
OUT_rent_raster = project_path + f"/Throughput_datasets/{version}eu_nuts0_for_rasterize_rents.tif"
OUT_production_path = project_path + f"/Throughput_datasets/{version}eu_nuts0_for_rasterize_production.tif"
OUT_production_clean_path =project_path + f"/Throughput_datasets/{version}eu_nuts0_for_rasterize_production_nodata99.tif"

#1.2.0. paths
# static paths
IN_verkerk_wood_production_path = project_path + "/Input_datasets/woody_biomass_verkerk/woodprod_2010.tif"
IN_non_verkerk_wood_production_path = project_path + f"/Throughput_datasets/{version}eu_nuts0_for_rasterize_production_nodata99.tif"

OUT_production_path = project_path + f"/Throughput_datasets/forest_production/{version}merged_production_.tif"

#1.2.2.
# Static monetary yield paths
IN_forest_prices_cleaned_path = project_path + f"/Throughput_datasets/{version}eu_nuts0_for_rasterize_price.tif" # DOUBLE CHECK THIS ONE WITH OLD SCRIPT
IN_merged_production_path = project_path + f"/Throughput_datasets/forest_production/{version}merged_production_.tif"

OUT_for_monetary_yield_path = project_path + f"/Throughput_datasets/forest_monetary_yield/{version}whole_eu_forest_monetary_yield_.tif"


## Filter forest eu/ha using forest pixels ##
IN_reclass_for_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/forest_Reclass_new_LULC.tif"

OUT_for_monetary_yield_filtered = project_path + f"/Throughput_datasets/forest_monetary_yield/{version}whole_eu_forest_monetary_yield_filtered_.tif"
OUT_for_monetary_yield_filtered_binary_mask = project_path + f"/Throughput_datasets/forest_monetary_yield/{version}whole_eu_forest_monetary_yield_binary_mask_.tif"


#1.3. paths
IN_master_vector_path = project_path + "/NUTS_regions_missing_countries/reference_vector_feb_24/reference_vector_mar_24_cleaned_NUTS0.shp"
IN_for_yij_gridded_path = project_path + f"/Throughput_datasets/forest_monetary_yield/{version}whole_eu_forest_monetary_yield_filtered_.tif"
IN_for_reclass_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/forest_Reclass_new_LULC.tif"

OUT_for_yj_zonal_stats = project_path + f"/Throughput_datasets/forest_proportional_allocation_equation/{version}zonalstat_forest_yj_mean.tif"


#1.4 paths

# Static paths
IN_for_mj_rents_path = project_path + f"/Throughput_datasets/{version}eu_nuts0_for_rasterize_rents.tif"
IN_for_yj_path = project_path + f"/Throughput_datasets/forest_proportional_allocation_equation/{version}zonalstat_forest_yj_mean.tif"
IN_for_yij_path = project_path + f"/Throughput_datasets/forest_monetary_yield/{version}whole_eu_forest_monetary_yield_filtered_.tif"
# "/Throughput_datasets/forest_monetary_yield_WB_CY_MT/forest_monetary_yield_WB_CY_MT_plus_one_recfor_remove_0_minus_one_clipped_to_WB_CY_MT.tif" 
IN_reclass_for_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/forest_Reclass_new_LULC.tif"
IN_binary_yij_mask = project_path + f"/Throughput_datasets/forest_monetary_yield/{version}whole_eu_forest_monetary_yield_binary_mask_.tif"

OUT_for_mij_path = project_path + f"/Throughput_datasets/rasterized_land_rents/{version}for_allocated_rents.tif"

# checking whether input filepaths exist
input_list= [IN_master_vector_path,
IN_woody_biomass_production_path,
IN_wood_product_prices_path,
IN_forestry_rent_path,
IN_lulc,
IN_verkerk_wood_production_path,
IN_for_reclass_path,
IN_for_yij_gridded_path,
IN_reclass_for_path]

for input in input_list:
    check_file_exists(input)


#1.0. script
# read files
master_vector = gpd.read_file(IN_master_vector_path)
wood_product_prices = pd.read_csv(IN_wood_product_prices_path)
woody_biomass_production = pd.read_csv(IN_woody_biomass_production_path)
forestry_rent = pd.read_csv(IN_forestry_rent_path)

# drop or rename columns from tables as necessary
woody_biomass_production = woody_biomass_production.drop(columns=['MOUNT_TYPE','URBN_TYPE','COAST_TYPE','FID','LEVL_CODE', 'cell_count', 'cell_sum', 'cell_mean', 'prodcount', 'prodsum'])
forestry_rent = forestry_rent.rename(columns={'Country_NUTS_Code':'CNTR_CODE','Forestry_rent_EUR2021/ha':'FrE21/ha'})
wood_product_prices = wood_product_prices.rename(columns={'NUTS_ID':'CNTR_CODE'})
master_vector = master_vector.rename(columns={'CNTR_COD_1': 'CNTR_CODE'})

# 1st merge of reference vector and wood product prices
eu0_nuts_for_master_gdf = master_vector.merge(wood_product_prices, on='CNTR_CODE')
print("merge of timber prices and reference shapefile complete")
print(eu0_nuts_for_master_gdf)

# remove and rename columns
eu0_nuts_for_master_clean_gdf = eu0_nuts_for_master_gdf.drop(columns=
                                                            ['P2_group_subgroup', 'P2_price', 'P2_Year', 'P2_species', 
                                                             'P2_value', 'P2_currency', 'Final_2021EUR_per1000m3', 
                                                             'Difference in %', 'WDI_Country_Code', 'Country'])
# , # old cols from rental shapefile'Country_Na','FrnEU21','F_rn%GDP','GDP_EUR202','GDP_USD202'])
eu0_nuts_for_master_clean_gdf = eu0_nuts_for_master_clean_gdf.rename(columns={'Hybrid_Roundwood_Logs_Pulpwood_2021EUR_per1000m3': 'EU21/1k_m3',
                                                                              'NUTS_ID__2': 'NUTS_ID'})




print(eu0_nuts_for_master_clean_gdf.columns)
print(forestry_rent.columns)
eu0_nuts_for_master_clean_gdf['CNTR_CODE']
forestry_rent['geo']



# 2nd merge of ref vector and forestry rent
eu0_nuts_for_master_clean_merge2_gdf = eu0_nuts_for_master_clean_gdf.merge(forestry_rent, on='CNTR_CODE')
print("merge of forestry rents and master shapefile complete")
print(eu0_nuts_for_master_clean_merge2_gdf)




# 3rd merge of ref vector and forestry production complete
eu0_nuts_for_master_clean_merge3_gdf = eu0_nuts_for_master_clean_merge2_gdf.merge(woody_biomass_production, on='CNTR_CODE')
print("merge of forestry production and master shapefile complete")
print(eu0_nuts_for_master_clean_merge3_gdf)
eu0_nuts_for_master_clean_gdf.columns

# write file to throughput folder
# eu0_nuts_for_master_clean_gdf.to_file("C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/eu_nuts0_for_rents_prices_production_WB_CY_MT.shp")
eu0_nuts_for_master_clean_merge3_gdf.to_file(OUT_rent_price_prod_refvector_path)

# for reference
dict_for_output = {'wood_price':'EU21/1k_m3',
                   'forest_rent':'FrE21/ha',
                    'average_production':'prodmean' }
#'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/mar24_eu_nuts0_for_rents_prices_production.shp'

print("end of 1.0. script")


#1.1. script

# Read in vector ##
# Hashed out so that we can include the production values in Cyprus from the Verkerk map
vector = gpd.read_file(IN_master_vector_rent_woodprice_woodprod)


print(vector.head())

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# # Open example raster
reference_raster = rasterio.open(IN_lulc)

dict_for_output = {'wood_price':'EU21/1k_m3',
                   'forest_rent':'FrE21/ha',
                    'average_production':'prodmean' }

########################
## repeatable section ##
########################

# PRICES

burn_name = dict_for_output['wood_price']
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open(IN_lulc)

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
        OUT_price_raster, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)
# save the rasterized vector out


print(f"rasterisation of timber prices available at {OUT_price_raster}")

########################
## repeatable section ##
########################

# RENT

burn_name = dict_for_output['forest_rent']
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open(IN_lulc)

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
        OUT_rent_raster, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)
# save the rasterized vector out


print(f"rasterisation of forestry rents available at {OUT_rent_raster}")


########################
## repeatable section ##
########################

#PRODUCTION

burn_name = dict_for_output['average_production']
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open(IN_lulc)

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
        OUT_production_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)
# save the rasterized vector out


with rasterio.open(OUT_production_path) as src1:
    # Lees metadata van een invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32', compress = 'lzw')

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = OUT_production_clean_path
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1

        resultaat = raster1 # *(raster1>0) 
        resultaat[resultaat == -99] = np.NAN
        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band

print(f"rasterisation of forestry production available at {OUT_production_clean_path}")

print("end of 1.1. script")

#1.2.0. script

src1 = rasterio.open(IN_verkerk_wood_production_path)
src2 = rasterio.open(IN_non_verkerk_wood_production_path)

srcs_to_mosaic = [src1, src2]

# The merge function returns a single array and the affine transform info
arr, out_trans = merge(srcs_to_mosaic)

output_meta = src1.meta.copy()
output_meta.update(
    {"driver": "GTiff",
        "height": arr.shape[1],
        "width": arr.shape[2],
        "transform": out_trans,
    }
)

with rasterio.open(OUT_production_path, 'w', **output_meta) as m:
    m.write(arr)


print(" merge of production rasters successful ")
print(" ")
print(" merged raster available at ... ")
print(f" {OUT_production_path}")

print("end of 1.2.0. script")

#1.2.2. script

raster_path_1 = IN_forest_prices_cleaned_path
raster_path_2 = IN_merged_production_path

with rasterio.open(raster_path_1) as src1, rasterio.open(raster_path_2) as src2:
    # Lees metadata van een invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32', compress = 'lzw')

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = OUT_for_monetary_yield_path
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2
        # resultaat[resultaat == -99] = np.NAN

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print("raster calculation of forest monetary yield successful")
print(f"     available at ...  {OUT_for_monetary_yield_path}")

##############################################
## filter forest eu/ha using forest pixels  ##
##############################################

import rasterio
from rasterio.plot import show
import numpy as np
import matplotlib.pyplot as plt


# Open invoerrasters
raster1_pad = OUT_for_monetary_yield_path
raster2_pad = IN_reclass_for_path

with rasterio.open(raster1_pad) as src1, rasterio.open(raster2_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32', compress = 'lzw')

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = OUT_for_monetary_yield_filtered
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 + 1
        resultaat1 = resultaat * raster2
        resultaat1[resultaat1 == 0] = np.NAN
        resultaat2 = resultaat1 - 1
        # removing the pixels that are less than zero due to coastal miscapture
        resultaat2[resultaat2 < 0] = np.NAN

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat2, 1)  # Schrijf het resultaat naar de eerste band

print("Forestry monetary yield has been successfully calculated")
print(" ")
print("raster available at: ")
print(f" ... {uitvoer_pad}")

raster1_pad = OUT_for_monetary_yield_filtered

with rasterio.open(raster1_pad) as src:

    array = src.read()
    profile = src.profile

    # Reclassify: NaN < 210, NaN >230, 230> 1 >210
    array[np.where(array < 0)] = np.nan 
    array[np.where(array >= 0)] = 1
    
    # and so on ...  

with rasterio.open(OUT_for_monetary_yield_filtered_binary_mask, 'w', **profile) as dst:
    # Write to disk
    dst.write(array)


print("Forestry monetary yield binary mask has been successfully calculated")
print(" ")
print("raster available at: ")
print(f" ... {OUT_for_monetary_yield_filtered_binary_mask}")

print("end of 1.2.2. script")

#1.3. script

# read in the reference vector
eu_nuts0 = gpd.read_file(IN_master_vector_path)
eu_nuts0.columns

# read in the for yield raster
raster_path_1 = IN_for_yij_gridded_path
raster_path_2 = IN_for_reclass_path


# Implementation of lesson into NaturaConnect code
d = rasterstats.zonal_stats(eu_nuts0.geometry, raster_path_1, stats=['sum'])
values = [i['sum'] for i in d]
eu_nuts0['sum_for_yield_values'] = values

d= rasterstats.zonal_stats(eu_nuts0.geometry, raster_path_1, stats=['count'])
values = [i['count'] for i in d]
eu_nuts0['count_for_yield_cells'] = values

d = rasterstats.zonal_stats(eu_nuts0.geometry, raster_path_2, stats=['sum'])
values = [i['sum'] for i in d]
eu_nuts0['sum_reclulc_values'] = values

d= rasterstats.zonal_stats(eu_nuts0.geometry, raster_path_2, stats=['count'])
values = [i['count'] for i in d]
eu_nuts0['count_reclulc_cells'] = values


# 'sum_for_cells' should equal 'sum_reclulc_for'
eu_nuts0['check_cell'] = eu_nuts0['count_reclulc_cells'] - eu_nuts0['count_for_yield_cells']

print("printed value should be < 0:")
print(eu_nuts0['check_cell'].sum())
print("if value > 0, it means that the forest production map contains NaN pixels where the LULC defines pixels as forest land")

eu_nuts0['mean_for_yield'] = eu_nuts0['sum_for_yield_values'] / eu_nuts0['count_for_yield_cells']

print(eu_nuts0.iloc[:,-6:]) # view the last six columns of the dataframe

print("vector zonal analysis complete")

########################################
## Rasterise the mean from the vector ##
########################################

vector = eu_nuts0

burn_name = "mean_for_yield"
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open("C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif")

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
        OUT_for_yj_zonal_stats, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(" rasterisation complete")

print("for yj zonal statistics successful")

print(f" for yj raster available at:  {OUT_for_yj_zonal_stats}")

print("end of 1.3. script")



#1.4 script

#("Forestry_mj_rents_AIout_BH_AL_RS_MK_XK_CY_MAGNET_cleaned@1"/"zonalstat_Forestry_yj_mean@1") * "Forestry_yij_allocation_gridded_cleaned@1"  
# allocate paths
raster_1_path = IN_for_mj_rents_path
raster_2_path = IN_for_yj_path
raster_3_path = IN_for_yij_path
raster_4_path = IN_reclass_for_path
raster_5_path = IN_binary_yij_mask


with rasterio.open(raster_1_path) as src1, rasterio.open(raster_2_path) as src2, rasterio.open(raster_3_path) as src3, rasterio.open(raster_4_path) as src4, rasterio.open(raster_5_path) as src5:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32', compress = 'lzw')

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = OUT_for_mij_path
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        raster3 = src3.read(1)  # Lees eerste band van raster2
        raster4 = src4.read(1)  # Lees eerste band van raster2
        raster5 = src5.read(1)  # Lees eerste band van raster2


        resultaat = (raster1/raster2) * raster3      # "1/2" is the mj/yj and "3" is the yij, so resultaat is the mcij
        resultaat1 = resultaat + 1                   # to keep all useful 0 pixels that are not NaN
        resultaat2 = resultaat1 * raster5            # masking step
        resultaat3 = resultaat2/(resultaat2>0)       # so that all values greater than 0.1 get NaN value
        resultaat4 = resultaat3 - 1                  # to restore the values back down by 1

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat4, 1)  # Schrijf het resultaat naar de eerste band


print("Forestry proportional allocation raster calculation successful")
print(f"     available at ...  {OUT_for_mij_path}")

print("end of 1.4. script")

print(f"end of {version} run")


