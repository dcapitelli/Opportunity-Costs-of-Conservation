
############################################################
## Aggregate the crop rasters                             ##
############################################################

import rasterio
from rasterio.plot import show
import numpy as np
import matplotlib.pyplot as plt

 # Open invoerrasters
 # raster1_pad = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/qgis_JRC_Forest_yield_1km.tif"
 # raster2_pad = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/eu_nuts0_for_rents_prices_rast.tif"


 # real run
whea_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_whea_price_biomass_euro_kg_ha.tif"
rice_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_rice_price_biomass_euro_kg_ha.tif"
maiz_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_maiz_price_biomass_euro_kg_ha.tif"
barl_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_barl_price_biomass_euro_kg_ha.tif"
pmil_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_pmil_price_biomass_euro_kg_ha.tif"
smil_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_smil_price_biomass_euro_kg_ha.tif"
sorg_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_sorg_price_biomass_euro_kg_ha.tif"
ocer_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_ocer_price_biomass_euro_kg_ha.tif"
pota_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_pota_price_biomass_euro_kg_ha.tif"
swpo_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_swpo_price_biomass_euro_kg_ha.tif"
yams_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_yams_price_biomass_euro_kg_ha.tif"
bean_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_bean_price_biomass_euro_kg_ha.tif"
chic_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_chic_price_biomass_euro_kg_ha.tif"
cowp_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_cowp_price_biomass_euro_kg_ha.tif"
pige_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_pige_price_biomass_euro_kg_ha.tif"
lent_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_lent_price_biomass_euro_kg_ha.tif"
opul_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_opul_price_biomass_euro_kg_ha.tif"
soyb_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_soyb_price_biomass_euro_kg_ha.tif"
grou_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_grou_price_biomass_euro_kg_ha.tif"
cnut_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_cnut_price_biomass_euro_kg_ha.tif"
oilp_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_oilp_price_biomass_euro_kg_ha.tif"
sunf_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_sunf_price_biomass_euro_kg_ha.tif"
rape_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_rape_price_biomass_euro_kg_ha.tif"
sesa_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_sesa_price_biomass_euro_kg_ha.tif"
ooil_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_ooil_price_biomass_euro_kg_ha.tif"
sugc_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_sugc_price_biomass_euro_kg_ha.tif"
sugb_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_sugb_price_biomass_euro_kg_ha.tif"
cott_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_cott_price_biomass_euro_kg_ha.tif"
ofib_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_ofib_price_biomass_euro_kg_ha.tif"
toba_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_toba_price_biomass_euro_kg_ha.tif"
bana_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_bana_price_biomass_euro_kg_ha.tif"
trof_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_trof_price_biomass_euro_kg_ha.tif"
temf_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_temf_price_biomass_euro_kg_ha.tif"
vege_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_vege_price_biomass_euro_kg_ha.tif"
rest_biomass_price_ha_path = r"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_rest_price_biomass_euro_kg_ha.tif"


