
library(ggplot2)
library(ggpubr)
library(ggrepel)
library(dplyr)

d_urban_rent <- read.csv("C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/rent_population_per_hectare_europe.csv")

x <- d_urban_rent$Population_hectare
y <- d_urban_rent$Rent_ha
z <- d_urban_rent$City
r <- d_urban_rent$EU_region

d_urban_rent$log_x <- log(d_urban_rent$Population_hectare)
d_urban_rent$log_y <- log(d_urban_rent$Rent_ha)

## regions defined as by Dou et al.
south_eu <- list("IT", "ES", "EL","MT","CY","PT")
west_eu <- list("BE","LU","FR", "NL", "UK", "IE","DE","CH","AT")
north_eu <- list("FI", "DK","SE","NO")
east_eu <- list("LV","EE","LT","HU","SK", "BG", "RO","CZ","PL","SI", "AL","BH","HR","KO","ME","MK","RS")

d_urban_rent$EU_region = "hi"
d_urban_rent <- d_urban_rent %>%
  mutate(EU_region = case_when(Country %in% south_eu ~ "South",
                               Country %in% west_eu ~ "West",
                               Country %in% north_eu ~ "North",
                               Country %in% east_eu ~ "East"))

dsouth <- subset(d_urban_rent, EU_region =="South")
dwest <- subset(d_urban_rent, EU_region == "West")
dnorth <- subset(d_urban_rent, EU_region == "North")
deast <- subset(d_urban_rent, EU_region == "East")



library(dplyr)

# Fit a linear model to the entire data
model <- lm(log_y ~ log_x + d_urban_rent$EU_region, data = d_urban_rent)

# Extract the coefficients for the slope and intercept
coefficients <- coef(model)
slope_log_x <- coefficients["log_x"]

# Create a dataframe for slopes by region (z) for annotation
# We use `dplyr` to group by region and fit a model for each region separately
slopes_by_region <- d_urban_rent %>%
  group_by(d_urban_rent$EU_region) %>%
  do({
    model <- lm(log_y ~ log_x, data = .)  # Fit the linear model per region
    tibble(slope = coef(model)["log_x"])  # Extract the slope for log_x
  })

# Add predictions from the model for plotting
d_urban_rent <- d_urban_rent %>%
  mutate(fitted = predict(model))

# Create the ggplot
ggplot(d_urban_rent, aes(x = log_x, y = log_y, color = z)) +
  geom_point(alpha = 0.7, size = 2) +  # Scatterplot points
  geom_smooth(method = "lm", se = FALSE, aes(group = d_urban_rent$EU_region)) +  # Regression lines per group
  labs(
    title = "Fixed-Effects Model: Log-Transformed Rent Relationship by Region",
    x = "Log of Predictor (log_x)",
    y = "Log of Response (log_y)",
    color = "Region"
  ) +
  theme_minimal() +
  theme(legend.position = "top") +
  # Annotating slopes for each region in the plot
  # geom_text(data = slopes_by_region, 
            # aes(x = max(d_urban_rent$log_x), 
            #     y = max(d_urban_rent$log_y) - 1,  # Adjust position for label
            #     label = paste("Slope (", z, "): ", round(slope, 2), sep = "")),
            # color = "black", size = 4, hjust = 1, vjust = 1)  # Positioning labels
  
  
# -----------------------------------------------------------------

# November 2024 redoing the log_rent and log population density +Eu region 

# Assuming you have your data and the necessary libraries loaded:
library(ggplot2)
library(dplyr)

# Fit a linear model with fixed effects (assuming 'log_x' is the independent variable and 'log_y' is the dependent variable)
# If you want to include 'z' (the region) as a fixed effect:
z <- d_urban_rent$EU_region
lm_model <- lm(log_y ~ log_x + z, data = d_urban_rent)

# Summary of the model to get the coefficients
summary(lm_model)


# Extract coefficients from the model
intercept <- 8.33318
slope <- 1.05445
intercepts <- c(North = intercept + 0.77811,
                South = intercept + 0.25687,
                West = intercept + 0.61754,
                East = intercept#,
               # Default = intercept
               )  # Default intercept
# Prepare equations as a data frame for annotations
equations <- data.frame(
  z = names(intercepts),
  intercept = intercepts,
  equation = paste0("log_y = ", round(slope, 2), " * log_x + ", round(intercepts, 2))
)


# Add predicted values to the dataset
d_urban_rent <- d_urban_rent %>%
  mutate(predicted = case_when(
    z == "North" ~ intercepts["North"] + slope * log_x,
    z == "South" ~ intercepts["South"] + slope * log_x,
    z == "West" ~ intercepts["West"] + slope * log_x,
    z == "East"  ~ intercepts["East"] + slope * log_x #,
   # TRUE ~ intercept + slope * log_x  # Default for other cases
  ))


# Create the plot
log_xy_plus_region <- ggplot(d_urban_rent, aes(x = log_x, y = log_y, color = z)) +
  geom_point(size = 2, alpha = 0.7) +  # Scatterplot points
  geom_abline(aes(slope = slope, intercept = intercepts[z], color = z),
              data = unique(d_urban_rent), size = 1) +  # Parallel lines per group
  # geom_text(data = equations, 
            # aes(x = max(d_urban_rent$log_x), y = max(d_urban_rent$log_y) - seq(0, 1.5, length.out = nrow(equations)), 
                # label = equation, color = z),
            # hjust = 3.5, size = 3, show.legend = FALSE) +  # Add equations to the plot
  labs(
    title = "Log rent ~ Log population density + EU region",
    x = "Log rent (euros per hectare)",
    y = "Log population density (people per hectare)",
    color = "EU region (z)"
  ) +
  theme_minimal() +
  theme(legend.position = "top")

