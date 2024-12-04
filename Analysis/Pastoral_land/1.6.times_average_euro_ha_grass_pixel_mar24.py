
############################################################
## Times the averaged biomass value by reclass cropland   ##
############################################################


import rasterio
from rasterio.plot import show
import numpy as np
import matplotlib.pyplot as plt

reclass_grassland_path = r"c:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/grass_Reclass_new_LULC.tif"
average_biomass_value_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/grass_monetary_yield_eu/glw4_newLULC_averaged_price_biomass_by_livestock_price_count.tif"

out_rast_average_biomass_value_grass_pixels_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/grass_proportional_allocation_equation/grass_newLULC__yij_allocation_gridded.tif"

# Open invoerrasters
raster1_pad = reclass_grassland_path
raster2_pad = average_biomass_value_path
uitvoer_pad = out_rast_average_biomass_value_grass_pixels_path

with rasterio.open(raster1_pad) as src1, rasterio.open(raster2_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')

    # Maak uitvoerrasterbestand aan
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        # resultaat1 = raster1 * raster2
        resultaat0_5 = raster2 + 0.5  # so that all 0 values in raster 2 that are cropland pixels can be kept
        resultaat0_5_reclass = raster1 * resultaat0_5
        resultaatno_0_5 = resultaat0_5_reclass/(resultaat0_5_reclass > 0)
        resultaatno_0 = resultaatno_0_5 - 0.5        

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaatno_0, 1)  # Schrijf het resultaat naar de eerste band
        

        # # Schrijf het resultaat naar het uitvoerrasterbestand
        # dst.write(resultaat1, 1)  # Schrijf het resultaat naar de eerste band

print(f"Times the averaged biomass value by reclass grassland step successful. file available at {uitvoer_pad}")
