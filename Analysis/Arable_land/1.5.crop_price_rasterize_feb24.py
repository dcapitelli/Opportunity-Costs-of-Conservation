

# Rasterize the crop prices
import geopandas as gpd
import rasterio
from rasterio import features
from rasterio.enums import MergeAlg
from rasterio.plot import show
from numpy import int16



# Read in vector
vector = gpd.read_file("C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/eu_nuts0_crop_prices_feb24_update1.1.shp")
                    

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'maiz_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')


#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'rice_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'whea_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')


#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'barl_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'pmil_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'smil_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'sorg_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'ocer_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'pota_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'swpo_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'yams_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'bean_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'chic_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'cowp_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'pige_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'lent_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'opul_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'soyb_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'grou_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'cnut_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'oilp_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'sunf_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'rape_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'sesa_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'ooil_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'sugc_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'sugb_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'cott_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'ofib_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'toba_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'bana_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')

#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'trof_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')


#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'temf_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')


#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'vege_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')


#################################
### repeatable section of code ##
#################################

# assign column to burn
burn_name = 'rest_price'
burn_value = vector[burn_name]

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

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


OUT_crop_price_path = f'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif'

# save the rasterized vector out
with rasterio.open(
        OUT_crop_price_path, "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)

print(f'Crop price rasterization was successful for: {burn_name}')
print(f'file stored under: C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_biomass_eu/eu_crop_price_euro2021kg/feb_24_update/eu_nuts0_crop_price_{burn_name}_eur2021kg_feb24_update_1.1.tif ')

#################################
### repeatable section of code ##
#################################

# [      'whea_price', 'rice_price', 'maiz_price', 'barl_price', 'pmil_price',
#        'smil_price', 'sorg_price', 'ocer_price', 'pota_price', 'swpo_price',
#        'yams_price', 'bean_price', 'chic_price', 'cowp_price', 'pige_price', 
#        'lent_price', 'opul_price', 'soyb_price', 'grou_price', 'cnut_price', 
#        'oilp_price', 'sunf_price', 'rape_price', 'sesa_price', 
#        'ooil_price', 'sugc_price', 'sugb_price', 'cott_price',   
#        'ofib_price', 'toba_price', 'bana_price', 'trof_price', 'temf_price',
#        'vege_price', 'rest_price', 'crpricnum', 'Mask_nodat', 'geometry']




## end of script