# Print the plot
log_xy_plus_region

# save the dataset
write.csv(d_urban_rent,"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Cartographs/Paper figures/UrbanRentPopulationModel/UrbanRentPopulationModel.csv")

# save the plot
ggsave("C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Cartographs/Paper figures/UrbanRentPopulationModel/UrbanRentPopulationModel.png",log_xy_plus_region, width = 4.5, height = 4.5)



# -----------------------------------------------------------------
# explore the spatial origin of the dots
plot_rent_pop_eu_point <- ggplot(data = d, aes(x = x, y = y))+
  geom_point( aes(size=4,shape=r, color=r, alpha=0.5))+
  theme(legend.position = "right")+
  theme(axis.title.x = element_text(size = 16))+
  theme(axis.title.y = element_text(size = 16))+
  # scale_x_continuous(trans = "log10")+
  ylab("Renting price (euros per hectare)")+
  xlab("Population density (heads per hectare)")

plot_rent_pop_eu_point

###

col <-  wes_palette("Zissou1")

plot_pop_rent_eu_legend <- ggplot(data = d, aes(x=x, y=y, color= factor(z)))+
  geom_point(size=3, shape=19)+
  geom_label_repel(aes(label = z),
                   box.padding   = 0.35, 
                   point.padding = 0.5,
                   segment.color = 'grey50') +
  theme(legend.position = "none")+
  theme(axis.title.x = element_text(size = 16))+
  theme(axis.title.y = element_text(size = 16))+
  # guides(fill=guide_legend(title="City"))+
  # geom_text(hjust=0, vjust=0)+
  scale_x_continuous(trans = 'log10')+
  ylab("Rent (euros per hectare)")+
  xlab("Population density (heads per hectare)")
plot_pop_rent_eu_legend 

ggsave("C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/rent_population_per_hectare_europe_label_log10_reverse_axis.png",
       plot_pop_rent_eu_legend, width = 10, height = 10)

plot_pop_rent_eu <- ggplot(data = d, aes(x = x, y= y))+
  geom_point()+
  ylab("Rent (euros per hectare)")+
  xlab("Population density (per hectare)")+
  geom_smooth(method=lm, se=TRUE)+
  stat_regline_equation(label.y = 450000, aes(label = after_stat(eq.label))) +
  stat_regline_equation(label.y = 410000, aes(label = ..adj.rr.label..))

  # theme(legend.position = "right")+
  # theme(legend.title = element_text("City"))

plot_pop_rent_eu

ggsave("C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/rent_population_per_hectare_europe_popX_rentY.png",
       plot_pop_rent_eu, width = 4, height = 4)


#fit linear regression model to dataset and view model summary
model <- lm(y~x, data=d)
summary(model)

# Call:
#   lm(formula = y ~ x, data = d)
# 
# Residuals:
#   Min      1Q    Median      3Q     Max
# -21.210  -3.999  -0.633   2.910  41.106
# 
# Coefficients:
#               Estimate Std. Error t value Pr(>|t|)
# (Intercept) 3.474e+00  2.317e+00   1.499    0.142
# x           1.148e-04  1.078e-05  10.648 3.06e-13 ***
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Residual standard error: 9.769 on 40 degrees of freedom
# Multiple R-squared:  0.7392,	Adjusted R-squared:  0.7327
# F-statistic: 113.4 on 1 and 40 DF,  p-value: 3.059e-13



## fit linear regression model to EU region dataset

## South
x <- dsouth$Population_hectare
y <- dsouth$Rent_ha

plot_south <- ggplot(data= dsouth, aes(x=dsouth$Population_hectare, y=dsouth$Rent_ha))+
  geom_point()+
  ylab(element_blank())+
  xlab(element_blank())+
  xlim(0, 50)+
  # ylab("Rent (euros per hectare)")+
  # xlab("Population density (per hectare)")+
  geom_smooth(method=lm, se=TRUE)+
  stat_regline_equation(label.y = 200000, aes(label = after_stat(eq.label))) +
  stat_regline_equation(label.y = 255000, aes(label = ..adj.rr.label..))+
  ggtitle("Southern Europe")
plot_south

model <- lm(y~x, data=dsouth)
summary(model)

# Call:
#   lm(formula = y ~ x, data = dsouth)
# 
# Residuals:
#   9     17     18     24     25     32     36 
# -23480   8200  10457  12370 -23120  -4387  19960 
# 
# Coefficients:
#               Estimate Std.Error t value Pr(>|t|)    
# (Intercept)  -3794.4    13975.0  -0.272 0.796851    
# x             6635.1      609.4  10.888 0.000114 ***
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Residual standard error: 19150 on 5 degrees of freedom
# Multiple R-squared:  0.9595,	Adjusted R-squared:  0.9514 
# F-statistic: 118.5 on 1 and 5 DF,  p-value: 0.0001135

