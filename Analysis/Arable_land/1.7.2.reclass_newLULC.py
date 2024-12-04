reclassLULCtoUrb = False
reclassLULCtoCrop = False
reclassLULCtoGrass = False
reclassLULCtoForest = False
reclassLULCtoBare = False
reclassLULCtoWater = False
countLULCreclassPixels = False
divideReclassLULCbyCount = False
applyFractiontoFinalMaps = True

# read path
count_reclass_filepath =  "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/countReclass.tif"

urban_reclass_filepath = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/urban_Reclass_new_LULC.tif"
crop_reclass_filepath = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/crop_Reclass_new_LULC.tif"
grass_reclass_filepath = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/grass_Reclass_new_LULC.tif"
forest_reclass_filepath = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/forest_Reclass_new_LULC.tif"
bare_reclass_filepath = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/bare_Reclass_new_LULC.tif"
water_reclass_filepath = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/water_Reclass_new_LULC.tif"

# final paths
urban_costs = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/CLUMondo/eu_regional_analysis/extended/mar24_POP_2020_rent_hectare_combined_clean__.tif"
grass_costs = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/rasterized_land_rents/mar24_grass_allocated_rents.tif"
crop_costs = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/rasterized_land_rents/feb24_crop_allocated_rents_TEST3__.tif"
forest_costs = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/rasterized_land_rents/mar24_master_run_1_for_allocated_rents.tif"

if reclassLULCtoUrb == True:
    # import rioxarray and shapley

    # read the lulc raster
    new_lulc_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif"

    import rasterio as rio
    import numpy as np

    with rio.open(new_lulc_path) as src:    
        # Read as numpy array
        array = src.read()
        profile = src.profile

        # Reclassify: NaN < 210, NaN >230, 230> 1 >210
        array[np.where(array < 209)] = np.nan 
        array[np.where(array == 210)] = 1
        array[np.where(array == 220)] = 1
        array[np.where(array == 230)] = 1
        array[np.where(array > 231)] = np.nan  
        # and so on ...  

    urban_reclass_filepath = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/urban_Reclass_new_LULC.tif"
    with rio.open(urban_reclass_filepath, 'w', **profile) as dst:
        # Write to disk
        dst.write(array)

if reclassLULCtoCrop == True:
    # import rioxarray and shapley

    # read the lulc raster
    new_lulc_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif"

    import rasterio as rio
    import numpy as np


    with rio.open(new_lulc_path) as src:    
        # Read as numpy array
        array = src.read()
        profile = src.profile

        # Reclassify: NaN < 210, NaN >230, 230> 1 >210
        array[np.where(array < 409)] = np.nan 
        array[np.where(array == 410)] = 1
        array[np.where(array == 510)] = 1
        array[np.where(array == 520)] = 1
        array[np.where(array == 530)] = 1
        array[np.where(array == 700)] = 1
        array[np.where(array == 420)] = np.nan
        array[np.where(array == 610)] = np.nan
        array[np.where(array == 620)] = np.nan
        array[np.where(array == 630)] = np.nan
        array[np.where(array > 701)] = np.nan  
        # and so on ...  

    crop_reclass_filepath = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/crop_Reclass_new_LULC.tif"
    with rio.open(crop_reclass_filepath, 'w', **profile) as dst:
        # Write to disk
        dst.write(array)

if reclassLULCtoGrass == True:
    # import rioxarray and shapley

    # read the lulc raster
    new_lulc_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif"

    import rasterio as rio
    import numpy as np


    with rio.open(new_lulc_path) as src:    
        # Read as numpy array
        array = src.read()
        profile = src.profile

        # Reclassify: NaN < 210, NaN >230, 230> 1 >210
        array[np.where(array < 250)] = np.nan 
        array[np.where(array == 300)] = 1
        array[np.where(array == 410)] = 1
        array[np.where(array == 420)] = 1
        array[np.where(array == 610)] = 1
        array[np.where(array == 620)] = 1
        array[np.where(array == 630)] = 1
        array[np.where(array == 510)] = np.nan
        array[np.where(array == 520)] = np.nan
        array[np.where(array == 530)] = np.nan 
        array[np.where(array > 631)] = np.nan  
        # and so on ...  

    grass_reclass_filepath = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/grass_Reclass_new_LULC.tif"
    with rio.open(grass_reclass_filepath, 'w', **profile) as dst:
        # Write to disk
        dst.write(array)

