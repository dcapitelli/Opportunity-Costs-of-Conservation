
"""
Credit to @author: nde370 for sharing his "align rasters" script from the Land system map for  Europe report. I used the structure of his code and adapted it to my needs 
"""

import rioxarray, os
from rasterio.enums import Resampling 
import fiona
from shapely.geometry import shape


project_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries"

IN_master_vector_path = project_path + "/NUTS_regions_missing_countries/reference_vector_feb_24/reference_vector_mar_24_cleaned.shp"


# switches to contol which processes will be run. 
aligning = False
makeRegionRas = False
clipping = True

# Reference raster (all rasters will be aligned to this one)
reference_ras = r'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/New LULC map/eu_lum_map_2_nov_clip.tif'
# Region shape (shapefile with 1 polygon (may be multipart, but only 1 feature)). polygon must be unsimplified (follows raster exactly)
region_shp = r'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/NUTS_regions_missing_countries/reference_vector_feb_24/reference_vector_mar_24_cleaned.shp'
# where to store aligned but unclipped rasters
aligned_dir = r'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/CLUMondo/aligned_files'
# where to store clipped rasters
clipped_dir = r'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/CLUMondo/clipped_files'
# directory where rasters to be aligned are stored 
rasterDir = r'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/CLUMondo/selected_files'
# dictionary with resampling method included
# All resampling methods are here: https://rasterio.readthedocs.io/en/stable/api/rasterio.enums.html#rasterio.enums.Resampling


rastersDic = {'Pop_2020_Aligned.tif':                            Resampling.nearest}



def matching_crs(reference_raster,input_rasters, in_directory):
    """
    input:
      reference_raster  :   reference raster, all other rasters will take the crs and resolution of this raster
      input_rasters     :   dictionary of all rasters that need to be reprojected/resampled (keys) and resample methods as values ()
                              (example: [Resampling.mode,Resampling.bilinear,Resampling.average])
    
    returns:
      list of reprojected/resampled rasters
    """
    matched_rasters = {}
    for r in input_rasters:
        print('aligning '+ r)
        # load as raster
        raster = rioxarray.open_rasterio(os.path.join(in_directory,r), masked=True)
        reprojected_raster = raster.rio.reproject_match(reference_raster, resampling=input_rasters[r])
        matched_rasters[r] = reprojected_raster
    return matched_rasters

# open the reference grid
ref_ras = rioxarray.open_rasterio(reference_ras,  masked=True)

###############################################################################
# 1: align rasters
###############################################################################

if aligning == True:
    print('aligning...')
    matched_rasters = matching_crs(ref_ras, rastersDic,rasterDir)
    print('saving')
    for r in matched_rasters:
        print('/tsaving '+ r)
        matched_rasters[r].rio.to_raster(os.path.join(aligned_dir, r))
else:
    # open these rasters from dir
    matched_rasters = {}
    for r in rastersDic:
        matched_rasters[r] = rioxarray.open_rasterio(os.path.join(aligned_dir,r), masked=True)

###############################################################################
# 2: define region 
###############################################################################    

# make the region raster (based on the domain of the CORINE raster (which has no no-data inside it's extent)).
# This region raster only serves to then make a polygon of the study area.
if makeRegionRas == True:
    print('making region raster...')
    regionRas = matched_rasters['CORINE.tif'].astype('float')
    regionRas.rio.write_nodata(0, encoded=True, inplace=True) # untested, maybe this line should just be dropped
    regionRas = regionRas.where(regionRas != 44, regionRas.rio.nodata) # class 44 is territorial waters (sea)
    regionRas = regionRas.where(regionRas < 0, 1) # stupid syntax of this where statement
    regionRas.rio.to_raster(r'C:/Users/nde370/surfdrive/PhD_supervision/Saskia/Forest management Europe/Forest management Europe/Niels_sandbox/test_aligner/region/region.tif')
    # convert this regionRas to polygon in arc / Q. do not simplify, make multipart

###############################################################################
# 3. Clip
###############################################################################
if clipping == True:
    print('clipping...')
    regionSHP = fiona.open(region_shp)
    region_geom = shape(regionSHP[0]['geometry'])
    clipped_rasters = {}
    for r in matched_rasters:
        print('/tclipping ' + r)
        clipped_raster = matched_rasters[r].rio.clip([region_geom])
        clipped_rasters[r] = clipped_raster
        clipped_raster.rio.to_raster(os.path.join(clipped_dir,r)) 


print("clipping and aligning complete")