## East
x <- deast$Population_hectare
y <- deast$Rent_ha

plot_east <- ggplot(data= deast, aes(x=deast$Population_hectare, y=deast$Rent_ha))+
  geom_point()+
  ylab(element_blank())+
  xlab(element_blank())+
  # ylab("Rent (euros per hectare)")+
  # xlab("Population density (per hectare)")+
  geom_smooth(method=lm, se=TRUE)+
  stat_regline_equation(label.y = 300000, aes(label = after_stat(eq.label))) +
  stat_regline_equation(label.y = 350000, aes(label = ..adj.rr.label..))+
  ggtitle("Eastern Europe")
plot_east

model <- lm(y~x, data=deast)
summary(model)

# Call:
#   lm(formula = y ~ x, data = deast)
# 
# Residuals:
#   Min     1Q Median     3Q    Max 
# -25262 -14417  -2619   4382  41751 
# 
# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
# (Intercept)    10374       6619   1.567    0.138    
# x               4475        240  18.645 8.69e-12 ***
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Residual standard error: 19690 on 15 degrees of freedom
# Multiple R-squared:  0.9586,	Adjusted R-squared:  0.9559 
# F-statistic: 347.7 on 1 and 15 DF,  p-value: 8.694e-12

## West
x <- dwest$Population_hectare
y <- dwest$Rent_ha

plot_west <- ggplot(data= dwest, aes(x=dwest$Population_hectare, y=dwest$Rent_ha))+
  geom_point()+
  ylab(element_blank())+
  xlab(element_blank())+
  # ylab("Rent (euros per hectare)")+
  # xlab("Population density (per hectare)")+
  geom_smooth(method=lm, se=TRUE)+
  stat_regline_equation(label.y = 500000, aes(label = after_stat(eq.label))) +
  stat_regline_equation(label.y = 555000, aes(label = ..adj.rr.label..))+
  ggtitle("Western Europe")
plot_west

model <- lm(y~x, data=dwest)
summary(model)

# Call:
#   lm(formula = y ~ x, data = dwest)
# 
# Residuals:
#   Min      1Q  Median      3Q     Max 
# -139887  -49000   -6335   55181  135685 
# 
# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
# (Intercept)    52042      39396   1.321    0.211    
# x               7332       1116   6.572 2.64e-05 ***
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Residual standard error: 83060 on 12 degrees of freedom
# Multiple R-squared:  0.7826,	Adjusted R-squared:  0.7645 
# F-statistic: 43.19 on 1 and 12 DF,  p-value: 2.643e-05

## North
x <- dnorth$Population_hectare
y <- dnorth$Rent_ha

plot_north <- ggplot(data= dnorth, aes(x=dnorth$Population_hectare, y=dnorth$Rent_ha))+
  geom_point()+
  ylab(element_blank())+
  xlab(element_blank())+
  # ylab("Rent (euros per hectare)")+
  # xlab("Population density (per hectare)")+
  geom_smooth(method=lm, se=TRUE)+
  stat_regline_equation(label.y = 223000, aes(label = after_stat(eq.label))) +
  stat_regline_equation(label.y = 255000, aes(label = ..adj.rr.label..))+
  ggtitle("Northern Europe")
plot_north

model <- lm(y~x, data=dnorth)
summary(model)

# Call:
#   lm(formula = y ~ x, data = dnorth)
# 
# Residuals:
#   15       19       34       38 
# 7316.74 -1784.90   -16.23 -5515.60 
# 
# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)   
# (Intercept)  29682.9     6717.3   4.419  0.04759 * 
#   x             8019.2      374.1  21.437  0.00217 **
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Residual standard error: 6601 on 2 degrees of freedom
# Multiple R-squared:  0.9957,	Adjusted R-squared:  0.9935 
# F-statistic: 459.6 on 1 and 2 DF,  p-value: 0.002169


# General model with main effects

x <- d$Population_hectare
y <- d$Rent_ha
z <- d$EU_region


model_x <- lm(y~x, data = d)
summary_model_x <- summary(model_x)

model_x_plus_region <- lm(y~x + z, data = d)
summary_model_x_plus_region <- summary(model_x_plus_region)

model_x_times_region <- lm(y~x * z, data = d)
summary_model_x_times_region <- summary(model_x_times_region)

log_x <- log(x)
model_log_x <- lm(y~log_x, data = d)
summary_model_log_x <- summary(model_log_x)

model_log_x_plus_region <- lm(y~log_x + z, data = d)
summary_model_log_x_plus_region <- summary(model_log_x_plus_region)

model_log_x_times_region <- lm(y~log_x * z, data = d)
summary_model_log_x_times_region <- summary(model_log_x_times_region)

log_y <- log(y)
model_log_y <- lm(log_y~x, data = d)
summary_model_log_y <- summary(model_log_y)

model_log_y_plus_region <- lm(log_y~x + z, data = d)
summary_model_log_y_plus_region <- summary(model_log_y_plus_region)

model_log_y_times_region <- lm(log_y~x * z, data = d)
summary_model_log_y_times_region <- summary(model_log_y_times_region)


model_log_xy <- lm(log_y~log_x, data = d)
summary_model_log_xy <- summary(model_log_xy)

