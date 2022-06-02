install.packages("dataRetrieval")
library(dataRetrieval)

#>   De Cicco, L.A., Hirsch, R.M., Lorenz, D., Watkins, W.D., 2018,
#>   dataRetrieval: R packages for discovering and retrieving water data
#>   available from Federal hydrologic web services, doi:10.5066/P9X4L3GE
#> 
#> A BibTeX entry for LaTeX users is
#> 
#>   @Manual{,
#>     author = {Laura A. {De Cicco} and David Lorenz and Robert M. Hirsch and William Watkins},
#>     title = {dataRetrieval: R packages for discovering and retrieving water data available from U.S. federal hydrologic web services},
#>     publisher = {U.S. Geological Survey},
#>     address = {Reston, VA},
#>     version = {2.7.6},
#>     institution = {U.S. Geological Survey},
#>     year = {2018},
#>     doi = {10.5066/P9X4L3GE},
#>     url = {https://code.usgs.gov/water/dataRetrieval},

# Calcasieu River at I-10 at Lake Charles, LA
siteNumberDS <- "08017044" 
CalcasieuDSInfo <- readNWISsite(siteNumberDS)
parameterCdDS <- "00065"

# Calcasieu River at I-10 at Lake Charles, LA
siteNumberUS <- "08015500" 
CalcasieuUSInfo <- readNWISsite(siteNumberUS)
parameterCdUS <- "00060"

# DEsired info
start.date = "2017-01-01"
end.date = "2021-01-01"


#Raw daily data:
CalcasieuUS <- readNWISdata(siteNumbers = siteNumberUS, parameterCd = parameterCdUS,
                     startDate = start.date, endDate = end.date,
                     service = "uv")

CalcasieuDS <- readNWISdata(siteNumbers = siteNumberDS, parameterCd = parameterCdDS,
                     startDate = start.date, endDate = end.date,
                     service = "uv")

# Sample data Nitrate:
parameterCd <- "00618"
qwData <- readNWISqw(siteNumber,parameterCd,
                      "1980-01-01","2010-01-01")

pCode <- readNWISpCode(parameterCd)


write.csv(CalcasieuDS,"gageData_ds.csv")
#print(CalcasieuUSInfo)