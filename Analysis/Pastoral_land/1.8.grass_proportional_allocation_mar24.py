"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/grass_proportional_allocation_equation/mar24_zonalstat_grass_yj_mean.tif"

############################################################
## Perform proportional allocation calculation            ##
############################################################

mar24_Run = False
jun24_MAE_Run = True # checking that the implementation was done correctly 
                        #and saw that the end calculations were different to how the crop calculations 
                        #were done, so I decided to run a separate option taking the calculations from
                        #the crop proportional allocation file.

import rasterio
from rasterio.plot import show
import numpy as np
import matplotlib.pyplot as plt

# hard coded inputs: binary_yij_mask

# load paths
# current paths
grass_mj_rents_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/rasterized_land_rents/grass_mj_rents_feb_24.tif"
grass_yj_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/grass_proportional_allocation_equation/mar24_zonalstat_grass_yj_mean.tif"
grass_yij_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/grass_proportional_allocation_equation/grass_newLULC__yij_allocation_gridded.tif"
reclass_grassland_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/grass_Reclass_new_LULC.tif"
binary_yij_mask = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/reference_layers/mar24_grass_yield_binary_mask.tif"

out_rast_grass_allocated_rents_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/rasterized_land_rents/mar24_grass_allocated_rents.tif"
out_rast_grass_allocated_rents_path_MAE_check = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/rasterized_land_rents/jun24_MAE_grass_allocated_rents.tif"
# allocate paths
raster_1_path = grass_mj_rents_path
raster_2_path = grass_yj_path
raster_3_path = grass_yij_path
raster_4_path = reclass_grassland_path
raster_5_path = binary_yij_mask

if mar24_Run == True:

    with rasterio.open(raster_1_path) as src1, rasterio.open(raster_2_path) as src2, rasterio.open(raster_3_path) as src3, rasterio.open(raster_4_path) as src4, rasterio.open(raster_5_path) as src5:
        # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
        meta = src1.meta.copy()

        # Werk metadata bij voor het uitvoerraster
        meta.update(driver='GTiff', dtype='float32')

        # Maak uitvoerrasterbestand aan
        uitvoer_pad = out_rast_grass_allocated_rents_path
        with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
            # Voer de vermenigvuldiging uit op de invoerrasters
            raster1 = src1.read(1)  # Lees eerste band van raster1
            raster2 = src2.read(1)  # Lees eerste band van raster2
            raster3 = src3.read(1)  # Lees eerste band van raster2
            raster4 = src4.read(1)  # Lees eerste band van raster2
            raster5 = src5.read(1)  # Lees eerste band van raster2


            resultaat = (raster1/raster2) * raster3
            resultaat1 = resultaat + 1
            resultaat2 = resultaat1 * raster4
            resultaat3 = resultaat2 - 1
            resultaat4 = resultaat3/(resultaat3>0)
            resultaat5 = resultaat4 * (resultaat4>0)
            resultaat6 = resultaat5 * raster5
            resultaat7 = resultaat6 * (resultaat6>0)
            # Schrijf het resultaat naar het uitvoerrasterbestand
            dst.write(resultaat7, 1)  # Schrijf het resultaat naar de eerste band




    print("grass proportional allocation raster calculation successful")
    print(f"     available at ...  {uitvoer_pad}")


if jun24_MAE_Run == True:
    with rasterio.open(raster_1_path) as src1, rasterio.open(raster_2_path) as src2, rasterio.open(raster_3_path) as src3, rasterio.open(raster_4_path) as src4, rasterio.open(raster_5_path) as src5:
        # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
        meta = src1.meta.copy()

        # Werk metadata bij voor het uitvoerraster
        meta.update(driver='GTiff', dtype='float32')

        # Maak uitvoerrasterbestand aan
        uitvoer_pad = out_rast_grass_allocated_rents_path_MAE_check
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

            # resultaat5 = resultaat4 * (resultaat4>0)
            # resultaat6 = resultaat5 * raster5
            # resultaat7 = resultaat6 * (resultaat6>0)

            # Schrijf het resultaat naar het uitvoerrasterbestand
            dst.write(resultaat4, 1)  # Schrijf het resultaat naar de eerste band


    print("grass proportional allocation raster calculation successful")
    print(f"     available at ...  {uitvoer_pad}")