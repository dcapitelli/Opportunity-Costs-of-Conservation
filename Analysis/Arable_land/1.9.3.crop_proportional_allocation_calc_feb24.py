############################################################
## Perform proportional allocation calculation            ##
############################################################

import rasterio as rio
from rasterio.plot import show
import numpy as np
import matplotlib.pyplot as plt

# hard coded inputs: binary_yij_mask

# load paths

# 1) check the number of non nan cells in each region for each input raster (and do for nan)
# 2) border / area vs mae


# current paths
crop_mj_rents_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/rasterized_land_rents/crop_mj_rents_feb_24.tif"
crop_yj_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_proportional_allocation_equation/feb24_zonalstat_crop_yj_mean.tif"
crop_yij_path = r"c:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_proportional_allocation_equation/feb24_crop_yij_allocation_gridded_cleaned_1.1.tif" 
reclass_cropland_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/crop_Reclass_new_LULC.tif"
binary_yij_mask = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/reference_layers/feb24_crop_yield_binary_mask.tif"

out_rast_crop_allocated_rents_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/rasterized_land_rents/feb24_crop_allocated_rents_TEST3__.tif"

# allocate paths
raster_1_path = crop_mj_rents_path
raster_2_path = crop_yj_path
raster_3_path = crop_yij_path
raster_4_path = reclass_cropland_path
raster_5_path = binary_yij_mask

with rio.open(raster_1_path) as src1, rio.open(raster_2_path) as src2, rio.open(raster_3_path) as src3, rio.open(raster_4_path) as src4, rio.open(raster_5_path) as src5:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_crop_allocated_rents_path
    with rio.open(uitvoer_pad, 'w', **meta) as dst:
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

        # resultaat5 = resultaat4 * (resultaat4>0)
        # resultaat6 = resultaat5 * raster5
        # resultaat7 = resultaat6 * (resultaat6>0)

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat4, 1)  # Schrijf het resultaat naar de eerste band


print("Crop proportional allocation raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")


# # Has something gone wrong? have a look at the meta data hereunder
# crop_mj_rents = rio.open(crop_mj_rents_path)
# crop_mj_rents.shape

# crop_yj = rio.open(crop_yj_path)
# crop_yj.shape

# crop_yij = rio.open(crop_yij_path)
# crop_yij.shape

# reclass_cropland = rio.open(reclass_cropland_path)
# reclass_cropland.shape

# binary_yij = rio.open(binary_yij_mask)
# binary_yij.shape
