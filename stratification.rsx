##Copernicus = group
##LC= raster
##issue= raster
##output= output raster

library(sf)
library(sp)
library(terra)
library(snow)


LC<-terra::rast(LC)
issue<-terra::rast(issue)


x<-resample(issue, LC, method='near')
issue<-x


issue<-terra::project(issue,crs(LC))
issue<-crop(issue, ext(LC), mask=T)
issue<-terra::resample(issue, LC, method='near')


result<-terra::zonal(issue,LC,'median', na.rm=T)

#result
>result

rec<-terra::classify(LC,result)

rc <- function(x1,x2) { ifelse(x1 <= x2, 0, ifelse(x1 > x2, 1, NA)) }

s2<-c(issue,rec)

output <- terra::lapp(s2, fun = rc, cores = 4, filename = "output.tif", overwrite = TRUE)
