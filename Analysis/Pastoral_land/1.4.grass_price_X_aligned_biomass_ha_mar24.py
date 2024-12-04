import rasterio
from rasterio.plot import show
import numpy as np
import matplotlib.pyplot as plt

grass_name = 'catt'
in_grass_price_path = 'c:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/grass_biomass_eu/grass_prices/MAR24_eu_nuts0_livestock_price_cattle_val_euros_heads.tif'
# in_grass_price: no data = -99; Width	5582 Height	4474; Extent	944000,942000 : 6526000,5416000 ; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/grass_biomass_eu/aligned/mar24_prjsmp_clip_newLULC_/mar24_prjsmp_clip_newLULC_{grass_name}_heads_10km.tif" 

out_rast_calc_grass_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/grass_monetary_yield_eu/glw4_newLULC_{grass_name}_price_biomass_euro_heads_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_grass_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_grass_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        # 10km2 is 1000 hectares therefore divide raster1 by a factor of 1000
        resultaat = (raster1/1000) * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{grass_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

grass_name = 'goat'

in_grass_price_path = f"c:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/grass_biomass_eu/grass_prices/MAR24_eu_nuts0_livestock_price_goat_value_euros_heads.tif" 
# in_grass_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/grass_biomass_eu/aligned/mar24_prjsmp_clip_newLULC_/mar24_prjsmp_clip_newLULC_{grass_name}_heads_10km.tif" 

out_rast_calc_grass_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/grass_monetary_yield_eu/glw4_newLULC_{grass_name}_price_biomass_euro_heads_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_grass_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_grass_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        # 10km2 is 1000 hectares therefore divide raster1 by a factor of 1000
        resultaat = (raster1/1000) * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{grass_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

grass_name = 'shee'

in_grass_price_path = "c:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/grass_biomass_eu/grass_prices/MAR24_eu_nuts0_livestock_price_sheep_valu_euros_heads.tif" 
# in_grass_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/grass_biomass_eu/aligned/mar24_prjsmp_clip_newLULC_/mar24_prjsmp_clip_newLULC_{grass_name}_heads_10km.tif" 

out_rast_calc_grass_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/grass_monetary_yield_eu/glw4_newLULC_{grass_name}_price_biomass_euro_heads_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_grass_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_grass_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        # 10km2 is 1000 hectares therefore divide raster1 by a factor of 1000
        resultaat = (raster1/1000) * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{grass_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

##############################
## end of repeatable section ##
##############################

print("#~~~~~~~~~~End~of~script~~~~~~~~~~#")

#~~~~~~~~~~End~of~script~~~~~~~~~~#