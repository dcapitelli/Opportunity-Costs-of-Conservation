

############################################################
## Times the averaged biomass value by reclass cropland   ##
############################################################


import rasterio
from rasterio.plot import show
import numpy as np
import matplotlib.pyplot as plt

reclass_cropland_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/crop_Reclass_new_LULC.tif"
average_biomass_value_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_aggregated_price_biomass_by_crop_price_count.tif" 
out_rast_average_biomass_value_crop_pixels_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_proportional_allocation_equation/feb24_crop_yij_allocation_gridded_cleaned_1.1.tif"

# Open invoerrasters
raster1_pad = reclass_cropland_path
raster2_pad = average_biomass_value_path
uitvoer_pad = out_rast_average_biomass_value_crop_pixels_path

with rasterio.open(raster1_pad) as src1, rasterio.open(raster2_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')

    # Maak uitvoerrasterbestand aan
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1, masked=True)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        # resultaat = raster1 * raster2
        resultaat0_5 = raster2 + 0.5  # so that all 0 values in raster 2 that are cropland pixels can be kept
        resultaat0_5_reclass = raster1 * resultaat0_5 # the masking step
        resultaatno_0_5 = resultaat0_5_reclass/(resultaat0_5_reclass > 0.1) # so that all values greater than 0.1 get NaN value
        resultaatno_0 = resultaatno_0_5 - 0.5  # to restore the values back down by 0.5      

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaatno_0, 1)  # Schrijf het resultaat naar de eerste band

print(f"Times the averaged biomass value by reclass cropland step successful. file available at {uitvoer_pad}")

