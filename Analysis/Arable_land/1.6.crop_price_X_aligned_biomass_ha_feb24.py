import rasterio
from rasterio.plot import show
import numpy as np
import matplotlib.pyplot as plt

crop_name = 'whea'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -999; no data inside eu = 0; height, width (4474,5582); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe
#{'driver': 'GTiff', 'dtype': 'float64', 'nodata': -999.0, 'width': 5582, 'height': 4474, 'count': 1, 'crs': CRS.from_epsg(3035), 'transform': Affine(1000.0, 0.0, 944000.0,
#       0.0, -1000.0, 5416000.0)}
# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32') #, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'rice'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'maiz'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'barl'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'pmil'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'smil'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'sorg'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'ocer'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'pota'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'swpo'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'yams'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'bean'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'chic'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'cowp'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'pige'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'lent'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'opul'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'soyb'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'grou'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'cnut'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'oilp'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'sunf'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'rape'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'sesa'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

# rasterio._err.CPLE_AppDefinedError: 
# C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_ooil_price_biomass_euro_kg_ha.tif
# : TIFFReadDirectory:Failed to read directory at offset 8
# solution: deleted the files that the script made and then tried again

crop_name = 'ooil'
crop_price = f'{crop_name}_price'
# crop_label = f'_{crop_name}_'
in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -999; no data inside eu = 0; height, width (4474,5582); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe
#{'driver': 'GTiff', 'dtype': 'float64', 'nodata': -999.0, 'width': 5582, 'height': 4474, 'count': 1, 'crs': CRS.from_epsg(3035), 'transform': Affine(1000.0, 0.0, 944000.0,
#       0.0, -1000.0, 5416000.0)}
# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32') #, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")
########################
## repeatable section ##
########################

crop_name = 'sugc'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'sugb'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'cott'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'ofib'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'toba'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'bana'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'trof'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'temf'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'vege'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")

########################
## repeatable section ##
########################

crop_name = 'rest'
crop_price = f'{crop_name}_price'

in_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{crop_price}_eur2021kg_feb24_update_1.1.tif'# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe 
# in_crop_price: no data = -99; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

in_aligned_biomass_ha_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_biomass_yield/aligned/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_clip_{crop_name}_kg_ha.tif" 

out_rast_calc_crop_price_times_biomass_ha = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_{crop_name}_price_biomass_euro_kg_ha.tif"
# desired metadata: no data outside eu = -99; no data inside eu = 0; height, width (4516,6500); extent 900000,900000 : 7400000,5416000; pixel size 1000 -1000; crs EPSG:3035 - ETRS89-extended / LAEA Europe

# Open invoerrasters
biomass_pad = in_aligned_biomass_ha_path
price_pad =  in_crop_price_path

with rasterio.open(biomass_pad) as src1, rasterio.open(price_pad) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')#, nodata = -999)

    # Maak uitvoerrasterbestand aan
    uitvoer_pad = out_rast_calc_crop_price_times_biomass_ha
    with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)  # Lees eerste band van raster1
        raster2 = src2.read(1)  # Lees eerste band van raster2
        resultaat = raster1 * raster2

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band


print(f"{crop_name} raster calculation successful")
print(f"     available at ...  {uitvoer_pad}")



###############################
## end of repeatable section ##
###############################

print("#~~~~~~~~~~End~of~script~~~~~~~~~~#")

#~~~~~~~~~~End~of~script~~~~~~~~~~#