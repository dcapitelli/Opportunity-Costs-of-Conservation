###########################
## Rasterise crop prices ##
###########################

import pandas as pd
import numpy as np
import geopandas as gpd
import rasterio
from rasterio import features
from rasterio.enums import MergeAlg
from rasterio.plot import show
from numpy import int16

# old file --> spam_crop_prices_national_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Crop_prices/spam_crop_prices_national_sanitized.csv"
# old line --> spam_crop_prices_national_check = pd.read_csv(spam_crop_prices_national_path)
# old line --> spam_crop_price_0nan = spam_crop_prices_national_check.replace(0.000000, np.nan, inplace=True)
# old line --> spam_crop_price_nan0 = spam_crop_prices_national_check['rice_price_eur2021/kg'].replace(0, np.nan, inplace=True)
# old line --> spam_crop_prices_national_check['rice_price_eur2021/kg']
# old line --> spam_crop_price_nan0 = spam_crop_prices_national_check.mask(np.isclose(spam_crop_prices_national_check.values, 0.000000))
# old line --> spam_crop_prices_national_check
# old line --> spam_crop_prices_national_check_nan_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Crop_prices/spam_crop_prices_national_check_nan.csv"
# old line --> spam_crop_prices_national_check.to_csv(spam_crop_prices_national_check_nan_path)

# clean the crop prices dataset
# spam_crop_prices_national_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Crop_prices/spam_crop_prices_national_sanitized_SOD_update_1.1.csv"
spam_crop_prices_national_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Crop_prices/spam_crop_prices_national_sanitized_feb24_update_1.1.csv"
spam_crop_prices_national = pd.read_csv(spam_crop_prices_national_path)
spam_crop_prices_national.columns
spam_crop_prices_national_cleaned = spam_crop_prices_national.drop(spam_crop_prices_national.filter(regex='source').columns, axis=1)
spam_crop_prices_national_cleaned['Num_rows'] = (spam_crop_prices_national_cleaned[['whea_price_eur2021/kg', 'rice_price_eur2021/kg',
       'maiz_price_eur2021/kg', 'barl_price_eur2021/kg',
       'pmil_price_eur2021/kg', 'smil_price_eur2021/kg',
       'sorg_price_eur2021/kg', 'ocer_price_eur2021/kg',
       'pota_price_eur2021/kg', 'swpo_price_eur2021/kg',
       'yams_price_eur2021/kg', 'cass_price_eur2021/kg',
       'orts_price_eur2021/kg', 'bean_price_eur2021/kg',
       'chic_price_eur2021/kg', 'cowp_price_eur2021/kg',
       'pige_price_eur2021/kg', 'lent_price_eur2021/kg',
       'opul_price_eur2021/kg', 'soyb_price_eur2021/kg',
       'grou_price_eur2021/kg', 'cnut_price_eur2021/kg',
       'oilp_price_eur2021/kg', 'sunf_price_eur2021/kg',
       'rape_price_eur2021/kg', 'sesa_price_eur2021/kg',
       'ooil_price_eur2021/kg', 'sugc_price_eur2021/kg',
       'sugb_price_eur2021/kg', 'cott_price_eur2021/kg',
       'ofib_price_eur2021/kg', 'acof_price_eur2021/kg',
       'rcof_price_eur2021/kg', 'coco_price_eur2021/kg',
       'teas_price_eur2021/kg', 'toba_price_eur2021/kg',
       'bana_price_eur2021/kg', 'plnt_price_eur2021/kg',
       'trof_price_eur2021/kg', 'temf_price_eur2021/kg',
       'vege_price_eur2021/kg', 'rest_price_eur2021/kg']] > 0).sum(axis=1)
spam_crop_prices_national_cleaned = spam_crop_prices_national_cleaned.rename(columns={"Country_NUTS_Code": "CNTR_COD_4"})
spam_crop_prices_national_cleaned.columns

# Merge the nuts0 and crop price count datasets
# old path spam_crop_prices_national_nosource_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Crop_prices/spam_crop_prices_national_sanitized_CY_KO_ME_no_source_price_count.csv"

# old path nuts0_polygon_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/NUTS_regions_missing_countries/merged_NUTS0_XK_BIH.shp"
nuts0_polygon_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/NUTS_regions_missing_countries/reference_vector_feb_24/reference_vector_feb_24.shp"
nuts0_polygon = gpd.read_file(nuts0_polygon_path)

nuts0_polygon_crop_price_count = nuts0_polygon.merge(spam_crop_prices_national_cleaned, on="CNTR_COD_4")
# already clean so no cleaning needed: nuts0_polygon_crop_price_count_clean = nuts0_polygon_crop_price_count.drop(columns=['GID_0','COUNTRY','GID_0_2','COUNTRY_2','MOUNT_TYPE','URBN_TYPE','COAST_TYPE','FID'])
nuts0_polygon_crop_price_count.head(30)

vector0 = nuts0_polygon_crop_price_count
vector0 = vector0.fillna(0)
vector0
vector0.to_file("C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/eu_nuts0_crop_prices_feb24_update1.1.shp")
                # "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/eu_nuts0_crop_prices_SOD_update1.1.shp"
                # C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/eu_nuts0_crop_prices_0_MAGNET.shp")


# Rasterize the ['Num_rows']

# Read in vector
vector = nuts0_polygon_crop_price_count

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Open example raster
raster = rasterio.open('C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/Nov23_EU_landSystem.tif')

# create tuples of geometry, value pairs, where value is the attribute value you want to burn
geom_value = ((geom,value) for geom, value in zip(vector.geometry, vector['Num_rows']))

# Rasterize vector using the shape and transform of the raster
rasterized = features.rasterize(geom_value,
                                out_shape = raster.shape,
                                transform = raster.transform,
                                all_touched = False,
                                fill = -99,   # background value
                                merge_alg = MergeAlg.replace,
                                dtype = float)


# save the rasterized vector out
# old path 'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/eu_nuts0_crop_price_count_MAGNET.tif'
# 'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/eu_nuts0_crop_price_count_SOD_update_1.1.tif
feb_24_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/eu_nuts0_crop_prices_feb24_update1.1.tif"
with rasterio.open(
        'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/eu_nuts0_crop_price_count_feb24_update_1.1.tif', "w",
        driver = "GTiff",
        crs = raster.crs,
        transform = raster.transform,
        dtype = rasterio.float32,
        count = 1,
        width = raster.width,
        height = raster.height) as dst:
    dst.write(rasterized, indexes = 1)


# fill na with 0s
# vector0 = vector.fillna(0)
print(vector0.columns) 

# vector0.to_file("C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/eu_nuts0_crop_prices_0_MAGNET.shp")
# go to script called crop_price_rasterize.py


## end of script