# model_log_xy_plus_region <- lm(log_y~log_x + z, data = d)
model_log_xy_plus_region <- lm(log(Rent_ha)~ log(Population_hectare) + EU_region, data = d_urban_rent)

summary_model_log_xy_plus_region <- summary(model_log_xy_plus_region)

model_log_xy_times_region <- lm(log_y~log_x * z, data = d)
summary_model_log_xy_times_region <- summary(model_log_xy_times_region)

# Model selection using AIC and BIC
require(broom)

AIC_BIC_x <- glance(model_x)
AIC_BIC_x_plus_region <- glance(model_x_plus_region)
AIC_BIC_x_times_region <- glance(model_x_times_region)

AIC_BIC_log_x <- glance(model_log_x)
AIC_BIC_log_x_plus_region <- glance(model_log_x_plus_region)
AIC_BIC_log_x_times_region <- glance(model_log_x_times_region)

AIC_BIC_log_y <- glance(model_log_y)
AIC_BIC_log_y_plus_region <- glance(model_log_y_plus_region)
AIC_BIC_log_y_times_region <- glance(model_log_y_times_region)

AIC_BIC_log_xy <- glance(model_log_xy)
AIC_BIC_log_xy_plus_region <- glance(model_log_xy_plus_region)
AIC_BIC_log_xy_times_region <- glance(model_log_xy_times_region)

# Bring together model selection results into a table

AIC_BIC_table_x_logx_logy_logxy <- rbind(AIC_BIC_x, 
                       AIC_BIC_x_plus_region, 
                       AIC_BIC_x_times_region,
                       AIC_BIC_log_x,
                       AIC_BIC_log_x_plus_region,
                       AIC_BIC_log_x_times_region,
                       AIC_BIC_log_y,
                       AIC_BIC_log_y_plus_region,
                       AIC_BIC_log_y_times_region,
                       AIC_BIC_log_xy,
                       AIC_BIC_log_xy_plus_region,
                       AIC_BIC_log_xy_times_region)
AIC_BIC_table_x_logx_logy_logxy$Model <- c("AIC_BIC_x", 
                        "AIC_BIC_x_plus_region", 
                        "AIC_BIC_x_times_region",
                        "AIC_BIC_log_x",
                        "AIC_BIC_log_x_plus_region",
                        "AIC_BIC_log_x_times_region",
                        "AIC_BIC_log_y",
                        "AIC_BIC_log_y_plus_region",
                        "AIC_BIC_log_y_times_region",
                        "AIC_BIC_log_xy",
                        "AIC_BIC_log_xy_plus_region",
                        "AIC_BIC_log_xy_times_region")
library(dplyr)
AIC_BIC_table_x_logx_logy_logxy <- AIC_BIC_table_x_logx_logy_logxy %>% select(Model, everything())

write.csv(AIC_BIC_table_x_logx_logy_logxy,"C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/AIC_BIC_table_x_logx_logy_logxy_model_selection.csv")

# Model selected: AIC_BIC_x_times_region
# r.squared adj.r.squared  sigma  statistic  p.value    df    logLik   AIC   BIC
#      <dbl>         <dbl>  <dbl>     <dbl>     <dbl> - <dbl>  <dbl> <dbl> <dbl>
#      0.890         0.867 51600.      39.2  1.81e-14     7    -511. 1040. 1055.

d$predlm <-  predict(model_x_times_region)
d$predlm_logx <- predict(model_log_x_plus_region)
d$predlm_logy <- predict(model_log_y_plus_region)
d$predlm_logxy <- predict(model_log_xy_plus_region)
d_urban_rent$predlm_logxy <- predict(model_log_xy_plus_region)

d$predlm_logxy <- predict(model_log_xy)


x_times_region <- ggplot(d, aes(x = x, y = y, color = z) ) +
                  geom_point() +
                  geom_line(aes(y = predlm))+
                  ggtitle("Rent ~ Pop * EU_region")+
                  ylab("Rent (euros per hectare)")+
                  xlab("Population density (per hectare)")+
                  stat_regline_equation(label.y = c(200000, 300000, 400000, 500000), aes(label = after_stat(eq.label)))
x_times_region  
ggsave("C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/x_times_region.png",x_times_region, width=5, height=5)

log_x_plus_region <- ggplot(d, aes(x = log_x, y = y, color = z) ) +
                        geom_point() +
                        geom_line(aes(y = predlm_logx))+
                        ggtitle("Rent ~ LogPop + EU_region")+
                        ylab("Rent (euros per hectare)")+
                        xlab("Log Population density (per hectare)")+
                        stat_regline_equation(label.y = c(200000, 300000, 400000, 500000), aes(label = after_stat(eq.label)))
log_x_plus_region 
ggsave("C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/log_x_plus_region.png",log_x_plus_region, width=5, height=5)


log_y_plus_region <- ggplot(d, aes(x = x, y = log_y, color = z) ) +
  geom_point() +
  geom_line(aes(y = predlm_logy))+
  ggtitle("LogRent ~ Pop + EU_region")+
  ylab("Log Rent (euros per hectare)")+
  xlab("Population density (per hectare)")+
  stat_regline_equation(label.y = c(13,14,15,16), aes(label = after_stat(eq.label)))+
  stat_regline_equation(label.y = c(13.4,14.4,15.4,16.4), aes(label = ..adj.rr.label..))
  
