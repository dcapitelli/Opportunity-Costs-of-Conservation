import pandas as pd
import rasterio
import rasterstats

# Import the rasterstats package
import rasterstats

# Extract the nearest value in the raster for all mining sites
vegetation_raster = "central_africa_vegetation_map_foraf.tif"
mining_sites['vegetation'] = rasterstats.point_query(mining_sites.geometry, vegetation_raster, interpolate='nearest')
print(mining_sites.head())

# Replace numeric vegation types codes with description
mining_sites['vegetation'] = mining_sites['vegetation'].replace(vegetation_types)

# Make a plot indicating the vegetation type
mining_sites.plot(column='vegetation', legend=True)
plt.show()


# Implementation of lesson into NaturaConnect code
eu_nuts0['sum_crop_yield'] = rasterstats.zonal_stats(eu_nuts0.geometry, crop_yield_raster, stats=['sum'])
eu_nuts0['sum_crop_cells'] = rasterstats.zonal_stats(eu_nuts0.geometry, crop_yield_raster, stats=['count'])
eu_nuts0['sum_reclulc_crop'] = rasterstats.zonal_stats(eu_nuts0.geometry, reclulc_cropland_raster, stats=['sum'])

# 'sum_crop_cells' should equal 'sum_reclulc_crop'
eu_nuts0['check_cell'] = eu_nuts0['sum_crop_cells'] - eu_nuts0['sum_reclulc_crop']
print(eu_nuts0['check_cell'].sum())
print("printed value should = 0:" eu_nuts0['check_cell'].sum())

eu_nuts0['mean_crop_yield'] = eu_nuts0['sum_crop_yield'] / eu_nuts0['sum_reclulc_crop']

