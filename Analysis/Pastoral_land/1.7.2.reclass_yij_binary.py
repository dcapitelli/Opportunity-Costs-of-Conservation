
import rasterio as rio
import numpy as np


grass_yij_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/grass_proportional_allocation_equation/grass_newLULC__yij_allocation_gridded.tif"

with rio.open(grass_yij_path) as src:    
    # Read as numpy array
    array = src.read()
    profile = src.profile

    # Reclassify: NaN < 210, NaN >230, 230> 1 >210
    array[np.where(array < 0)] = np.nan 
    array[np.where(array >= 0)] = 1
    
    # and so on ...  

grass_yij_binary_filepath = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/reference_layers/mar24_grass_yield_binary_mask.tif"
with rio.open(grass_yij_binary_filepath, 'w', **profile) as dst:
    # Write to disk
    dst.write(array)

print("grass yij binary mask reclassification successful")
print(f"         available at ...  {grass_yij_binary_filepath}")


with rio.open(grass_yij_path) as src:    
    # Read as numpy array
    array = src.read()
    profile = src.profile

    # Reclassify: NaN < 210, NaN >230, 230> 1 >210
    array[np.where(array < 0)] = np.nan 

    
    # and so on ...  

grass_yij_binary_filepath = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/grass_proportional_allocation_equation/mar24_grass_yield_reclass_no_inf.tif"
with rio.open(grass_yij_binary_filepath, 'w', **profile) as dst:
    # Write to disk
    dst.write(array)