log_y_plus_region
ggsave("C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/log_y_plus_region.png",log_y_plus_region, width=5, height=5)

log_xy <- ggplot(d, aes(x = log_x, y = log_y) ) +
  geom_point() +
  geom_line(aes(y = predlm_logxy))+
  ggtitle("LogRent ~ LogPop")+
  ylab("Log Rent (euros per hectare)")+
  xlab("Log Population density (per hectare)")+
  stat_regline_equation(label.y = 13, aes(label = after_stat(eq.label)))+
  stat_regline_equation(label.y = 11, aes(label = ..adj.rr.label..))

log_xy

# required lines before plot
d$predlm_logxy <- predict(model_log_xy_plus_region)

log_xy_plus_region <- ggplot(d, aes(x = log_x, y = log_y, color = z) ) +
  geom_point() +
  geom_line(aes(y = predlm_logxy))+
  ggtitle("LogRent ~ LogPop + EU_region")+
  ylab("Log Rent (euros per hectare)")+
  xlab("Log Population density (per hectare)")+
  stat_regline_equation(label.y = c(11,13,15,17), aes(label = after_stat(eq.label)))+
  stat_regline_equation(label.y = c(11.9,13.9,15.9,17.9), aes(label = ..adj.rr.label..))

log_xy_plus_region

ggsave("C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Cartographs/Paper figures/model_relationship_logRent_logPop_4.png",log_xy_plus_region, width=4, height=4)


# redoing the plot to check that it is correct
log_xy_plus_region <- ggplot(d_urban_rent, aes(x = log_x, y = log_y, color = z)) +
  geom_point() +  # Scatter plot of the data
  geom_smooth(method = "lm", aes(group = EU_region), se = FALSE, linetype = "solid") +  # Separate regression lines for each region
  ggtitle("LogRent ~ LogPop + EU_region") +
  ylab("Log Rent (euros per hectare)") +
  xlab("Log Population density (per hectare)") +
  stat_regline_equation(label.y = c(11, 13, 15, 17), aes(label = after_stat(eq.label))) +  # Show equations for slopes
  stat_regline_equation(label.y = c(11.9, 13.9, 15.9, 17.9), aes(label = ..adj.rr.label..))  # Show adjusted R-squared values

log_xy_plus_region







x_times_region +log_x_plus_region +log_y_plus_region + log_xy_plus_region

library(gridExtra)
top_row_model <- plot_grid(x_times_region,log_x_plus_region, labels = c('', ''))
bottom_row_model <- plot_grid(log_y_plus_region,log_xy_plus_region, labels = c('', ''))
left <- titleGrob("Rent (euros/ha/yr)", rot = 90, gp = gpar(fontsize = 11),debug=FALSE)+
bottom <- titleGrob("Population density (heads/ ha)", gp = gpar(fontsize = 11),debug=FALSE)+
group <- grid.arrange(arrangeGrob(top_row_model, ncol=1, nrow=1),
                        arrangeGrob(bottom_row_model, ncol=1, nrow=1), heights = c(2,2), left="Rent (euros/ha/yr)", bottom = "Population density (heads/ha)")
group
ggsave("C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/regional_eu_pop_rent_four_models.png",group, width=10, height=10)

# Create the residual data frame
res_model_x <- resid(model_x)
res_model_x_plus_region <- resid(model_x_plus_region)
res_model_x_times_region <- resid(model_x_times_region)

res_model_log_x <- resid(model_log_x)
res_model_log_x_plus_region <- resid(model_log_x_plus_region)
res_model_log_x_times_region <- resid(model_log_x_times_region)

res_model_log_y <- resid(model_log_y)
res_model_log_y_plus_region <- resid(model_log_y_plus_region)
res_model_log_y_times_region <- resid(model_log_y_times_region)

res_model_log_xy <- resid(model_log_xy)
res_model_log_xy_plus_region <- resid(model_log_xy_plus_region)
res_model_log_xy_times_region <- resid(model_log_xy_times_region)

# Plot the residuals
res_plot_x <- plot(fitted(model_x),res_model_x)
res_plot_x_plus_region <- plot(fitted(model_x_plus_region),res_model_x_plus_region)
res_plot_x_times_region <- plot(fitted(model_x_times_region),res_model_x_times_region)

res_plot_log_x <- plot(fitted(model_log_x),res_model_log_x)
res_plot_log_x_plus_region <- plot(fitted(model_log_x_plus_region),res_model_log_x_plus_region)
res_plot_log_x_times_region <- plot(fitted(model_log_x_times_region),res_model_log_x_times_region)

res_plot_log_y <- plot(fitted(model_log_y),res_model_log_y)
res_plot_log_y_plus_region <- plot(fitted(model_log_y_plus_region),res_model_log_y_plus_region)
res_plot_log_y_times_region <- plot(fitted(model_log_y_times_region),res_model_log_y_times_region)

res_plot_log_xy <- plot(fitted(model_log_xy),res_model_log_xy)
res_plot_log_xy_plus_region <- plot(fitted(model_log_xy_plus_region),res_model_log_xy_plus_region)
res_plot_log_xy_times_region <- plot(fitted(model_log_xy_times_region),res_model_log_xy_times_region)


