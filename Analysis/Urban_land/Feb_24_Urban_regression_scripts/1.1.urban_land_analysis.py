

import geopandas as gpd
import pandas as pd
import rioxarray as riox
import rasterio
from shapely.geometry import Polygon
import numpy as np

version = 'mar24_'

# paths
project_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries"
urban_path = 'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents'

IN_master_vector_path = project_path + "/NUTS_regions_missing_countries/reference_vector_feb_24/reference_vector_mar_24_cleaned.shp"
IN_population_hectare = urban_path + "/CLUMondo/convert_km_to_hectare/Pop_2020__hectare__.tif"


# switches:
assignEUtoRegions = False#True
reclassLULCtoUrb = False
clipUrbReclassEUregions = False
clipPopDensityEUregions =  False#True
imputeRegressionEUregions =  False#True
imputeRegressionEUwide = False
combineRegions =True#False # trying....

if assignEUtoRegions == True:
    # read country shapefiles
    master_vector = gpd.read_file(IN_master_vector_path)
    master_vector = master_vector.rename(columns={'CNTR_COD_1':'CNTR_ID'})

    # use the region list of countries to subset the shapefile
    south_eu = ["IT", "ES", "EL","MT","CY","PT","AN"]
    south_data = pd.DataFrame(south_eu, columns=['CNTR_ID'])
    south_eu_gdf = master_vector.merge(south_data, on="CNTR_ID")

    west_eu = ["BE","LU","FR", "NL", "UK", "IE","DE","CH","AT","LI"]
    west_data = pd.DataFrame(west_eu, columns=['CNTR_ID'])
    west_eu_gdf = master_vector.merge(west_data, on="CNTR_ID")

    north_eu = ["FI", "DK","SE","NO"]
    north_data = pd.DataFrame(north_eu, columns=['CNTR_ID'])
    north_eu_gdf = master_vector.merge(north_data, on="CNTR_ID")

    east_eu = ["LV","EE","LT","HU","SK", "BG", "RO","CZ","PL","SI", "AL","BH","HR","XK","ME","MK","RS"]
    east_data = pd.DataFrame(east_eu, columns=['CNTR_ID'])
    east_eu_gdf = master_vector.merge(east_data, on="CNTR_ID")
    east_eu_gdf['CNTR_ID'].unique()

    # create file path
    north_region = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/reference_files/{version}north_region.shp"
    south_region = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/reference_files/{version}south_region.shp"
    west_region = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/reference_files/{version}west_region.shp"
    east_region = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/reference_files/{version}east_region.shp"

    # write file to file path
    north_eu_gdf.to_file(north_region)
    south_eu_gdf.to_file(south_region)
    west_eu_gdf.to_file(west_region)
    east_eu_gdf.to_file(east_region)

    print("EU region shapefiles successfully divided into north, west, east, and south")
    print(f"south region available at {south_region}")
    print(f"east region available at {east_region}")
    print(f"west region available at {west_region}")
    print(f"north region available at {north_region}")

########################
# reclass the lulc map #
########################

if reclassLULCtoUrb == True:
    # import rioxarray and shapley

    # read the lulc raster
    new_lulc_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/eu_lum_map_2_nov_clip.tif"

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

#####################
# clip the lulc map #
#####################

if clipUrbReclassEUregions == True:
    # Read raster using rioxarray
    urb_Reclass = riox.open_rasterio(urban_reclass_filepath)
    
    # Use shapely polygon in clip method of rioxarray object to clip raster
    clipped_east_urb_Reclass = urb_Reclass.rio.clip(east_eu_gdf["geometry"])
    clipped_north_urb_Reclass = urb_Reclass.rio.clip(north_eu_gdf["geometry"])
    clipped_west_urb_Reclass = urb_Reclass.rio.clip(west_eu_gdf["geometry"])
    clipped_south_urb_Reclass = urb_Reclass.rio.clip(south_eu_gdf["geometry"])
    
    # Save clipped raster
    east_clipped_filepath = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/{version}east_eu_clip_urb_Reclass.tif"
    clipped_east_urb_Reclass.rio.to_raster(east_clipped_filepath)

    north_clipped_filepath = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/{version}north_eu_clip_urb_Reclass.tif"
    clipped_north_urb_Reclass.rio.to_raster(north_clipped_filepath)

    west_clipped_filepath = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/{version}west_eu_clip_urb_Reclass.tif"
    clipped_west_urb_Reclass.rio.to_raster(west_clipped_filepath)

    south_clipped_filepath = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/{version}south_eu_clip_urb_Reclass.tif"
    clipped_south_urb_Reclass.rio.to_raster(south_clipped_filepath)

