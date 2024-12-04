import rasterio
from rasterio import features
from rasterio.enums import MergeAlg
from rasterio.plot import show
from numpy import int16

########################################
## Aggregate rasters together ##
########################################

out_rast_calc_livestock_biomass_price_ha_path_catt = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/grass_monetary_yield_eu/glw4_newLULC_catt_price_biomass_euro_heads_ha.tif"
out_rast_calc_livestock_biomass_price_ha_path_shee = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/grass_monetary_yield_eu/glw4_newLULC_shee_price_biomass_euro_heads_ha.tif"
out_rast_calc_livestock_biomass_price_ha_path_goat = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/grass_monetary_yield_eu/glw4_newLULC_goat_price_biomass_euro_heads_ha.tif"


with rasterio.open(out_rast_calc_livestock_biomass_price_ha_path_catt) as src1, rasterio.open(out_rast_calc_livestock_biomass_price_ha_path_shee) as src2, rasterio.open(out_rast_calc_livestock_biomass_price_ha_path_goat) as src3:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()
    
    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')
    
    # Maak uitvoerrasterbestand aan
    out_rast_calc_grass_biomass_price_ha_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/grass_monetary_yield_eu/glw4_newLULC_agg_price_biomass_euro_heads_ha.tif"

    with rasterio.open(out_rast_calc_grass_biomass_price_ha_path, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)
        raster2 = src2.read(1)
        raster3 = src3.read(1)

        resultaat = raster1 + raster2 + raster3  

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band

print(f"Aggregated monetary yield raster has been successfully written and is available at:  {out_rast_calc_grass_biomass_price_ha_path}.")



#############################################################
## Divide aggregated euro kg spam maps by crop price count ##
#############################################################


livestock_price_availability_count_path = r'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/mar24_eu_nuts0_livestock_price_count.tif'

with rasterio.open(out_rast_calc_grass_biomass_price_ha_path) as src1, rasterio.open(livestock_price_availability_count_path) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')

    # Maak uitvoerrasterbestand aan 
    out_rast_calc_livestock_biomass_price_ha_livestock_price_count_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/grass_monetary_yield_eu/glw4_newLULC_averaged_price_biomass_by_livestock_price_count.tif"

    with rasterio.open(out_rast_calc_livestock_biomass_price_ha_livestock_price_count_path, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)
        raster2 = src2.read(1)

        resultaat = raster1 / raster2   

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band

print(f"Aggregated monetary yield raster has been successfully written and is available at: ...  {out_rast_calc_livestock_biomass_price_ha_livestock_price_count_path}  .")



print("#~~~~~End~~of~~script~~~~~~~#")