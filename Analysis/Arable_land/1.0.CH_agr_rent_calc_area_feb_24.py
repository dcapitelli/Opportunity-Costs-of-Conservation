import geopandas as gpd
import pandas as pd
import os.path


# this script is a little messy!


# organise the paths
root_dir = 'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries'
sub_nuts = 'NUTS_regions_missing_countries'
sub_input = 'Input_datasets/Agricultural_land_rents'
example_path = os.path.join(root_dir, sub_nuts, 'here').replace("/","/")


# input file paths
IN_nuts_ch_bh_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/NUTS_regions_missing_countries/reference_vector_feb_24/reference_vector_mar_24_cleaned.shp"
IN_agr_full_list_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Agricultural_land_rents/updated_list_agr_land_rent_feb24/arable_pastoral_rents_sanitized_stitched_BH_AL_RS_MK_ME_XK_CY_PT_CH_feb_24_update.csv"

IN_ch_file_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/NUTS_regions_missing_countries/NUTS3_RG_01M_2021_3035_CH.shp"
IN_ch_nuts3_rent_path ="C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Agricultural_land_rents/ch__nuts3_agr_rent.csv"
IN_qgis_made_union_nuts3 = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/NUTS_regions_missing_countries/Union_EU_marco_microstates_CH_.shp"
IN_ch_uaa = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Agricultural_land_rents/updated_list_agr_land_rent_feb24/ch_uaa_nuts3.csv"
IN_union_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/NUTS_regions_missing_countries/Union_EU_marco_microstates_cleaned.shp"
# IN_qgis_made_union_nuts3 was not used in the end as I made the vector merge without QGIS


# output file paths, OUT_union_path is the final shapefile of agr rent
OUT_union_cleaned = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/NUTS_regions_missing_countries/Union_EU_marco_microstates_cleaned_NUTS.shp"

OUT_CH_rent_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/NUTS_regions_missing_countries/NUTS3_RG_01M_2021_3035_CH_km2_rent_.shp"
OUT_union_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Agricultural_land_rents/updated_list_agr_land_rent_feb24/arable_pastoral_rents_sanitized_stitched_BH_AL_RS_MK_ME_XK_CY_PT_CH_feb_24__final.shp"
OUT_union_new_path_merge_populated = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/NUTS_regions_missing_countries/Union_EU_marco_microstates_dirty_CH_nuts3_merge_populated.shp"
OUT_union_new_path_merge_removed = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/NUTS_regions_missing_countries/Union_EU_marco_microstates_dirty_CH_nuts3_merge_removed.shp"
# OUT_union_path_test = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Agricultural_land_rents/updated_list_agr_land_rent_feb24/arable_pastoral_rents_sanitized_stitched_BH_AL_RS_MK_ME_XK_CY_PT_CH__test__2.shp"

#function switches:
calcCHRent = False



if calcCHRent == True:
    ## First task is to make the Switzerland (CH) vector and perform calculations to get the euro/ha values

    ch_vector = gpd.read_file(IN_ch_file_path)
    ch_uaa = pd.read_file(IN_ch_uaa)

    ch_vector_uaa = ch_vector.merge(ch_uaa, on = 'NUTS_ID')

    # OBSOLETE as realised that I needed to use the UAA to get accurate values.
    # ch_vector["area_m2"] = ch_vector["geometry"].area
    # ch_vector["area_km2"] = ch_vector["geometry"].area * 1e-6


    ch_table = pd.read_csv(IN_ch_nuts3_rent_path)

    ch_vector_uaa = ch_vector_uaa.rename(columns = {"NUTS_3":"NUTS_ID" })

    ch_table =ch_table.rename(columns = {"NUTS_3": "NUTS_ID"})

    ch_merged = ch_vector_uaa.merge(ch_table, on ="NUTS_ID")

    ch_merged = ch_merged.drop(columns = ["MOUNT_TYPE","URBN_TYPE", "COAST_TYPE", "FID", "Area"])

    ch_merged["uaa_ha"] = ch_merged["uaa_ha"].str.replace(' ','')

    ch_merged["uaa_ha"] = ch_merged["uaa_ha"].astype(int)

    ch_merged['eu_ha'] = ch_merged["2021_euros"]/ch_merged["uaa_ha"]

    # create area-based weight for basel_city (422ha) and basel_countryside (21367ha)
    proportion_basel_city_CH031 =422 /(21367 + 422)
    proportion_basel_country_CH032 =21367 /(21367 + 422)

    # find the original values for basel_city and basel_countryside
    rent_basel_city_CH031 = ch_merged.loc[ch_merged['NUTS_ID'] == "CH031", '2021_euros'].iloc[0]
    rent_basel_city_CH032 = ch_merged.loc[ch_merged['NUTS_ID'] == "CH032", '2021_euros'].iloc[0]

    # use area-based weight for basel_city and basel_countryside to adjust the rent
    new_rent_CH031 = proportion_basel_city_CH031 * rent_basel_city_CH031
    new_rent_CH032 = proportion_basel_country_CH032 * rent_basel_city_CH032

    # create boolean mask
    mask31 = ch_merged["NUTS_ID"] == "CH031"
    mask32 = ch_merged["NUTS_ID"] == "CH032"

    # insert value into dataframe using boolean mask
    ch_merged.loc[mask31, "2021_euros"] = new_rent_CH031
    ch_merged.loc[mask32, "2021_euros"] = new_rent_CH032

    # redo the calculations to get normal values for basel city and basel countryside
    ch_merged["eu_ha"] = ch_merged["2021_euros"]/ch_merged["uaa_ha"]

    print("Now the city and landscape regions of Basel are the same!")


    ch_merged.to_file(OUT_CH_rent_path)