# using population density at 1km estimates from Pop: https://www.nature.com/articles/s41597-022-01675-x#Sec9
# C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/Pop.zip

###############################################
## Clip pop density raster to the EU regions ##
###############################################

if clipPopDensityEUregions == True:
    # this population density raster has already been converted into per hectare units
    population_density_path =  IN_population_hectare

    # Read raster using rioxarray
    population_density_Raster = riox.open_rasterio(population_density_path)

    # read country shapefiles
    master_vector = gpd.read_file(IN_master_vector_path)
    master_vector = master_vector.rename(columns={'CNTR_COD_1':'CNTR_ID'})

    # use the region list of countries to subset the shapefile
    south_eu = ["IT", "ES", "EL","MT","CY","PT","AN"]
    south_data = pd.DataFrame(south_eu, columns=['CNTR_ID'])
    south_eu_gdf = master_vector.merge(south_data, on="CNTR_ID")

    west_eu = ["BE","LU","FR", "NL", "UK", "IE","DE","CH","AT","LI"]
    west_data = pd.DataFrame(west_eu, columns=['CNTR_ID'])
    west_eu_gdf = master_vector.merge(west_data, on="CNTR_ID")

    north_eu = ["FI", "DK","SE","NO"]
    north_data = pd.DataFrame(north_eu, columns=['CNTR_ID'])
    north_eu_gdf = master_vector.merge(north_data, on="CNTR_ID")

    east_eu = ["LV","EE","LT","HU","SK", "BG", "RO","CZ","PL","SI", "AL","BH","HR","XK","ME","MK","RS"]
    east_data = pd.DataFrame(east_eu, columns=['CNTR_ID'])
    east_eu_gdf = master_vector.merge(east_data, on="CNTR_ID")

    # Use shapely polygon in clip method of rioxarray object to clip raster
    east_population_density_Raster = population_density_Raster.rio.clip(east_eu_gdf["geometry"])
    north_population_density_Raster = population_density_Raster.rio.clip(north_eu_gdf["geometry"])
    west_population_density_Raster = population_density_Raster.rio.clip(west_eu_gdf["geometry"])
    south_population_density_Raster = population_density_Raster.rio.clip(south_eu_gdf["geometry"])

    # Save clipped raster
    east_clipped_filepath = urban_path + f"/CLUMondo/eu_regional_analysis/{version}east_Pop_2020_population_hectare.tif"
    east_population_density_Raster.rio.to_raster(east_clipped_filepath)

    north_clipped_filepath = urban_path + f"/CLUMondo/eu_regional_analysis/{version}north_Pop_2020_population_hectare.tif"
    north_population_density_Raster.rio.to_raster(north_clipped_filepath)

    west_clipped_filepath = urban_path + f"/CLUMondo/eu_regional_analysis/{version}west_Pop_2020_population_hectare.tif"
    west_population_density_Raster.rio.to_raster(west_clipped_filepath)

    south_clipped_filepath = urban_path + f"/CLUMondo/eu_regional_analysis/{version}south_Pop_2020_population_hectare.tif"
    south_population_density_Raster.rio.to_raster(south_clipped_filepath)

##########################################################################
## Impute the result of each regression and filter using urb land class ##
##########################################################################

