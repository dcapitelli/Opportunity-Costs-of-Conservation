# Thanks to Paul for helping me make this script


import arcpy
from arcpy.sa import *
from arcpy import env  
import winsound
duration = 5000  # milliseconds
freq = 440  # Hz

arcpy.env.overwriteOutput = True
arcpy.CheckOutExtension("Spatial")
# arcpy.env.snapRaster = "Z:/arcpy_files/EULandClass/EU_landSystem.tif" # add the raster to snap to here
arcpy.env.snapRaster = "Z:/arcpy_files/NewLandUse/Nov23_EU_landSystem.tif"
arcpy.env.workspace = "Z:/arcpy_files"


cell_size_degrees = 0.0174532925199433
cell_size_meters = 1000
# arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("ETRS 1989")
# arcpy.env.extent ="Z:/arcpy_files/EULandClass/EU_landSystem.tif"  
arcpy.env.extent = "Z:/arcpy_files/NewLandUse/Nov23_EU_landSystem.tif"

cattle = False
sheep = False
goat = True

## General settings ready ##
if cattle == True:
    raster_name = 'catt'

    in_raster_reproj_path = "Z:/arcpy_files/grass_biomass_yield/GLW4_catt/5_{}_2015_Da.tif".format(raster_name)
    out_raster_reproj_path = "Z:/arcpy_files/grass_biomass_yield/GLW4_aligned/reprojected_{}_heads_10km.tif".format(raster_name)
    out_coordinate_system_path = "Z:/arcpy_files/reference_vector_OLD/eu_nuts_2_agr_rents_TR_FRY_JanMayenSvalbard_removed.prj"

    out_raster_reproj_file = 'reprojected_{}_heads_10km.tif'.format(raster_name)

    arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, out_coordinate_system_path, "NEAREST") #reproject your raster here

    in_raster_resample_path = out_raster_reproj_path
    out_raster_resample_path = "Z:/arcpy_files/grass_biomass_yield/reprojected_and_resampled_GLW4/reproj_resampled_{}_heads_10km.tif".format(raster_name)
    arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

    out_raster_clipped_path = "Z:/arcpy_files/grass_biomass_yield/reprojected_resampled_clipped_GLW4/prjsmp_clip_{}_heads_10km_COMPARE_with_NEW_LULC.tif".format(raster_name)
    # mask_polygon_file = "Z:/arcpy_files/reference_vector_OLD/eu_nuts_2_agr_rents_TR_FRY_JanMayenSvalbard_removed.shp"
    mask_polygon_file = "Z:/arcpy_files/ReferenceVector_feb24/reference_vector_mar_24_cleaned.shp"
    outExtractByMask = ExtractByMask(out_raster_resample_path, mask_polygon_file) #extract by mask
    outExtractByMask.save(out_raster_clipped_path)

    print("{} snap successful".format(raster_name))
    print(" ")
    print("reprojected, resampled, and clipped GLW4 file available at {} ".format(out_raster_clipped_path))
    print(" ")

    winsound.Beep(freq, duration)
#######################
# repeatable section ##
########################
if sheep == True:
    raster_name = 'shee'

    in_raster_reproj_path = "Z:/arcpy_files/grass_biomass_yield/GLW4_shee/5_{}_2015_Da.tif".format(raster_name)
    out_raster_reproj_path = "Z:/arcpy_files/grass_biomass_yield/GLW4_aligned/reprojected_{}_heads_10km.tif".format(raster_name)
    out_coordinate_system_path = "Z:/arcpy_files/reference_vector/eu_nuts_2_agr_rents_TR_FRY_JanMayenSvalbard_removed.prj"
    out_raster_reproj_file = 'reprojected_{}_heads_10km.tif'.format(raster_name)

    arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, out_coordinate_system_path, "NEAREST") #reproject your raster here

    in_raster_resample_path = out_raster_reproj_path
    out_raster_resample_path = "Z:/arcpy_files/grass_biomass_yield/reprojected_and_resampled_GLW4/reproj_resampled_{}_heads_10km.tif".format(raster_name)
    arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

    out_raster_clipped_path = "Z:/arcpy_files/grass_biomass_yield/reprojected_resampled_clipped_GLW4/prjsmp_clip_{}_heads_10km.tif".format(raster_name)
    mask_polygon_file = "Z:/arcpy_files/reference_vector/eu_nuts_2_agr_rents_TR_FRY_JanMayenSvalbard_removed.shp"
    outExtractByMask = ExtractByMask(out_raster_resample_path, mask_polygon_file) #extract by mask
    outExtractByMask.save(out_raster_clipped_path)

    print("{} snap successful".format(raster_name))
    print(" ")
    print("reprojected, resampled, and clipped GLW4 file available at {} ".format(out_raster_clipped_path))
    print(" ")
    winsound.Beep(freq, duration)
########################
## repeatable section ##
########################

if goat == True:
    raster_name = 'goat'

    in_raster_reproj_path = "Z:/arcpy_files/grass_biomass_yield/GLW4_goat/5_{}_2015_Da.tif".format(raster_name)
    out_raster_reproj_path = "Z:/arcpy_files/grass_biomass_yield/GLW4_aligned/mar24_reprojected_{}_heads_10km.tif".format(raster_name)
    out_coordinate_system_path = "Z:/arcpy_files/reference_vector_OLD/eu_nuts_2_agr_rents_TR_FRY_JanMayenSvalbard_removed.prj"
    # out_coordinate_system_path = arcpy.SpatialReference(3035)


    arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, out_coordinate_system_path, "NEAREST") #reproject your raster here

    in_raster_resample_path = out_raster_reproj_path
    out_raster_resample_path = "Z:/arcpy_files/grass_biomass_yield/reprojected_and_resampled_GLW4/mar24_reproj_resampled_{}_heads_10km.tif".format(raster_name)
    arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

    out_raster_clipped_path = "Z:/arcpy_files/grass_biomass_yield/reprojected_resampled_clipped_GLW4/mar24_prjsmp_clip_{}_heads_10km_COMPARE_with_NEW_LULC.tif".format(raster_name)
    # mask_polygon_file = "Z:/arcpy_files/reference_vector_OLD/eu_nuts_2_agr_rents_TR_FRY_JanMayenSvalbard_removed.shp"
    mask_polygon_file = "Z:/arcpy_files/ReferenceVector_feb24/reference_vector_mar_24_cleaned.shp"
    outExtractByMask = ExtractByMask(out_raster_resample_path, mask_polygon_file) #extract by mask
    outExtractByMask.save(out_raster_clipped_path)

    print("{} snap successful".format(raster_name))
    print(" ")
    print("reprojected, resampled, and clipped GLW4 file available at {} ".format(out_raster_clipped_path))
    print(" ")
    winsound.Beep(freq, duration)
##############################
## End of repeatable section ##
##############################

print("#~~~~~~~~~End~~of~~script~~~~~~~~~~#")

#~~~~~~~~~End~~of~~script~~~~~~~~~~#