## Next step is to merge the two following files and remove the CH from the union shapefile first

IN_union_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/NUTS_regions_missing_countries/Union_EU_marco_microstates_cleaned.shp"
OUT_CH_rent_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/NUTS_regions_missing_countries/NUTS3_RG_01M_2021_3035_CH_km2_rent_.shp"
union_new_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/NUTS_regions_missing_countries/Union_EU_marco_microstates_dirty_CH_nuts3.shp"

union_vector = gpd.read_file(IN_union_path)
union_vector_noCH = union_vector[union_vector['CNTR_COD_4'] !='CH']
# union_vector_CH_nuts3 = gpd.read_file(union_new_path)
ch_rent_vector = gpd.read_file(OUT_CH_rent_path)

union_vector_noCH.columns
ch_rent_vector.columns

## 
# Merging the CH and NUTS2 geodatasets
##

union_vector_noCH = union_vector_noCH.to_crs(3035)
CH_NUTS2_merge = gpd.overlay(union_vector_noCH, ch_rent_vector, how = 'union')

CH_NUTS2_merge.to_file(union_new_path)

# CH_NUTS2_merge has the polygons for the whole of EU plus CH at nuts3, now we need to add the rent onto the shapefile


CH_NUTS2_merge.columns
['NUTS_ID__1', 'LEVL_COD_4', 'CNTR_COD_4', 'NAME_LAT_4', 'NUTS_NAM_4',
       'layer_2_2', 'path_2_2', 'NUTS_ID', 'LEVL_CODE', 'CNTR_CODE',
       'NAME_LATN', 'NUTS_NAME', 'name', 'uaa_ha', 'NUTS_2', 'Cantons',
       '2021_thous', '2021_tho_1', '2021_euros', 'eu_ha', 'geometry']

drop_cols = ['NUTS_2', 'Cantons','2021_thous', '2021_tho_1', '2021_euros', 'euros_km2', 'euros_ha']
CH_NUTS2_merge = CH_NUTS2_merge.drop(columns = drop_cols)

CH_NUTS2_merge.sort_values('NUTS_ID__1')
union_new_path_merge = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/NUTS_regions_missing_countries/Union_EU_marco_microstates_dirty_CH_nuts3_merge.shp"


union_vector_noCH = union_vector_noCH.rename(columns = 
{'NUTS_ID__1': "NUTS_ID", 
 'LEVL_COD_4': 'LEVL_CODE',
 'CNTR_COD_4':'CNTR_CODE',
 'NAME_LAT_4': 'NAME_LATN',
 'NUTS_NAM_4':'NUTS_NAME',

 })


ch_rent_vector = ch_rent_vector.rename(columns = {
    'NUTS_3': 'NUTS_ID__1',
    'LEVL_CODE': 'LEVL_COD_4',
    'CNTR_CODE':'CNTR_COD_4',
    'NAME_LATN':'NAME_LAT_4'})



CH_NUTS2_merge.to_file(OUT_union_new_path_merge_populated)

# removed the duplicated rows (CH plus other countries)
CH_NUTS2_merge_rmv = CH_NUTS2_merge.copy()
dup_index = CH_NUTS2_merge_rmv[(CH_NUTS2_merge_rmv['LEVL_COD_4'] == 2.0) & (CH_NUTS2_merge_rmv['LEVL_CODE'] == 3.0)].index #and (CH_NUTS2_merge['LEVL_CODE'] == 3)
CH_NUTS2_merge_rmv.drop(dup_index, inplace= True)
CH_NUTS2_merge_rmv.to_file(OUT_union_new_path_merge_removed)



#### 
# merging the table and geodataframe together
####

## First the grass and forest updated vector
agr_full_table = pd.read_csv(IN_agr_full_list_path)
reference_vector = gpd.read_file(IN_nuts_ch_bh_path)

agr_full_table.columns
reference_vector.columns

rename_cols_dict = {'NUTS_ID__2': "NUTS_ID"}
reference_vector = reference_vector.rename(columns = rename_cols_dict)
merged_vector = reference_vector.merge(agr_full_table, on="NUTS_ID")
merged_vector['LEVL_COD_1'] = merged_vector['LEVL_COD_1'].astype(int)

merged_vector = merged_vector.rename(columns= {'ARABLE_LAND_RENT_EUR2021/HA': "ARNE21_HA","PASTORAL_LAND_RENT_EUR2021/HA": "PRNE21_HA"})