if imputeRegressionEUregions == True:
    ''' Using the selected model relating population density and residential rent:
        LogRent = 1.05LogPop + 8.33 + 0.77(North) + 0.26(South) + 0.62(West) [East intercept is 8.33]

        Split into regional values:
        LogRent = 1.05LogPop + 8.33  

        Since ln(y) = A*ln(x) + B 
            rearranged for y is:
            y = e^(ln(e^B * x^A))

    '''
    modelDict = {"East": "LogRent = 1.05LogPop + 8.33318",
                 "North": "LogRent = 1.05LogPop + 9.11129",
                 "South": "LogRent = 1.05LogPop + 8.59005",
                 "West": "LogRent = 1.05LogPop + 8.95072",
                 "reEast": "Rent = exp( ln( exp(8.33318) * Population(1.05) ) )",
                 "reNorth": "Rent = exp( ln( exp(9.11129) * Population(1.05) ) )",
                 "reSouth": "Rent = exp( ln( exp(8.59005) * Population(1.05) ) )",
                 "reWest": "Rent = exp( ln( exp(8.95072) * Population(1.05) ) )"}
    print('made reference dictionary')
    east_pop_filepath = east_clipped_filepath = urban_path + f"/CLUMondo/eu_regional_analysis/{version}east_Pop_2020_population_hectare.tif"
    north_pop_filepath = north_clipped_filepath = urban_path + f"/CLUMondo/eu_regional_analysis/{version}north_Pop_2020_population_hectare.tif"
    west_pop_filepath = west_clipped_filepath = urban_path + f"/CLUMondo/eu_regional_analysis/{version}west_Pop_2020_population_hectare.tif"
    south_pop_filepath = south_clipped_filepath = urban_path + f"/CLUMondo/eu_regional_analysis/{version}south_Pop_2020_population_hectare.tif"
    print('read population file paths')

    east_urb_filepath = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/east_eu_clip_urb_Reclass.tif"
    north_urb_filepath = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/north_eu_clip_urb_Reclass.tif"
    west_urb_filepath = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/west_eu_clip_urb_Reclass.tif"
    south_urb_filepath = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/south_eu_clip_urb_Reclass.tif"
    print('read urban land filter map file paths')

    OUT_east_regression_path = urban_path + f"/CLUMondo/eu_regional_analysis/{version}east_Pop_2020_rent_hectare_regression.tif"
    OUT_east_filtered_path = urban_path + f"/CLUMondo/eu_regional_analysis/{version}east_Pop_2020_rent_hectare_regression_filtered.tif"
    
    OUT_west_regression_path = urban_path + f"/CLUMondo/eu_regional_analysis/{version}west_Pop_2020_rent_hectare_regression.tif"
    OUT_west_filtered_path = urban_path + f"/CLUMondo/eu_regional_analysis/{version}west_Pop_2020_rent_hectare_regression_filtered.tif"
    
    OUT_north_regression_path = urban_path + f"/CLUMondo/eu_regional_analysis/{version}north_Pop_2020_rent_hectare_regression.tif"
    OUT_north_filtered_path = urban_path + f"/CLUMondo/eu_regional_analysis/{version}north_Pop_2020_rent_hectare_regression_filtered.tif"
    
    OUT_south_regression_path = urban_path + f"/CLUMondo/eu_regional_analysis/{version}south_Pop_2020_rent_hectare_regression.tif"
    OUT_south_filtered_path = urban_path + f"/CLUMondo/eu_regional_analysis/{version}south_Pop_2020_rent_hectare_regression_filtered.tif"

    from numpy import exp
    from numpy import log as ln
    from numpy import float_power as fp
    print('imported numpy functions: exp, log as ln, and float_power as fp')

    region = "east"

    with rasterio.open(east_pop_filepath) as src1:#, rasterio.open(east_urb_filepath) as src2: 
        # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
        meta = src1.meta.copy()

        # Werk metadata bij voor het uitvoerraster
        meta.update(driver='GTiff', dtype='float32')

        # Maak uitvoerrasterbestand aan
        uitvoer_pad = OUT_east_regression_path
        with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
            # Voer de vermenigvuldiging uit op de invoerrasters
            east_population = src1.read(1)  # Lees eerste band van raster1

            # East: Rent = exp( ln( exp(8.33318) * population(1.05) ) )
            east_rent = exp( ln( exp(8.33318) * fp(east_population, 1.05) ) )

            # resultaat[resultaat> -255] = np.nan # after inspecting the raster it seems values with 255 are Nan values 
            # Schrijf het resultaat naar het uitvoerrasterbestand
            dst.write(east_rent, 1)  # Schrijf het resultaat naar de eerste band

    print(f" East is succesvol geschreven. Hoort bij bestandspad {uitvoer_pad}")
    
    
    with rasterio.open(OUT_east_regression_path) as src1, rasterio.open(east_urb_filepath) as src2:
        # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
        meta = src1.meta.copy()

        # Werk metadata bij voor het uitvoerraster
        meta.update(driver='GTiff', dtype='float32')

        # Maak uitvoerrasterbestand aan
        uitvoer_pad = OUT_east_filtered_path
        with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
            # Voer de vermenigvuldiging uit op de invoerrasters
            raster1 = src1.read(1)  # Lees eerste band van raster1
            raster2 = src2.read(1)

            resultaat = raster1 * raster2 
            resultaat[resultaat <= 0] = np.nan
            # resultaat[resultaat<0] = np.nan # after inspecting the raster it seems values with 0 are Nan values 
            # Schrijf het resultaat naar het uitvoerrasterbestand
            dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band

    print(f"{region} is succesvol geschreven. Hoort bij bestandspad {uitvoer_pad}")

    region = "north"
    with rasterio.open(north_pop_filepath) as src2:#, rasterio.open(north_clipped_filepath) as src2urb:
        # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
        meta = src2.meta.copy()

        # Werk metadata bij voor het uitvoerraster
        meta.update(driver='GTiff', dtype='float32')

        # Maak uitvoerrasterbestand aan
        uitvoer_pad = OUT_north_regression_path 
        with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
            # Voer de vermenigvuldiging uit op de invoerrasters
            north_population = src2.read(1)  # Lees eerste band van raster1

            # North: Rent (euros per hectare) = 30000 + 8000*Population density (count per hectare) 
            north_rent = exp( ln( exp(9.11129) * fp(north_population, 1.05) ) )

            # resultaat[resultaat==255] = np.nan # after inspecting the raster it seems values with 255 are Nan values 
            # Schrijf het resultaat naar het uitvoerrasterbestand
            dst.write(north_rent, 1)  # Schrijf het resultaat naar de eerste band

    print(f"{region} is succesvol geschreven. Hoort bij bestandspad {uitvoer_pad}")

    with rasterio.open(OUT_north_regression_path) as src1, rasterio.open(north_urb_filepath) as src2:
        # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
        meta = src1.meta.copy()

        # Werk metadata bij voor het uitvoerraster
        meta.update(driver='GTiff', dtype='float32')

        # Maak uitvoerrasterbestand aan
        uitvoer_pad = OUT_north_filtered_path
        with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
            # Voer de vermenigvuldiging uit op de invoerrasters
            raster1 = src1.read(1)  # Lees eerste band van raster1
            raster2 = src2.read(1)

            resultaat = raster1 * raster2 
            resultaat[resultaat <= 0] = np.nan
            # resultaat[resultaat<0] = np.nan # after inspecting the raster in QGIS it seems values with 0 are Nan values 
            # Schrijf het resultaat naar het uitvoerrasterbestand
            dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band

    print(f"{region} is succesvol geschreven. Hoort bij bestandspad {uitvoer_pad}")

    region = "west"
    with rasterio.open(west_pop_filepath) as src3:#, rasterio.open(west_clipped_filepath) as src3urb:
        # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
        meta = src3.meta.copy()

        # Werk metadata bij voor het uitvoerraster
        meta.update(driver='GTiff', dtype='float32')

        # Maak uitvoerrasterbestand aan
        uitvoer_pad = OUT_west_regression_path
        with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
            # Voer de vermenigvuldiging uit op de invoerrasters
            west_population = src3.read(1)  # Lees eerste band van raster1
            
            # West: Rent (euros per hectare) = 52000 + 7300*Population density (count per hectare) 
            west_rent = exp( ln( exp(8.95072) * fp(west_population, 1.05) ) )

            # resultaat[resultaat==255] = np.nan # after inspecting the raster it seems values with 255 are Nan values 
            # Schrijf het resultaat naar het uitvoerrasterbestand
            dst.write(west_rent, 1)  # Schrijf het resultaat naar de eerste band

    print(f"{region} is succesvol geschreven. Hoort bij bestandspad {uitvoer_pad}")        


    with rasterio.open(OUT_west_regression_path) as src1, rasterio.open(west_urb_filepath) as src2:
        # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
        meta = src1.meta.copy()

        # Werk metadata bij voor het uitvoerraster
        meta.update(driver='GTiff', dtype='float32')

        # Maak uitvoerrasterbestand aan
        uitvoer_pad = OUT_west_filtered_path
        with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
            # Voer de vermenigvuldiging uit op de invoerrasters
            raster1 = src1.read(1)  # Lees eerste band van raster1
            raster2 = src2.read(1)

            resultaat = raster1 * raster2 
            resultaat[resultaat <= 0] = np.nan
            # resultaat[resultaat<0] = np.nan # after inspecting the raster in QGIS it seems values with 0 are Nan values 
            # Schrijf het resultaat naar het uitvoerrasterbestand
            dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band

    print(f"{region} is succesvol geschreven. Hoort bij bestandspad {uitvoer_pad}")

    region = "south"
    with rasterio.open(south_pop_filepath) as src4:#, rasterio.open(south_clipped_filepath) as src4urb:
        # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
        meta = src4.meta.copy()

        # Werk metadata bij voor het uitvoerraster
        meta.update(driver='GTiff', dtype='float32')

        # Maak uitvoerrasterbestand aan
        uitvoer_pad = OUT_south_regression_path
        with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
            # Voer de vermenigvuldiging uit op de invoerrasters
            south_population = src4.read(1)  # Lees eerste band van raster1

            # South model:  
            south_rent = exp( ln( exp(8.59005) * fp(south_population, 1.05) ) )

            # resultaat[resultaat==255] = np.nan # after inspecting the raster it seems values with 255 are Nan values 
            # Schrijf het resultaat naar het uitvoerrasterbestand
            dst.write(south_rent, 1)  # Schrijf het resultaat naar de eerste band

    print(f"{region} is succesvol geschreven. Hoort bij bestandspad {uitvoer_pad}")


    with rasterio.open(OUT_south_regression_path) as src1, rasterio.open(south_urb_filepath) as src2:
        # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
        meta = src1.meta.copy()

        # Werk metadata bij voor het uitvoerraster
        meta.update(driver='GTiff', dtype='float32')

        # Maak uitvoerrasterbestand aan
        uitvoer_pad = OUT_south_filtered_path
        with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
            # Voer de vermenigvuldiging uit op de invoerrasters
            raster1 = src1.read(1)  # Lees eerste band van raster1
            raster2 = src2.read(1)

            resultaat = raster1 * raster2 
            resultaat[resultaat <= 0] = np.nan
            # resultaat[resultaat<0] = np.nan # after inspecting the raster in QGIS it seems values with 0 are Nan values 
            # Schrijf het resultaat naar het uitvoerrasterbestand
            dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band

    print(f"{region} is succesvol geschreven. Hoort bij bestandspad {uitvoer_pad}")