with rasterio.open(whea_biomass_price_ha_path) as src1, rasterio.open(rice_biomass_price_ha_path) as src2, rasterio.open(maiz_biomass_price_ha_path) as src3, rasterio.open(barl_biomass_price_ha_path) as src4, rasterio.open(pmil_biomass_price_ha_path) as src5, rasterio.open(smil_biomass_price_ha_path) as src6, rasterio.open(sorg_biomass_price_ha_path) as src7, rasterio.open(ocer_biomass_price_ha_path) as src8, rasterio.open(pota_biomass_price_ha_path) as src9, rasterio.open(swpo_biomass_price_ha_path) as src10, rasterio.open(yams_biomass_price_ha_path) as src11, rasterio.open(bean_biomass_price_ha_path) as src12, rasterio.open(chic_biomass_price_ha_path) as src13, rasterio.open(cowp_biomass_price_ha_path) as src14, rasterio.open(pige_biomass_price_ha_path) as src15, rasterio.open(lent_biomass_price_ha_path) as src16, rasterio.open(opul_biomass_price_ha_path) as src17, rasterio.open(soyb_biomass_price_ha_path) as src18, rasterio.open(grou_biomass_price_ha_path) as src19:#, rasterio.open(cnut_biomass_price_ha_path) as src20: #, rasterio.open(oilp_biomass_price_ha_path) as src21, rasterio.open(sunf_biomass_price_ha_path) as src22, rasterio.open(rape_biomass_price_ha_path) as src23, rasterio.open(sesa_biomass_price_ha_path) as src24, rasterio.open(ooil_biomass_price_ha_path) as src25, rasterio.open(sugc_biomass_price_ha_path) as src26, rasterio.open(sugb_biomass_price_ha_path) as src27, rasterio.open(cott_biomass_price_ha_path) as src28, rasterio.open(ofib_biomass_price_ha_path) as src29, rasterio.open(toba_biomass_price_ha_path) as src30, rasterio.open(bana_biomass_price_ha_path) as src31, rasterio.open(trof_biomass_price_ha_path) as src32, rasterio.open(temf_biomass_price_ha_path) as src33, rasterio.open(vege_biomass_price_ha_path) as src34, rasterio.open(rest_biomass_price_ha_path) as src35: 
     # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
     meta = src1.meta.copy()

     # Werk metadata bij voor het uitvoerraster
     meta.update(driver='GTiff', dtype='float32')
     

     # Maak uitvoerrasterbestand aan
     out_rast_calc_crop_biomass_price_ha_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_aggregated_price_biomass_part1_19_ha.tif"
     # out_rast_calc_crop_biomass_price_ha_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/spam_aggregated_price_biomass_part19_35_ha.tif"

     with rasterio.open(out_rast_calc_crop_biomass_price_ha_path, 'w', **meta) as dst:
         # Voer de vermenigvuldiging uit op de invoerrasters
         raster1 = src1.read(1)  # Lees eerste band van raster1
         raster2 = src2.read(1)  # Lees eerste band van raster2
         raster1 = src1.read(1)
         raster2 = src2.read(1)
         raster3 = src3.read(1)
         raster4 = src4.read(1)
         raster5 = src5.read(1)
         raster6 = src6.read(1)
         raster7 = src7.read(1)
         raster8 = src8.read(1)
         raster9 = src9.read(1)
         raster10 = src10.read(1)
         raster11 = src11.read(1)
         raster12 = src12.read(1)
         raster13 = src13.read(1)
         raster14 = src14.read(1)
         raster15 = src15.read(1)
         raster16 = src16.read(1)
         raster17 = src17.read(1)
         raster18 = src18.read(1)
         raster19 = src19.read(1)
         # raster20 = src20.read(1)
         # raster21 = src21.read(1)
         # raster22 = src22.read(1)
         # raster23 = src23.read(1)
         # raster24 = src24.read(1)
         # raster25 = src25.read(1)
         # raster26 = src26.read(1)
         # raster27 = src27.read(1)
         # raster28 = src28.read(1)
         # raster29 = src29.read(1)
         # raster30 = src30.read(1)
         # raster31 = src31.read(1)
         # raster32 = src32.read(1)
         # raster33 = src33.read(1)
         # raster34 = src34.read(1)
         # raster35 = src35.read(1)

         resultaat = raster1  + raster2  + raster3  + raster4  + raster5  + raster6  + raster7  + raster8  + raster9  + raster10 + raster11 + raster12 + raster13 + raster14 + raster15 + raster16 + raster17 + raster18 + raster19 #+ raster20 + raster21 + raster22 + raster23 + raster24 + raster25 + raster26 + raster27 + raster28 + raster29 + raster30 + raster31 + raster32 + raster33 + raster34 + raster35 

         # Schrijf het resultaat naar het uitvoerrasterbestand
         dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band

print(f"Aggregated monetary yield raster has been successfully written and is available at:  {out_rast_calc_crop_biomass_price_ha_path}.")

 # Plot raster
fig, ax = plt.subplots(1, figsize = (10, 10))
show(resultaat, ax = ax)
plt.gca()#.invert_yaxis()
plt.show()

 ##################################
 ## second run for rasters 20-35 ##
 ##################################

