
import rasterio as rio
import numpy as np


crop_yij_path = "c:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_proportional_allocation_equation/feb24_crop_yij_allocation_gridded_cleaned_1.1.tif"

with rio.open(crop_yij_path) as src:    
    # Read as numpy array
    array = src.read()
    profile = src.profile

    # Reclassify: NaN < 210, NaN >230, 230> 1 >210
    array[np.where(array < 0)] = np.nan 
    array[np.where(array >= 0)] = 1
    
    # and so on ...  

crop_yij_binary_filepath = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/reference_layers/feb24_crop_yield_binary_mask.tif"
with rio.open(crop_yij_binary_filepath, 'w', **profile) as dst:
    # Write to disk
    dst.write(array)

print("Crop yij binary mask reclassification successful")
print(f"         available at ...  {crop_yij_binary_filepath}")