if imputeRegressionEUwide == True:
    
    ''' Using the selected model relating population density and residential rent:
        LogRent = 1.09876LogPop + 8.53576

        Since ln(y) = A*ln(x) + B 
            rearranged for y is:
            y = e^(ln(e^B * x^A))

    '''
    modelDict = {"EU": "LogRent = 1.09876LogPop + 8.53576",
                 "reEU": "Rent = exp( ln( exp(8.53576) * Population(1.09876) ) )"
                 }
    print('made reference dictionary')
    eu_pop_filepath = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/SPP1/convert_km_2_ha/Pop_2020_population_hectare__.tif"
    print('read population file paths')

    eu_urb_filepath = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/urban_Reclass_new_LULC.tif"
    
    print('read urban land filter map file paths')

    from numpy import exp
    from numpy import log as ln
    from numpy import float_power as fp
    print('imported numpy functions: exp, log as ln, and float_power as fp')

    region = "eu_wide"

    with rasterio.open(eu_pop_filepath) as src1:#, rasterio.open(east_urb_filepath) as src2: 
        # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
        meta = src1.meta.copy()

        # Werk metadata bij voor het uitvoerraster
        meta.update(driver='GTiff', dtype='float32')

        # Maak uitvoerrasterbestand aan
        uitvoer_pad = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/SPP1/eu_wide_analysis/eu_wide_Pop_2020_rent_hectare_regression.tif"
        with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
            # Voer de vermenigvuldiging uit op de invoerrasters
            eu_population = src1.read(1)  # Lees eerste band van raster1

            # EU: Rent = exp( ln( exp(8.53576) * Population(1.09876) ) )
            eu_rent = exp( ln( exp(8.53576) * fp(eu_population, 1.09876) ) )

            # resultaat[resultaat> -255] = np.nan # after inspecting the raster it seems values with 255 are Nan values 
            # Schrijf het resultaat naar het uitvoerrasterbestand
            dst.write(eu_rent, 1)  # Schrijf het resultaat naar de eerste band

    print(f" EU is succesvol geschreven. Hoort bij bestandspad {uitvoer_pad}")
    
    
    eu_regression_path = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/SPP1/eu_wide_analysis/{region}_Pop_2020_rent_hectare_regression.tif"

    with rasterio.open(eu_regression_path) as src1, rasterio.open(eu_urb_filepath) as src2:
        # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
        meta = src1.meta.copy()

        # Werk metadata bij voor het uitvoerraster
        meta.update(driver='GTiff', dtype='float32')

        # Maak uitvoerrasterbestand aan
        uitvoer_pad = f"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/SPP1/eu_wide_analysis/{region}_Pop_2020_rent_hectare_filtered.tif"
        with rasterio.open(uitvoer_pad, 'w', **meta) as dst:
            # Voer de vermenigvuldiging uit op de invoerrasters
            raster1 = src1.read(1)  # Lees eerste band van raster1
            raster2 = src2.read(1)

            resultaat = raster1 * raster2 
            resultaat[resultaat <= 0] = np.nan
            # resultaat[resultaat<0] = np.nan # after inspecting the raster it seems values with 0 are Nan values 
            # Schrijf het resultaat naar het uitvoerrasterbestand
            dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band

    print(f"{region} is succesvol geschreven. Hoort bij bestandspad {uitvoer_pad}")