res_table <- rbind(res_model_x,
                   res_model_x_plus_region,
                   res_model_x_times_region,
                   res_model_log_x,
                   res_model_log_x_plus_region,
                   res_model_log_x_times_region,
                   res_model_log_y,
                   res_model_log_y_plus_region,
                   res_model_log_y_times_region,
                   res_model_log_xy,
                   res_model_log_xy_plus_region,
                   res_model_log_xy_times_region)


mres_table <- melt(res_table, id=-1)
colnames(mres_table)[1] <- "Model"
colnames(mres_table)[2] <- "Order"
colnames(mres_table)[3] <- "Residuals"


fitted_table <- rbind(fitted(model_x),
                      fitted(model_x_plus_region),
                      fitted(model_x_times_region),
                      fitted(model_log_x),
                      fitted(model_log_x_plus_region),
                      fitted(model_log_x_times_region),
                      fitted(model_log_y),
                      fitted(model_log_y_plus_region),
                      fitted(model_log_y_times_region),
                      fitted(model_log_xy),
                      fitted(model_log_xy_plus_region),
                      fitted(model_log_xy_times_region))
library(reshape2)
mfitted_table <- melt(fitted_table, id = -1)

View(mfitted_table)

colnames(mfitted_table)[1] <- "Model"
colnames(mfitted_table)[2] <- "Order"
colnames(mfitted_table)[3] <- "Fit"

mfitted_table$Model = c("res_model_x",
                       "res_model_x_plus_region",
                       "res_model_x_times_region",
                       "res_model_log_x",
                       "res_model_log_x_plus_region",
                       "res_model_log_x_times_region",
                       "res_model_log_y",
                       "res_model_log_y_plus_region",
                       "res_model_log_y_times_region",
                       "res_model_log_xy",
                       "res_model_log_xy_plus_region",
                       "res_model_log_xy_times_region")

View(mres_table)
res_fit <- merge(mfitted_table, mres_table, by = c("Model", "Order") )

View(res_fit)

res_fit$Main_effect = 1
res_fit$Log_transform = 2

res_fit <-res_fit %>%
  mutate(Main_effect = case_when(
    endsWith(Model, "model_x") ~ "none",
    endsWith(Model, "plus_region") ~ "plus_region",
    endsWith(Model, "times_region") ~ "times_region",
    endsWith(Model, "log_x") ~ "none",
    endsWith(Model, "log_y") ~ "none",
    endsWith(Model, "log_xy") ~ "none"))

res_fit <-res_fit %>%
  mutate(Log_transform = case_when(
    endsWith(Model, "model_x") ~ "none",
    endsWith(Model, "model_x_plus_region") ~ "none",
    endsWith(Model, "model_x_times_region") ~ "none",
    endsWith(Model, "log_x") ~ "Log_x",
    endsWith(Model, "log_x_plus_region") ~ "Log_x",
    endsWith(Model, "log_x_times_region") ~ "Log_x",
    endsWith(Model, "log_y") ~ "Log_y",
    endsWith(Model, "log_y_plus_region") ~ "Log_y",
    endsWith(Model, "log_y_times_region") ~ "Log_y",
    endsWith(Model, "log_xy") ~ "Log_x_Log_y",
    endsWith(Model, "log_xy_plus_region") ~ "Log_x_Log_y",
    endsWith(Model, "log_xy_times_region") ~ "Log_x_Log_y"
  ))

res_group_plot_x_log_x_log_y_log_xy <- ggplot(data= res_fit, 
                                 aes(x=Fit, 
                                     y=Residuals, 
                                     color = Model))+
  geom_hline(yintercept=0, linetype = 'dashed', col = 'grey60')+
  geom_point(alpha = 0.4)+
  theme(legend.position = "none")+
  facet_grid(vars(Main_effect), vars(Log_transform))+
  theme( strip.text.y = element_blank() )
res_group_plot_x_log_x_log_y_log_xy


res_fit_log_y <- res_fit[res_fit$Log_transform == "Log_y", 1:6]
res_fit_log_xy <- res_fit[res_fit$Log_transform == "Log_x_Log_y", 1:6]
res_fit_log_xy_plus <- res_fit_log_xy[res_fit_log_xy$Main_effect == "plus_region", 1:6]
res_fit_log_y_xy <- rbind(res_fit_log_y,
                          res_fit_log_xy)
View(res_fit_log_y_xy)

res_fit_log_x <- res_fit[res_fit$Log_transform == "Log_x", 1:6]
res_fit_x <-  res_fit[res_fit$Log_transform == "none", 1:6]
res_fit_x_log_x <-rbind(res_fit_x,
                        res_fit_log_x)
View(res_fit_x_log_x)

res_fit_log_xy_plus_plot <-   ggplot(data= res_fit_log_xy_plus, 
                                aes(x=Fit, 
                                    y=Residuals, 
                                    color = Model))+
  ggtitle("Residual plot")+#"LogRent ~ LogPop + EU_region")+
  ylab(element_text("Standardised Residuals"))+
  theme(legend.position = "none")+
  geom_hline(yintercept=0, linetype = 'dashed', col = 'grey60')+
  ylim(-1,1)+
  geom_point(alpha = 0.5)
res_fit_log_xy_plus_plot

ggsave("C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/res_fit_log_xy_plus_plot.png",res_fit_log_xy_plus_plot, width=4, height=4)