with rasterio.open(cnut_biomass_price_ha_path) as src20, rasterio.open(oilp_biomass_price_ha_path) as src21, rasterio.open(sunf_biomass_price_ha_path) as src22, rasterio.open(rape_biomass_price_ha_path) as src23, rasterio.open(sesa_biomass_price_ha_path) as src24, rasterio.open(ooil_biomass_price_ha_path) as src25, rasterio.open(sugc_biomass_price_ha_path) as src26, rasterio.open(sugb_biomass_price_ha_path) as src27, rasterio.open(cott_biomass_price_ha_path) as src28, rasterio.open(ofib_biomass_price_ha_path) as src29, rasterio.open(toba_biomass_price_ha_path) as src30, rasterio.open(bana_biomass_price_ha_path) as src31, rasterio.open(trof_biomass_price_ha_path) as src32, rasterio.open(temf_biomass_price_ha_path) as src33, rasterio.open(vege_biomass_price_ha_path) as src34, rasterio.open(rest_biomass_price_ha_path) as src35: 
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()
    
    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')


    # Maak uitvoerrasterbestand aan
    # out_rast_calc_crop_biomass_price_ha_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/spam_aggregated_price_biomass_part1_18_ha.tif"
    out_rast_calc_crop_biomass_price_ha_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_aggregated_price_biomass_part20_35_ha.tif"

    with rasterio.open(out_rast_calc_crop_biomass_price_ha_path, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster20 = src20.read(1)
        raster21 = src21.read(1)
        raster22 = src22.read(1)
        raster23 = src23.read(1)
        raster24 = src24.read(1)
        raster25 = src25.read(1)
        raster26 = src26.read(1)
        raster27 = src27.read(1)
        raster28 = src28.read(1)
        raster29 = src29.read(1)
        raster30 = src30.read(1)
        raster31 = src31.read(1)
        raster32 = src32.read(1)
        raster33 = src33.read(1)
        raster34 = src34.read(1)
        raster35 = src35.read(1)

        resultaat = raster20 + raster21 + raster22 + raster23 + raster24 + raster25 + raster26 + raster27 + raster28 + raster29 + raster30 + raster31 + raster32 + raster33 + raster34 + raster35 

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band

print(f"Aggregated monetary yield raster has been successfully written and is available at:  {out_rast_calc_crop_biomass_price_ha_path}.")

 # Plot raster
fig, ax = plt.subplots(1, figsize = (10, 10))
show(resultaat, ax = ax)
plt.gca()#.invert_yaxis()
plt.show()

########################################
## Add two aggregate rasters together ##
########################################

out_rast_calc_crop_biomass_price_ha_path_1_19 = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_aggregated_price_biomass_part1_19_ha.tif"
out_rast_calc_crop_biomass_price_ha_path_20_35 = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_aggregated_price_biomass_part20_35_ha.tif"

with rasterio.open(out_rast_calc_crop_biomass_price_ha_path_1_19) as src1, rasterio.open(out_rast_calc_crop_biomass_price_ha_path_20_35) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()
    
    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')
    
    # Maak uitvoerrasterbestand aan
    # out_rast_calc_crop_biomass_price_ha_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/spam_aggregated_price_biomass_part1_18_ha.tif"
    out_rast_calc_crop_biomass_price_ha_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_aggregated_price_biomass_part1_35_ha.tif"

    with rasterio.open(out_rast_calc_crop_biomass_price_ha_path, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)
        raster2 = src2.read(1)

        resultaat = raster1 + raster2   

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band

print(f"Aggregated monetary yield raster has been successfully written and is available at:  {out_rast_calc_crop_biomass_price_ha_path}.")

# Plot raster
fig, ax = plt.subplots(1, figsize = (10, 10))
show(resultaat, ax = ax)
plt.gca()#.invert_yaxis()
plt.show()


#############################################################
## Divide aggregated euro kg spam maps by crop price count ##
#############################################################


out_rast_calc_crop_biomass_price_ha_1_35_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_aggregated_price_biomass_part1_35_ha.tif"
crop_price_availability_count_path = 'C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/eu_nuts0_crop_price_count_feb24_update_1.1.tif'

with rasterio.open(out_rast_calc_crop_biomass_price_ha_1_35_path) as src1, rasterio.open(crop_price_availability_count_path) as src2:
    # Lees metadata van één invoerraster (ervan uitgaande dat beide rasters dezelfde metadata hebben)
    meta = src1.meta.copy()

    # Werk metadata bij voor het uitvoerraster
    meta.update(driver='GTiff', dtype='float32')

    # Maak uitvoerrasterbestand aan
    out_rast_calc_crop_biomass_price_ha_crop_price_count_path = "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/crop_monetary_yield_eu/feb24_spam_aggregated_price_biomass_by_crop_price_count.tif"

    with rasterio.open(out_rast_calc_crop_biomass_price_ha_crop_price_count_path, 'w', **meta) as dst:
        # Voer de vermenigvuldiging uit op de invoerrasters
        raster1 = src1.read(1)
        raster2 = src2.read(1)

        resultaat = raster1 / raster2   

        # Schrijf het resultaat naar het uitvoerrasterbestand
        dst.write(resultaat, 1)  # Schrijf het resultaat naar de eerste band

print(f"Aggregated monetary yield raster has been successfully written and is available at:  {out_rast_calc_crop_biomass_price_ha_crop_price_count_path}  //.")

# Plot raster
fig, ax = plt.subplots(1, figsize = (10, 10))
show(resultaat, ax = ax)
plt.gca()#.invert_yaxis()
plt.show()
