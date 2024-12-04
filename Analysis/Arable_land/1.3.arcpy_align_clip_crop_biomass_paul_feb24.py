# Thanks to Paul for helping me make this script

# Check file paths before running

import arcpy
from arcpy.sa import *
from arcpy import env  

arcpy.env.overwriteOutput = True
arcpy.CheckOutExtension("Spatial")
arcpy.env.snapRaster = "Z:/arcpy_files/NewLandUse/Nov23_EU_landSystem.tif" # add the raster to snap to here
arcpy.env.workspace = "Z:/arcpy_files"

##reproject raster first then resample

# print("where I used: projection = arcpy.SpatialReference('ETRS 1989')")
# print("and : arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, 'NEAREST')")
print("arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, 'BILINEAR')")
# print("IN_mask_polygon_file = Z:/arcpy_files/ReferenceVector/reference_vector_feb_24.shp") 
print("Here I changed the IN_coordinate_system_path to the Z :/arcpy_files/ReferenceVector/reference_vector_feb_24.prj")

cell_size_degrees = 0.0174532925199433
cell_size_meters = 1000
# projection = arcpy.SpatialReference("ETRS 1989")
projection = arcpy.SpatialReference(3035)
# arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("ETRS 1989")
arcpy.env.extent = "Z:/arcpy_files/NewLandUse/Nov23_EU_landSystem.tif"  


## Constant file paths
IN_mask_polygon_file = "Z:/arcpy_files/ReferenceVector/reference_vector_feb_24.shp"
# IN_coordinate_system_path = "Z :/arcpy_files/ReferenceVector/reference_vector_feb_24.prj" #wanted to use same file for coor sys but got ERROR 000628: Cannot set input into parameter out_coor_system.


# General settings ready ##


raster_name = 'whea'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'rice'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'maiz'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'barl'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'pmil'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'smil'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'sorg'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'ocer'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'pota'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'swpo'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'yams'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'bean'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'chic'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'cowp'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'pige'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'lent'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'opul'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'soyb'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'grou'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'cnut'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'oilp'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'sunf'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'rape'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'sesa'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'ooil'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'sugc'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'sugb'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'cott'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'ofib'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'toba'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'bana'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'trof'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'temf'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)
in_raster_reproj_path_previousFeb = "Z:/arcpy_files/eu_crop_biomass_yield/clip_eu_spam_feb_24/feb24_clip_eu_spam_{}_kg_ha.tif".format(raster_name)
in_raster_reproj_path_QGIS = "Z:/arcpy_files/eu_crop_biomass_yield/clip_eu_spam_feb_24/feb24_clip_eu_spam_{}_kg_ha_QGIS.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'vege'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")

########################
## repeatable section ##
########################


raster_name = 'rest'.upper()

in_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/world_spam/spam2010V2r0_global_Y_{}_A.tif".format(raster_name)

raster_name = raster_name.lower()

out_raster_reproj_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_spam_feb24/feb24_reprojected_{}_kg_ha.tif".format(raster_name)
out_raster_reproj_file = 'reprojected_{}_kg_ha.tif'.format(raster_name)

arcpy.ProjectRaster_management(in_raster_reproj_path, out_raster_reproj_path, projection, "NEAREST") #reproject your raster here

in_raster_resample_path = out_raster_reproj_path
out_raster_resample_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_and_resampled_spam_feb24/feb24_reproj_resampled_{}_kg_ha.tif".format(raster_name)
arcpy.management.Resample(in_raster_resample_path, out_raster_resample_path, cell_size_meters, "BILINEAR")

out_raster_clipped_path = "Z:/arcpy_files/eu_crop_biomass_yield/reprojected_resampled_clipped_spam_feb24/feb24_prjsmp_world_clip_{}_kg_ha.tif".format(raster_name)
outExtractByMask = ExtractByMask(out_raster_resample_path, IN_mask_polygon_file) #extract by mask
outExtractByMask.save(out_raster_clipped_path)

print("{} snap successful".format(raster_name))
print(" ")
print("reprojected, resampled, and clipped spam file available at {} ".format(out_raster_clipped_path))
print(" ")


#################################
## repeatable section finished ##
#################################


print(" ")
print("User_DJS, now you need to compress the reprojected_resampled_clipped_spam folder")
print("and send it to your personal drive and add the files to a suitable folder ")
print("then add the file paths into the next script")
print("#~~~~~~~~~End~~of~~script~~~~~~~~~~#")
#~~~~~~~~~End~~of~~script~~~~~~~~~~#