if reclassLULCtoForest == True:
    # import rioxarray and shapley

    # read the lulc raster
    new_lulc_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif"

    import rasterio as rio
    import numpy as np


    with rio.open(new_lulc_path) as src:    
        # Read as numpy array
        array = src.read()
        profile = src.profile

        # Reclassify: NaN < 210, NaN >230, 230> 1 >210
        array[np.where(array < 400)] = np.nan 
        array[np.where(array == 410)] = 1
        array[np.where(array == 420)] = 1
        array[np.where(array == 810)] = 1
        array[np.where(array == 820)] = 1
        array[np.where(array == 830)] = 1
        array[np.where(array == 840)] = 1
        array[np.where(array == 850)] = 1
        array[np.where(array == 510)] = np.nan
        array[np.where(array == 520)] = np.nan
        array[np.where(array == 530)] = np.nan
        array[np.where(array == 610)] = np.nan
        array[np.where(array == 620)] = np.nan
        array[np.where(array == 630)] = np.nan
        array[np.where(array == 700)] = np.nan 
 
        array[np.where(array > 631)] = np.nan  
        # and so on ...  

    forest_reclass_filepath = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/forest_Reclass_new_LULC.tif"
    with rio.open(forest_reclass_filepath, 'w', **profile) as dst:
        # Write to disk
        dst.write(array)

if reclassLULCtoBare == True:
    # import rioxarray and shapley

    # read the lulc raster
    new_lulc_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif"

    import rasterio as rio
    import numpy as np


    with rio.open(new_lulc_path) as src:    
        # Read as numpy array
        array = src.read()
        profile = src.profile

        # Reclassify: NaN < 210, NaN >230, 230> 1 >210
        array[np.where(array < 890)] = np.nan 
        array[np.where(array == 900)] = 1

        # and so on ...  

    bare_reclass_filepath = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/bare_Reclass_new_LULC.tif"
    with rio.open(bare_reclass_filepath, 'w', **profile) as dst:
        # Write to disk
        dst.write(array)

if reclassLULCtoWater == True:
    # import rioxarray and shapley

    # read the lulc raster
    new_lulc_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif"

    import rasterio as rio
    import numpy as np


    with rio.open(new_lulc_path) as src:    
        # Read as numpy array
        array = src.read()
        profile = src.profile

        # Reclassify: NaN < 210, NaN >230, 230> 1 >210
        array[np.where(array > 190)] = np.nan 
        array[np.where(array == 100)] = 1

        # and so on ...  

    water_reclass_filepath = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/water_Reclass_new_LULC.tif"
    with rio.open(water_reclass_filepath, 'w', **profile) as dst:
        # Write to disk
        dst.write(array)

if countLULCreclassPixels == True:
    # import rioxarray and shapley
    import rasterio
    import numpy as np

    with rasterio.open(urban_reclass_filepath) as srcUrb, rasterio.open(crop_reclass_filepath) as srcCrop, rasterio.open(grass_reclass_filepath) as srcGrass, rasterio.open(forest_reclass_filepath) as srcForest, rasterio.open(bare_reclass_filepath) as srcBare, rasterio.open(water_reclass_filepath) as srcWater:
        # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
        meta = srcUrb.meta.copy()

        # Werk metadata bij voor het uitvoerraster
        meta.update(driver='GTiff', dtype='float32')

        # Maak uitvoerrasterbestand aan
        out_path = count_reclass_filepath
        with rasterio.open(out_path, 'w', **meta) as dst:
            # Voer de vermenigvuldiging uit op de invoerrasters
            urb = srcUrb.read(1)  # Lees eerste band van raster1
            crop = srcCrop.read(1)
            grass = srcGrass.read(1)
            forest = srcForest.read(1)
            bare = srcBare.read(1)
            water = srcWater.read(1)

            # count = urb + crop + grass + forest + bare + water
            arrays = [urb, crop, grass, forest, bare, water]

            combined_array = np.stack(arrays)

            res = np.nansum(combined_array, axis = 0)

            dst.write(res, 1)  # Schrijf het resultaat naar de eerste band

    print(f"Uitvoerraster is succesvol geschreven. Hoort bij bestandspad {out_path}")

