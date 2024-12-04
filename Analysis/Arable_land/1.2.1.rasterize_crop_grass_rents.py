#Rasterize nuts2 crop rents m,j

import geopandas as gpd
import matplotlib.pyplot as plt
import rasterio
from rasterio import features
from rasterio.enums import MergeAlg
from rasterio.plot import show
from numpy import int16


cropRentRasterisation = False
grassRentRasterisation = True

############################################################
## Perform cropland land rent rasterisation               ##
############################################################

# specify paths
# pre feb24: nuts2_crop_rent_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/eu_nuts2_agr_rents_BH_AL_RS_MK_XK_PT__.shp"
nuts2_crop_rent_path = 'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/NUTS_regions_missing_countries/Union_EU_marco_microstates_cleaned_NUTS.shp'
nuts2_crop_rent_path_feb = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Agricultural_land_rents/updated_list_agr_land_rent_feb24/arable_pastoral_rents_sanitized_stitched_BH_AL_RS_MK_ME_XK_CY_PT_CH_feb_24_final.shp"
test = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Agricultural_land_rents/updated_list_agr_land_rent_feb24/arable_pastoral_rents_sanitized_stitched_BH_AL_RS_MK_ME_XK_CY_PT_CH_feb_24__final.shp"

# pre feb24: out_rast_crop_mj_rents_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/rasterized_land_rents/crop_mj_rents_SOD_update_1.1.tif"
out_rast_crop_mj_rents_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/rasterized_land_rents/crop_mj_rents_feb_24.tif"

# pre feb24: out_rast_grass_mj_rents_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/rasterized_land_rents/grass_mj_rents_SOD_update_1.1.tif"
out_rast_grass_mj_rents_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/rasterized_land_rents/grass_mj_rents_feb_24.tif"

land_use_map_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/eu_lum_map_2_nov_clip.tif"


# Read in vector
vector = gpd.read_file(nuts2_crop_rent_path)

if cropRentRasterisation == True:
    # assign column to burn
    burn_name = "ARNE21_HA"
    burn_value = vector[burn_name]


    # Get list of geometries for all features in vector file
    geom = [shapes for shapes in vector.geometry]


    # Open example raster
    raster = rasterio.open(land_use_map_path)


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
            out_rast_crop_mj_rents_path, "w",
            driver = "GTiff",
            crs = raster.crs,
            transform = raster.transform,
            dtype = rasterio.float32,
            count = 1,
            width = raster.width,
            height = raster.height) as dst:
        dst.write(rasterized, indexes = 1)

    print("crop rent rasterisation successful")

    print(f"crop rent raster available at:  {out_rast_crop_mj_rents_path}")


############################################################
## Perform grassland land rent rasterisation              ##
############################################################

if grassRentRasterisation == True:

    # assign column to burn
    burn_name = "PRNE21_HA"
    burn_value = vector[burn_name]


    # Get list of geometries for all features in vector file
    geom = [shapes for shapes in vector.geometry]


    # Open example raster
    raster = rasterio.open(land_use_map_path)


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
            out_rast_grass_mj_rents_path, "w",
            driver = "GTiff",
            crs = raster.crs,
            transform = raster.transform,
            dtype = rasterio.float32,
            count = 1,
            width = raster.width,
            height = raster.height) as dst:
        dst.write(rasterized, indexes = 1)

    print("grass rent rasterisation successful")

    print(f"grass rent raster available at:  {out_rast_grass_mj_rents_path}")

print("#~~~~~~~~~~End~of~script~~~~~~~~~~#")