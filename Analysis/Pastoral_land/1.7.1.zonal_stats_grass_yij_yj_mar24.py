import rasterstats
import rasterio
from rasterio import features
from rasterio.enums import MergeAlg
from rasterio.plot import show
import pandas 
import geopandas as gpd
import numpy as np
from numpy import int16


# read in the reference vector
eu_nuts0 = gpd.read_file("C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/NUTS_regions_missing_countries/reference_vector_feb_24/reference_vector_mar_24_cleaned.shp")
eu_nuts0.columns

# read in the grass yield raster
raster_path_1 = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/grass_proportional_allocation_equation/mar24_grass_yield_reclass_no_inf.tif"
raster_path_2 = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/grass_Reclass_new_LULC.tif"
output_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/grass_proportional_allocation_equation/mar24_zonalstat_grass_yj_mean.tif"

eu_nuts0.head(20)
eu_nuts0 = eu_nuts0.sort_values('sum_grass_yield_values')
eu_nuts0.tail(30)



# Implementation of lesson into NaturaConnect code
d = rasterstats.zonal_stats(eu_nuts0.geometry, raster_path_1, stats=['sum'])
values = [i['sum'] for i in d]
eu_nuts0['sum_grass_yield_values'] = values

d= rasterstats.zonal_stats(eu_nuts0.geometry, raster_path_1, stats=['count'])
values = [i['count'] for i in d]
eu_nuts0['count_grass_yield_cells'] = values

d = rasterstats.zonal_stats(eu_nuts0.geometry, raster_path_2, stats=['sum'])
values = [i['sum'] for i in d]
eu_nuts0['sum_reclulc_values'] = values

d= rasterstats.zonal_stats(eu_nuts0.geometry, raster_path_2, stats=['count'])
values = [i['count'] for i in d]
eu_nuts0['count_reclulc_cells'] = values

"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/grass_proportional_allocation_equation/mar24_zonalstat_grass_yj_mean.tif"
# 'sum_grass_cells' should equal 'sum_reclulc_grass'
eu_nuts0['check_cell'] = eu_nuts0['count_reclulc_cells'] - eu_nuts0['count_grass_yield_cells']

print("printed value should be < 0:")
print(eu_nuts0['check_cell'].sum())
print("if value > 0, it means that the GLW4 map contains NaN pixels where the LULC defines pixels as grassland")

eu_nuts0['mean_grass_yield'] = eu_nuts0['sum_grass_yield_values'] / eu_nuts0['count_grass_yield_cells']

# to get rid of the NaN values from the ['mean_grass_yield']
vector_new = eu_nuts0.loc[~((eu_nuts0['CNTR_COD_1']=='HR') & (eu_nuts0['mean_grass_yield'].isna()))] 
print(vector_new[vector_new['CNTR_COD_1']=='HR'])
vector_new = vector_new.loc[~((vector_new['CNTR_COD_1']=='ME') & (vector_new['mean_grass_yield'].isna()))] 
print(vector_new[vector_new['CNTR_COD_1']=='ME'])
vector_new = vector_new.loc[~((vector_new['CNTR_COD_1']=='RS') & (vector_new['mean_grass_yield'].isna()))] 
print(vector_new[vector_new['CNTR_COD_1']=='RS'])


print(eu_nuts0.iloc[:,-6:]) # view the last six columns of the dataframe

print("vector zonal analysis complete")

########################################
## Rasterise the mean from the vector ##
########################################

vector = vector_new
out_rast_grass_yj_path = output_path

burn_name = "mean_grass_yield"
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
        out_rast_grass_yj_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(" rasterisation complete")

print("grass yj zonal statistics successful")

print(f" grass yj raster available at:  {out_rast_grass_yj_path}")