if divideReclassLULCbyCount == True:
    import rasterio
    from rasterio.plot import show
    import numpy as np

    # read files
    IN_count_reclass_filepath =  "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/countReclass.tif"
    IN_urban_reclass_filepath = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/urban_Reclass_new_LULC.tif"
    IN_crop_reclass_filepath = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/crop_Reclass_new_LULC.tif"
    IN_grass_reclass_filepath = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/grass_Reclass_new_LULC.tif"
    IN_forest_reclass_filepath = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/forest_Reclass_new_LULC.tif"
    IN_bare_reclass_filepath = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/bare_Reclass_new_LULC.tif"
    IN_water_reclass_filepath = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/water_Reclass_new_LULC.tif"

    OUT_divide_count_urb_reclass_filepath =  "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/urb_countReclass.tif"
    OUT_divide_count_crop_reclass_filepath =  "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/crop_countReclass.tif"
    OUT_divide_count_grass_reclass_filepath =  "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/grass_countReclass.tif"
    OUT_divide_count_forest_reclass_filepath =  "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/forest_countReclass.tif"
    OUT_divide_count_bare_reclass_filepath =  "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/bare_countReclass.tif"
    OUT_divide_count_water_reclass_filepath =  "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/water_countReclass.tif"

    raster1_pad = IN_urban_reclass_filepath
    raster2_pad = IN_count_reclass_filepath

    with rasterio.open(raster1_pad) as src1, rasterio.open(raster2_pad) as src2:
        # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
        meta = src1.meta.copy()

        # Werk metadata bij voor het uitvoerraster
        meta.update(driver='GTiff', dtype='float32')

        # Maak uitvoerrasterbestand aan
        uitvoer_pad = OUT_divide_count_urb_reclass_filepath
        with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
            # Voer de vermenigvuldiging uit op de invoerrasters
            raster1 = src1.read(1)  # Lees eerste band van raster1
            raster2 = src2.read(1)  # Lees eerste band van raster2
            resultaat = raster1 / raster2

            # Schrijf het resultaat naar het uitvoerrasterbestand
            dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band

    print("urban count division is succesvol geschreven.")

    raster1_pad = IN_crop_reclass_filepath
    raster2_pad = IN_count_reclass_filepath

    with rasterio.open(raster1_pad) as src1, rasterio.open(raster2_pad) as src2:
        # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
        meta = src1.meta.copy()

        # Werk metadata bij voor het uitvoerraster
        meta.update(driver='GTiff', dtype='float32')

        # Maak uitvoerrasterbestand aan
        uitvoer_pad = OUT_divide_count_crop_reclass_filepath
        with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
            # Voer de vermenigvuldiging uit op de invoerrasters
            raster1 = src1.read(1)  # Lees eerste band van raster1
            raster2 = src2.read(1)  # Lees eerste band van raster2
            resultaat = raster1 / raster2

            # Schrijf het resultaat naar het uitvoerrasterbestand
            dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band

    print("crop count division is succesvol geschreven.")

    raster1_pad = IN_grass_reclass_filepath
    raster2_pad = IN_count_reclass_filepath

    with rasterio.open(raster1_pad) as src1, rasterio.open(raster2_pad) as src2:
        # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
        meta = src1.meta.copy()

        # Werk metadata bij voor het uitvoerraster
        meta.update(driver='GTiff', dtype='float32')

        # Maak uitvoerrasterbestand aan
        uitvoer_pad = OUT_divide_count_grass_reclass_filepath
        with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
            # Voer de vermenigvuldiging uit op de invoerrasters
            raster1 = src1.read(1)  # Lees eerste band van raster1
            raster2 = src2.read(1)  # Lees eerste band van raster2
            resultaat = raster1 / raster2

            # Schrijf het resultaat naar het uitvoerrasterbestand
            dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band

    print("grass count division is succesvol geschreven.")

    raster1_pad = IN_forest_reclass_filepath
    raster2_pad = IN_count_reclass_filepath

    with rasterio.open(raster1_pad) as src1, rasterio.open(raster2_pad) as src2:
        # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
        meta = src1.meta.copy()

        # Werk metadata bij voor het uitvoerraster
        meta.update(driver='GTiff', dtype='float32')

        # Maak uitvoerrasterbestand aan
        uitvoer_pad = OUT_divide_count_forest_reclass_filepath
        with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
            # Voer de vermenigvuldiging uit op de invoerrasters
            raster1 = src1.read(1)  # Lees eerste band van raster1
            raster2 = src2.read(1)  # Lees eerste band van raster2
            resultaat = raster1 / raster2

            # Schrijf het resultaat naar het uitvoerrasterbestand
            dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band

    print("forest count division is succesvol geschreven.")

    raster1_pad = IN_bare_reclass_filepath
    raster2_pad = IN_count_reclass_filepath

    with rasterio.open(raster1_pad) as src1, rasterio.open(raster2_pad) as src2:
        # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
        meta = src1.meta.copy()

        # Werk metadata bij voor het uitvoerraster
        meta.update(driver='GTiff', dtype='float32')

        # Maak uitvoerrasterbestand aan
        uitvoer_pad = OUT_divide_count_bare_reclass_filepath
        with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
            # Voer de vermenigvuldiging uit op de invoerrasters
            raster1 = src1.read(1)  # Lees eerste band van raster1
            raster2 = src2.read(1)  # Lees eerste band van raster2
            resultaat = raster1 / raster2

            # Schrijf het resultaat naar het uitvoerrasterbestand
            dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band

    print("bare count division is succesvol geschreven.")

    raster1_pad = IN_water_reclass_filepath
    raster2_pad = IN_count_reclass_filepath

    with rasterio.open(raster1_pad) as src1, rasterio.open(raster2_pad) as src2:
        # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
        meta = src1.meta.copy()

        # Werk metadata bij voor het uitvoerraster
        meta.update(driver='GTiff', dtype='float32')

        # Maak uitvoerrasterbestand aan
        uitvoer_pad = OUT_divide_count_water_reclass_filepath
        with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
            # Voer de vermenigvuldiging uit op de invoerrasters
            raster1 = src1.read(1)  # Lees eerste band van raster1
            raster2 = src2.read(1)  # Lees eerste band van raster2
            resultaat = raster1 / raster2

            # Schrijf het resultaat naar het uitvoerrasterbestand
            dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band

    print("forest count division is succesvol geschreven.")