res_group_plot <- ggplot(data= res_fit, 
                         aes(x=Fit, 
                             y=Residuals, 
                             color = Model))+
  geom_point(alpha = 0.5)+
  facet_grid(vars(Main_effect), vars(Log_transform))

res_group_plot

res_fit_x_log_x$Log_transform_f = factor(res_fit_x_log_x$Log_transform, levels=c('none','Log_x'))
res_fit_log_y_xy$Log_transform_f= factor(res_fit_log_y_xy$Log_transform, levels=c('Log_y','Log_x_Log_y'))

res_group_plot_y_log_xy <- ggplot(data= res_fit_log_y_xy, 
                                 aes(x=Fit, 
                                     y=Residuals, 
                                     color = Model))+
  geom_hline(yintercept=0, linetype = 'dashed', col = 'grey60')+
  geom_point(alpha = 0.4)+
  ylab(element_blank())+
  theme(legend.position = "none")+
  facet_grid(vars(Main_effect), vars(Log_transform_f))
  # theme( strip.text.y = element_blank() )

res_group_plot_y_log_xy


res_group_plot_x_log_x <- ggplot(data= res_fit_x_log_x, 
                         aes(x=Fit, 
                             y=Residuals, 
                             color = Model))+
  geom_hline(yintercept=0, linetype = 'dashed', col = 'grey60')+
  geom_point(alpha = 0.4)+
  ylab(element_text("Standardised Residuals"))+
  theme(legend.position = "none")+
  facet_grid(vars(Main_effect), vars(Log_transform_f))+
  theme( strip.text.y = element_blank() )

res_group_plot_x_log_x


res_fit$Fit <- as.numeric(res_fit$Fit)


library(scales)
res_fit_log_y$Fit <- as.numeric(res_fit_log_y$Fit)


res_log_Y_plot <-  ggplot(data= res_fit_log_y, 
                          aes(x=Fit, 
                              y=Residuals, 
                              color = Model))+
                    geom_point(alpha = 0.5)+
                    facet_grid(vars(Main_effect), vars(Log_transform))+
                    theme(legend.position = "none")+
                    ylab(element_blank())+
                    geom_hline(yintercept=0, linetype = 'dashed', col = 'grey60')+
                    # theme(axis.ticks.x = element_blank())+
                    # theme(axis.text.x = element_blank())+ 
                    scale_x_continuous(labels = number_format(accuracy = 0.1))
                    # theme(axis.text.x = element_text(angle = 90))
                    # scale_x_continuous() 
                    
                    # scale_x_continuous(breaks = scales::pretty_breaks(n = 5))
res_log_Y_plot

ggsave("C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/Residual_fit.png",res_group_plot, width=8, height=8)
ggsave("C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/Residual_fit_log_y.png",res_log_Y_plot, width=8, height=8)
ggsave("C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/Residual_fit_x_log_x.png",res_group_plot_x_log_x, width=8, height=8)


res_log_Y_plot
res_group_plot_x_log_x

top_row <- plot_grid(res_group_plot_x_log_x, res_group_plot_y_log_xy,  rel_widths = c(1, 0.9), labels = c('',''))
group_residual_plot <- grid.arrange(arrangeGrob(top_row, ncol=1, nrow=1))
ggsave("C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/Residual_fit_group_residual_plot_x_y_xy.png",group_residual_plot, width=12, height=5)


# Normal plot of the residuals
norm_x <- rstandard(model_x)
qqnorm(norm_x,
       ylab="Standardized Residuals", 
       xlab="Normal Scores", 
       main="Model_x")
qqline(norm_x)

norm_x_plot <- recordPlot()

plot(density(norm_x))

dens_norm_x_plot <- recordPlot()


norm_x_plus_region <- rstandard(model_x_plus_region)
qqnorm(norm_x_plus_region,
       ylab="Standardized Residuals", 
       xlab="Normal Scores", 
       main="Model_x_plus_region")
qqline(norm_x_plus_region)

norm_x_plus_region_plot <- recordPlot()

norm_x_times_region <- rstandard(model_x_times_region)
qqnorm(norm_x_times_region,
       ylab="Standardized Residuals", 
       xlab="Normal Scores", 
       main="Model_x_times_region")
qqline(norm_x_times_region)

norm_x_times_region_plot <- recordPlot()


norm_log_x <- rstandard(model_log_x)
qqnorm(norm_log_x,
       ylab="Standardized Residuals", 
       xlab="Normal Scores", 
       main="Model_log_x")
qqline(norm_log_x)

norm_log_x_plot <- recordPlot()

norm_log_x_plus_region <- rstandard(model_log_x_plus_region)
qqnorm(norm_log_x_plus_region,
       ylab="Standardized Residuals", 
       xlab="Normal Scores", 
       main="Model_log_x_plus_region")
qqline(norm_log_x_plus_region)

norm_log_x_plus_region_plot <- recordPlot()


norm_log_x_times_region <- rstandard(model_log_x_times_region)
qqnorm(norm_log_x_times_region,
       ylab="Standardized Residuals", 
       xlab="Normal Scores", 
       main="Model_log_x_times_region")
qqline(norm_log_x_times_region)

norm_log_x_times_region_plot <- recordPlot()



norm_log_y <- rstandard(model_log_y)
qqnorm(norm_log_y,
       ylab="Standardized Residuals", 
       xlab="Normal Scores", 
       main="Model_log_y")
