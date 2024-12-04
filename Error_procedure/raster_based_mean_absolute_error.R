# raster zone based mean absolute error

print(crop_mean_abs_error)
#[1] 1.744701e-05
print(live_mean_abs_error_2)
# [1] 1.390163e-05
print(for_mean_abs_error)
#[1] 4.651639e-06


library(raster)
library(sf)
library(exactextractr)
library(terra)


input_rent_forestry <- "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/mar24_eu_nuts0_for_rasterize_rents.tif"
output_rent_forestry <- "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/rasterized_land_rents/mar24_for_allocated_rents.tif"

output_forestry <- rast(output_rent_forestry)
input_forestry <- rast(input_rent_forestry)

z <- input_forestry
r <- output_forestry

zonal_hope <- zonal(r, z, mean, na.rm=TRUE)
forestry_zonal_calc <- zonal_hope

forestry_zonal_calc$abs_error <- abs(forestry_zonal_calc$mar24_for_allocated_rents - forestry_zonal_calc$mar24_eu_nuts0_for_rasterize_rents)

forestry_zonal_calc <- forestry_zonal_calc[-c(1, 2), ]

for_mean_abs_error <- mean(forestry_zonal_calc$abs_error)

forestry_zonal_calc$Index <- seq_len(nrow(forestry_zonal_calc))

print(for_mean_abs_error)
#[1] 4.651639e-06


f <-ggplot(data = forestry_zonal_calc, aes(x = Index, y = abs_error)) +
  geom_point(alpha=0.2)+ 
  theme(legend.position="none")+
  # geom_text(aes(label = column2, alpha = 0.3), vjust = -1, hjust = 0.5)+
  labs(x = "Index", y = "MAE")

f




input_rent_crop <- "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/rasterized_land_rents/crop_mj_rents_feb_24.tif"
output_rent_crop <- "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/rasterized_land_rents/feb24_crop_allocated_rents_TEST3__.tif"

output_crop <- rast(output_rent_crop)
input_crop <- rast(input_rent_crop)

z <- input_crop
r <- output_crop

crop_zonal_calc <- zonal(r, z, mean, na.rm=TRUE)
nan_index <- which(is.nan(crop_zonal_calc$feb24_crop_allocated_rents_TEST3__))

crop_zonal_calc$abs_error <- abs(crop_zonal_calc$feb24_crop_allocated_rents_TEST3__ - crop_zonal_calc$crop_mj_rents_feb_24)


crop_mean_abs_error <- mean(crop_zonal_calc$abs_error[-nan_index])

crop_zonal_calc$Index <- seq_len(nrow(crop_zonal_calc))

print(crop_mean_abs_error)
#[1] 1.744701e-05


q <-ggplot(data = crop_zonal_calc, aes(x = Index, y = abs_error)) +
  geom_point(alpha=0.2)+ 
  theme(legend.position="none")+
  # geom_text(aes(label = column2, alpha = 0.3), vjust = -1, hjust = 0.5)+
  labs(x = "Index", y = "MAE")

q



input_rent_livestock <- "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/rasterized_land_rents/grass_mj_rents_feb_24.tif"
output_rent_livestock <- "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/rasterized_land_rents/mar24_grass_allocated_rents.tif"
output_rent_livestock_2 <- "C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Throughput_datasets/rasterized_land_rents/jun24_MAE_grass_allocated_rents.tif"

output_live_2 <- rast(output_rent_livestock_2)
output_live <- rast(output_rent_livestock)
input_live <- rast(input_rent_livestock)

z <- input_live
r <- output_live
r2 <- output_live_2

live_zonal_calc <- zonal(r, z, mean, na.rm=TRUE)

live_zonal_calc_2 <- zonal(r2, z, mean, na.rm=TRUE)
live_zonal_calc_2$abs_error <- abs(live_zonal_calc_2$jun24_MAE_grass_allocated_rents - live_zonal_calc_2$grass_mj_rents_feb_24)
nan_index <- which(is.nan(live_zonal_calc_2$abs_error))
live_mean_abs_error_2 <- mean(live_zonal_calc_2$abs_error[-nan_index])
print(live_mean_abs_error_2)
# [1] 1.390163e-05

live_zonal_calc$abs_error <- abs(live_zonal_calc$mar24_grass_allocated_rents - live_zonal_calc$grass_mj_rents_feb_24)

nan_index <- which(is.nan(live_zonal_calc$abs_error))

live_mean_abs_error <- mean(live_zonal_calc$abs_error[-nan_index])

print(live_mean_abs_error)
#[1] 0.3071117

live_zonal_calc$Index <- seq_len(nrow(live_zonal_calc))
live_zonal_calc_2$Index <- seq_len(nrow(live_zonal_calc_2))
p <-ggplot(data = live_zonal_calc_2, aes(x = Index, y = abs_error)) +
  geom_point(alpha=0.2)+ 
  theme(legend.position="none")+
  # geom_text(aes(label = column2, alpha = 0.3), vjust = -1, hjust = 0.5)+
  labs(x = "Index", y = "MAE")

p

