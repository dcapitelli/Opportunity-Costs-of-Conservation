import arcpy
from arcpy.sa import *
from arcpy import env  

arcpy.env.overwriteOutput = True
arcpy.CheckOutExtension("Spatial")
arcpy.env.snapRaster = "Z:/arcpy_files/EULandClass/Nov23_EU_landSystem.tif" # add the raster to snap to here
arcpy.env.workspace = "Z:/arcpy_files"

##reproject raster first then resample

cell_size_degrees = 0.0174532925199433
cell_size_meters = 1000
# arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("ETRS 1989")
arcpy.env.extent = "Z:/arcpy_files/EULandClass/Nov23_EU_landSystem.tif"  


## Constant file paths
IN_mask_polygon_file = "Z:/arcpy_files/reference_vector/feb_24_reference_vector_buffer.shp"
IN_coordinate_system_path = "Z :/arcpy_files/reference_vector/feb_24_reference_vector_buffer.prj"


## General settings ready ##


raster_name = 'whea'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'rice'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'maiz'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'barl'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'pmil'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'smil'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'sorg'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'ocer'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'pota'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'swpo'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'yams'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'bean'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'chic'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'cowp'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'pige'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'lent'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'opul'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'soyb'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'grou'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'cnut'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'oilp'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'sunf'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'rape'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'sesa'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'ooil'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'sugc'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'sugb'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'cott'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'ofib'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'toba'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'bana'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'trof'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'temf'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'vege'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################

raster_name = 'rest'


IN_raster_MapSpam_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
OUT_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam/prjsmp_clip_{}_kg_ha.tif".format(raster_name)

outExtractByMask = ExtractByMask(IN_raster_MapSpam_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(OUT_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(OUT_raster_clipped_path))
print(" ")