qqline(norm_log_y)

norm_log_y_plot <- recordPlot()

norm_log_y_plus_region <- rstandard(model_log_y_plus_region)
qqnorm(norm_log_y_plus_region,
       ylab="Standardized Residuals", 
       xlab="Normal Scores", 
       main="Model_log_y_plus_region")
qqline(norm_log_y_plus_region)

norm_log_y_plus_region_plot <- recordPlot()

norm_log_y_times_region <- rstandard(model_log_y_times_region)
qqnorm(norm_log_y_times_region,
       ylab="Standardized Residuals", 
       xlab="Normal Scores", 
       main="Model_log_y_times_region")
qqline(norm_log_y_times_region)

norm_log_y_times_region_plot <- recordPlot()


norm_log_xy_times_region <- rstandard(model_log_xy_times_region)
qqnorm(norm_log_xy_times_region,
       ylab="Standardized Residuals", 
       xlab="Normal Scores", 
       main="Model_log_xy_times_region")
qqline(norm_log_xy_times_region)

norm_log_xy_times_region_plot <- recordPlot()


norm_log_xy_plus_region <- rstandard(model_log_xy_plus_region)
qqnorm(norm_log_xy_plus_region,
       ylab="Standardized Residuals", 
       xlab="Normal Scores", 
       main="Log Rent ~ Log Pop + EU region")
qqline(norm_log_xy_plus_region)
qqPlot(norm_log_xy_plus_region)

norm_log_xy_plus_region_plot <- recordPlot()

save_plot("C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Cartographs/Paper figures/qq_logXY_plus.png",norm_log_xy_plus_region_plot,ncol = 1, nrow = 1, base_height = 5, base_asp = 1, base_width = 5)

top_row <- plot_grid(norm_x_plot,norm_log_x_plot,norm_log_y_plot)#, labels = c('', '',''))
mid_row <- plot_grid(norm_x_plus_region_plot,norm_log_x_plus_region_plot,norm_log_y_plus_region_plot, labels = c('', '',''))
bot_row <- plot_grid(norm_x_times_region_plot,norm_log_x_times_region_plot,norm_log_y_times_region_plot, labels = c('', '',''))
grob

norm_x_plot <- as_grob(norm_x_plot, device = NULL)
norm_log_x_plot <- as_grob(norm_log_x_plot, device = NULL)
norm_log_y_plot <- as_grob(norm_log_y_plot, device = NULL)
norm_x_plus_region_plot <- as_grob(norm_x_plus_region_plot, device = NULL)
norm_log_x_plus_region_plot <- as_grob(norm_log_x_plus_region_plot, device = NULL)
norm_log_y_plus_region_plot <- as_grob(norm_log_y_plus_region_plot, device = NULL)
norm_x_times_region_plot <- as_grob(norm_x_times_region_plot, device = NULL)
norm_log_x_times_region_plot <- as_grob(norm_log_x_times_region_plot, device = NULL)
norm_log_y_times_region_plot <- as_grob(norm_log_y_times_region_plot, device = NULL)

group_norm <- grid.arrange(arrangeGrob(top_row, ncol=1, nrow=1),
             arrangeGrob(mid_row, ncol=1, nrow=1),
             arrangeGrob(bot_row, ncol=1, nrow=1), heights = c(2,2))
group_norm
library(gridGraphics)
library(grid)
ggsave("C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/group_norm_top_row.png",top_row, width=15, height=15)
ggsave("C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/group_norm_mid_row.png",mid_row, width=15, height=15)
ggsave("C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/group_norm_bot_row.png",bot_row, width=15, height=15)


# General plot log transformed

plot_log_x <- ggplot(data= d, aes(x=log_x, y=y))+
  geom_point()+
  ylab(element_blank())+
  xlab(element_blank())+
  # ylab("Rent (euros per hectare)")+
  # xlab("Population density (per hectare)")+
  geom_smooth(method=lm, se=TRUE)+
  stat_regline_equation(label.y = 223000, aes(label = after_stat(eq.label))) +
  stat_regline_equation(label.y = 255000, aes(label = ..adj.rr.label..))+
  ggtitle("EU-wide log_x")
plot_log_x

ggsave("C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/EU_wide_log_x.png",plot_log_x, width=5, height=5)


## Group figure
library(ggpattern)
library(ggpubr)
library(gridExtra)
library(cowplot)
library(gridtext)
library(grid)

top_row <- plot_grid(plot_west,plot_north, labels = c('', ''))
bottom_row <- plot_grid(plot_south,plot_east, labels = c('', ''))
left <- titleGrob("Rent (euros/ha/yr)", rot = 90, gp = gpar(fontsize = 11),debug=FALSE)+
bottom <- titleGrob("Population density (heads/ ha)", gp = gpar(fontsize = 11),debug=FALSE)+
group <- grid.arrange(arrangeGrob(top_row, ncol=1, nrow=1),
                       arrangeGrob(bottom_row, ncol=1, nrow=1), heights = c(2,2), left="Rent (euros/ha/yr)", bottom = "Population density (heads/ha)")
group
ggsave("C:/Users/spencerd/Documents/NaturaConnect/Spatial datasets/European countries/Input_datasets/Urban_land_rents/regional_eu_pop_rent.png",group, width=8, height=8)