merged_vector.to_file(OUT_union_cleaned)


# Second for the crop vector

#rename CH_NUTS2_merge_rmv columns for merge
rename_cols_dict = {'NUTS_ID__1': "NUTS_ID",
                    'LEVL_CODE':'XLEVL_COD',
                    'LEVL_COD_4':'LEVL_CODE'}#, 
#   'CNTR_COD_4':'CNTR_CODE',
#  'NAME_LAT_4': 'NAME_LATN',
#  'NUTS_NAM_4':'NUTS_NAME'}
CH_NUTS2_merge_rmv = CH_NUTS2_merge_rmv.rename(columns = rename_cols_dict)

CH_NUTS2_merge_rmv = CH_NUTS2_merge_rmv.rename(columns = {'LEVL_CODE':'XLEVL_COD','LEVL_COD_4':'LEVL_CODE'})
CH_NUTS2_merge_rmv['LEVL_CODE'] =CH_NUTS2_merge_rmv['LEVL_CODE'].astype(int)


#rename CH_NUTS2_merge_rmv columns for merge
rename_cols_dict = {'NUTS_ID__1': "NUTS_ID",
                    'LEVL_CODE':'XLEVL_COD',
                    'LEVL_COD_4':'LEVL_CODE'}
CH_NUTS2_merge_rmv = CH_NUTS2_merge_rmv.rename(columns = rename_cols_dict)
CH_NUTS2_merge_rmv['LEVL_CODE'] =CH_NUTS2_merge_rmv['LEVL_CODE'].astype(int)

###`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

# populating the CH_NUTS2_merge['NUTS_ID__1'] columns
NA_mask = CH_NUTS2_merge_rmv['NUTS_ID__1'].isna() 
CH_NUTS2_merge_rmv.loc[NA_mask, 'NUTS_ID__1'] = CH_NUTS2_merge_rmv['NUTS_ID']
CH_NUTS2_merge_rmv.loc[NA_mask,'LEVL_COD_4'] = CH_NUTS2_merge_rmv['LEVL_CODE']
CH_NUTS2_merge_rmv.loc[NA_mask,'CNTR_COD_4'] = CH_NUTS2_merge_rmv['CNTR_CODE']
CH_NUTS2_merge_rmv.loc[NA_mask,'NAME_LAT_4'] = CH_NUTS2_merge_rmv['NAME_LATN']
CH_NUTS2_merge_rmv.loc[NA_mask,'NUTS_NAM_4'] = CH_NUTS2_merge_rmv['NUTS_NAME']

# change the nuts_id column to 'NUTS_ID__1' in agr_full_table for merge 
agr_full_table = agr_full_table.rename(columns = {'NUTS_ID':'NUTS_ID__1'})

# Merge the CH_NUTS2_merge_rmv vector with the rent values from agr_full_table
agri_rent_nuts3 = CH_NUTS2_merge_rmv.merge(agr_full_table, on= 'NUTS_ID__1') 
agri_rent_nuts3.columns

agri_rent_nuts3.sort_values('LEVL_COD_4')
agri_rent_nuts3 = agri_rent_nuts3.rename(columns= {'ARABLE_LAND_RENT_EUR2021/HA': "ARNE21_HA","PASTORAL_LAND_RENT_EUR2021/HA": "PRNE21_HA"})

# transpose the eu_ha values onto the arable and pastoral columns
CH_mask_nuts3 = agri_rent_nuts3['LEVL_COD_4'] == 3.0
agri_rent_nuts3.loc[CH_mask_nuts3,'ARNE21_HA'] = agri_rent_nuts3['eu_ha']
agri_rent_nuts3.loc[CH_mask_nuts3,'PRNE21_HA'] = agri_rent_nuts3['eu_ha']

# change the level code from float to int
agri_rent_nuts3['LEVL_COD_4'] =agri_rent_nuts3['LEVL_COD_4'].astype(int)

# drop columns that aren't useful
dropcols_final = {'NUTS_ID', 'LEVL_CODE', 'CNTR_CODE_x',
       'NAME_LATN', 'NUTS_NAME_x', 'name', 'uaa_ha', 'NUTS_2', 'Cantons',
       '2021_thous', '2021_tho_1', '2021_euros', 'eu_ha',
       'CNTR_CODE_y', 'NUTS_NAME_y'}
agri_rent_nuts3_drop = agri_rent_nuts3.drop(columns = dropcols_final)
['NUTS_ID__1', 'LEVL_COD_4', 'CNTR_COD_4', 'NAME_LAT_4', 'NUTS_NAM_4',
       'layer_2_2', 'path_2_2',  'ARNE21_HA', 'ARABLE_LAND_RENT_ORIGIN',
       'PRNE21_HA', 'PASTORAL_LAND_RENT_ORIGIN']
# 'NUTS_NAME_x' appears twice so can't save the dataframe
agri_rent_nuts3_cleaned_up = agri_rent_nuts3.drop(columns = ['NUTS_NAME_x','NAME_LATN'])
agri_rent_nuts3_drop.to_file(OUT_union_path)
#SOLVED!! final output file