if applyFractiontoFinalMaps == True:

    IN_divide_count_crop_reclass_filepath =  "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/crop_countReclass.tif"
    IN_divide_count_grass_reclass_filepath =  "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/grass_countReclass.tif"
    IN_divide_count_forest_reclass_filepath =  "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/forest_countReclass.tif"


    # final paths
    urban_costs = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/CLUMondo/eu_regional_analysis/extended/mar24_POP_2020_rent_hectare_combined_clean__.tif"
    grass_costs = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/rasterized_land_rents/mar24_grass_allocated_rents.tif"
    crop_costs = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/rasterized_land_rents/feb24_crop_allocated_rents_TEST3__.tif"
    forest_costs = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/rasterized_land_rents/mar24_master_run_1_for_allocated_rents.tif"

    OUT_combination_raster = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/rasterized_land_rents/mar24_combined_allocated_rents.tif"
    OUT_combination_raster_wihtout_0 = 'c:\Users\spencerd\Documents\NaturaConnect\Spatial datasets\European countries\Input_datasets\hrl_combi_step\combined_new_LULC.tif' #clipped in QGIS
    raster1_pad = urban_costs
    raster2_pad = crop_costs
    raster3_pad = grass_costs
    raster4_pad = forest_costs

    raster5_pad = bare_reclass_filepath
    raster6_pad = water_reclass_filepath

    raster22_pad = IN_divide_count_crop_reclass_filepath
    raster33_pad = IN_divide_count_grass_reclass_filepath
    raster44_pad = IN_divide_count_forest_reclass_filepath

    with rasterio.open(raster1_pad) as src1, rasterio.open(raster2_pad) as src2, rasterio.open(raster3_pad) as src3, rasterio.open(raster4_pad) as src4, rasterio.open(raster5_pad) as src5, rasterio.open(raster6_pad) as src6, rasterio.open(raster22_pad) as src22,rasterio.open(raster33_pad) as src33,rasterio.open(raster44_pad) as src44:
        # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
        meta = src1.meta.copy()

        # Werk metadata bij voor het uitvoerraster
        meta.update(driver='GTiff', dtype='float32')

        # Maak uitvoerrasterbestand aan
        uitvoer_pad = OUT_combination_raster
        with rasterio.open(uitvoer_pad, 'w', **meta) as dst:

            # Voer de vermenigvuldiging uit op de invoerrasters
            urb = src1.read(1)  # Lees eerste band van raster1
            crop = src2.read(1)  # Lees eerste band van raster2
            grass = src3.read(1)  # Lees eerste band van raster2
            forest = src4.read(1)  # Lees eerste band van raster2
            bare = src5.read(1)  # Lees eerste band van raster2
            water = src6.read(1)  # Lees eerste band van raster2
            crop_reclass_fraction = src22.read(1)  # Lees eerste band van raster2
            forest_reclass_fraction = src44.read(1)  # Lees eerste band van raster2
            grass_reclass_fraction = src33.read(1)  # Lees eerste band van raster2

                
            crop_fraction = crop * crop_reclass_fraction
            forest_fraction = forest * forest_reclass_fraction
            grass_fraction = grass * grass_reclass_fraction
            bare0 = bare * 0 
            water0 = water * 0

            arrays = [urb, crop_fraction, grass_fraction, forest_fraction, bare0, water0]

            combined_array = np.stack(arrays)

            res = np.nansum(combined_array, axis = 0)


            # Schrijf het resultaat naar het uitvoerrasterbestand
            dst.write(res, 1)  # Schrijf het resultaat naar de eerste band

    print(f"combination raster is succesvol geschreven to {OUT_combination_raster}.")

