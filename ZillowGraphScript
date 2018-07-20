import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import quandl

# these fixed variables are the inputs for the user to enter.
DayBoth = '30'
MonthBoth = '06'
YearFrom = '2015'
YearTo = '2018'
Indicator = ['ZRISFRR']
LocationCode = 'Z'
Locations = ['08520', '32751']
quandl.ApiConfig.api_key = "NysKCsdEcqZ8sFDb3nDN"

# This appends your date ranges entered above to be added to the quandlquery
DateFrom = YearFrom+ "-" + MonthBoth + "-" + DayBoth
DateTo = YearTo + "-" + MonthBoth + "-" + DayBoth

#The logic behind this is that for each Zillow indicator and for each locations we get a table of quandl data. All of this is plotted on a line graph
#As an example, this could do Median home prices for two zipcodes and any combination of such. 
for SelectedIndicator in Indicator:
  for SelectedLocations in Locations:
    qundlquery = quandl.get('ZILLOW/'+LocationCode+SelectedLocations+"_"+SelectedIndicator, start_date=DateFrom, end_date=DateTo)
    plt.plot(qundlquery)

#This loops through our indicator's and locations to generate a list that is utilized in the legend of the graph
IndicatorNameList = []
for SelectedIndicator in Indicator:
  for SelectedLocations in Locations: 
    IndicatorNameList.append(SelectedIndicator + SelectedLocations)

#This (1) creates the legend on the graph, (2) saves the graphs and (3) opens the graph
plt.legend(IndicatorNameList)
plt.savefig('graph.png')
plt.show()


