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
eu_nuts0 = gpd.read_file("C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/NUTS_regions_missing_countries/reference_vector_feb_24/reference_vector_feb_24.shp")
eu_nuts0.columns

# read in the crop yield raster
raster_path_1 = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_proportional_allocation_equation/feb24_crop_yij_allocation_gridded_cleaned_1.1.tif"
raster_path_2 = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/crop_Reclass_new_LULC.tif"
output_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_proportional_allocation_equation/feb24_zonalstat_crop_yj_mean.tif"


# Implementation of lesson into NaturaConnect code
d = rasterstats.zonal_stats(eu_nuts0.geometry, raster_path_1, stats=['sum'])
values = [i['sum'] for i in d]
eu_nuts0['sum_crop_yield_values'] = values

d= rasterstats.zonal_stats(eu_nuts0.geometry, raster_path_1, stats=['count'])
values = [i['count'] for i in d]
eu_nuts0['count_crop_yield_cells'] = values

d = rasterstats.zonal_stats(eu_nuts0.geometry, raster_path_2, stats=['sum'])
values = [i['sum'] for i in d]
eu_nuts0['sum_reclulc_values'] = values

d= rasterstats.zonal_stats(eu_nuts0.geometry, raster_path_2, stats=['count'])
values = [i['count'] for i in d]
eu_nuts0['count_reclulc_cells'] = values


# 'sum_crop_cells' should equal 'sum_reclulc_crop'
eu_nuts0['check_cell'] = eu_nuts0['count_reclulc_cells'] - eu_nuts0['count_crop_yield_cells']

print("printed value should be < 0:")
print(eu_nuts0['check_cell'].sum())
print("if value > 0, it means that the MapSPAM map contains NaN pixels where the LULC defines pixels as cropland")

eu_nuts0['mean_crop_yield'] = eu_nuts0['sum_crop_yield_values'] / eu_nuts0['count_crop_yield_cells']

print(eu_nuts0.iloc[:,-6:]) # view the last six columns of the dataframe

print("vector zonal analysis complete")

########################################
## Rasterise the mean from the vector ##
########################################

vector = eu_nuts0
out_rast_crop_yj_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_proportional_allocation_equation/feb24_zonalstat_crop_yj_mean.tif"

burn_name = "mean_crop_yield"
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
        out_rast_crop_yj_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(" rasterisation complete")

print("crop yj zonal statistics successful")

print(f" crop yj raster available at:  {out_rast_crop_yj_path}")