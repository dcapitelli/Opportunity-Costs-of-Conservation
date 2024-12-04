
Urban cost layer refinement 

Here I lay out the different py files, their functions and order

1.0.Align_population_w_lulc.py
Function:
	align population raster with the land system map of the NaturaConnect project

1.1.urban_land_analysis.py
Function: 
	splits a EU raster into north, south, west, and east
	Clip pop density raster to the EU regions
	Impute the result of each regression and filter using urb land class
	Combine four regional inputs