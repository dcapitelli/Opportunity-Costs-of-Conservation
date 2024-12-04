import geopandas as gpd
import pandas as pd

ref_vec_feb = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/NUTS_regions_missing_countries/reference_vector_feb_24/reference_vector_feb_24.shp"
bh_vec = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/NUTS_regions_missing_countries/reference_vector_bosnia.shp"
ref_vec_mar = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/NUTS_regions_missing_countries/reference_vector_feb_24/reference_vector_mar_24.shp"
OUT_ref_mar = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/NUTS_regions_missing_countries/reference_vector_feb_24/reference_vector_mar_24_cleaned.shp"

# ref_vect_mar was made in QGIS using the vector union function. The attribute table was then cleaned in QGIS

ref_vect_mar = gpd.read_file(ref_vec_mar)
ref_vector = gpd.read_file(ref_vec_feb)
bh_vector = gpd.read_file(bh_vec)

ref_vect_mar.columns
dropcols = ['NUTS_ID__1', 'LEVL_COD_4', 'CNTR_COD_4', 'NAME_LAT_4', 'NUTS_NAM_4',
       'layer_2_2', 'path_2_2', 'NUTS_3', 'LEVL_CODE', 'CNTR_CODE',
       'NAME_LATN', 'NUTS_NAME','NUTS_3_2',
       'LEVL_CODE_', 'CNTR_CODE_', 'NAME_LATN_', 'NUTS_NAME_']

ref_vect_mar = ref_vect_mar.drop(columns = dropcols)

ref_vect_mar.to_file(OUT_ref_mar)