#######################################
## Extend four inputs to LULC extent ##
#######################################

# performed in QGIS:
#extension command:: gdal_translate -projwin 944000.0 5416000.0 6526000.0 942000.0 -a_nodata -9999.0 -of GTiff "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/SPP1/eu_regional_analysis/west_Pop_2020_rent_hectare_filtered.tif" "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets


##########################
## Combine four inputs  ##
##########################
    
if combineRegions == True:

    
    import numpy as np

    # Open invoerrasters
    east_extent = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/CLUMondo/eu_regional_analysis/extended/mar24_east_POP_2020_rent_hectare_extended.tif"
    west_extent = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/CLUMondo/eu_regional_analysis/extended/mar24_west_POP_2020_rent_hectare_extended.tif"
    north_extent = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/CLUMondo/eu_regional_analysis/extended/mar24_north_POP_2020_rent_hectare_extended.tif"
    south_extent = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/CLUMondo/eu_regional_analysis/extended/mar24_south_POP_2020_rent_hectare_extended.tif"
    combined_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/CLUMondo/eu_regional_analysis/extended/mar24_POP_2020_rent_hectare_combined__.tif"
    combined2_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/CLUMondo/eu_regional_analysis/extended/mar24_POP_2020_rent_hectare_combined_clean__.tif"

    
    with rasterio.open(east_extent) as src_East, rasterio.open(west_extent) as src_West, rasterio.open(north_extent) as src_North, rasterio.open(south_extent) as src_South:
        # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
        meta = src_East.meta.copy()

        # Werk metadata bij voor het uitvoerraster
        meta.update(driver='GTiff', dtype='float32')

        # Maak uitvoerrasterbestand aan
        out_path = combined_path
        with rasterio.open(out_path, 'w', **meta) as dst:
            # Voer de vermenigvuldiging uit op de invoerrasters
            east = src_East.read(1)  # Lees eerste band van raster1
            west = src_West.read(1)
            north = src_North.read(1)
            south = src_South.read(1)
            
            arrays = [east, south, north, west]

            combined_array = np.stack(arrays)

            res = np.nanmax(combined_array, axis = 0)

            dst.write(res, 1)  # Schrijf het resultaat naar de eerste band

    print(f"Uitvoerraster is succesvol geschreven. Hoort bij bestandspad {out_path}")

    urban_reclass_filepath = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/urban_Reclass_new_LULC.tif"

    with rasterio.open(combined_path) as src1, rasterio.open(urban_reclass_filepath) as src2:
        # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
        meta = src1.meta.copy()

        # Werk metadata bij voor het uitvoerraster
        meta.update(driver='GTiff', dtype='float32')
# Maak uitvoerrasterbestand aan
        out_path = combined2_path
        with rasterio.open(out_path, 'w', **meta) as dst:
            # Voer de vermenigvuldiging uit op de invoerrasters
            combi = src1.read(1)
            reclass = src2.read(1)  # Lees eerste band van raster1            

            
            resultaat1 = combi + 1                   # to keep all useful 0 pixels that are not NaN
            resultaat2 = resultaat1 * reclass            # masking step
            resultaat3 = resultaat2/(resultaat2>0)       # so that all values greater than 0.1 get NaN value
            resultaat4 = resultaat3 - 1                  # to restore the values back down by 1


            dst.write(resultaat4, 1)  # Schrijf het resultaat naar de eerste band

    print(f"Uitvoerraster is succesvol geschreven. Hoort bij bestandspad {out_path}")
