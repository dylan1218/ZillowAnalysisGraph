from django.shortcuts import render
from django.http import HttpResponse
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import quandl
import io
# Create your views here.


def index(request):
	return render(request, 'main/ReturnZillowGraph.html')	    

	
def ZillowGraph(info):
	
	DayBoth = '30'
	MonthBoth = '06'
	YearFrom = info
	YearTo = '2018'
	Indicator = ['ZHVISF']
	LocationCode = 'Z'
	Locations = ['76633', '32751','07728']
	quandl.ApiConfig.api_key = "NysKCsdEcqZ8sFDb3nDN"
	
	mpl.style.use('seaborn')
	f = plt.figure(facecolor='w')
	
	DateFrom = YearFrom+ "-" + MonthBoth + "-" + DayBoth
	DateTo = YearTo + "-" + MonthBoth + "-" + DayBoth
	
	for SelectedIndicator in Indicator:
  		for SelectedLocations in Locations:
    			qundlquery = quandl.get('ZILLOW/'+LocationCode+SelectedLocations+"_"+SelectedIndicator, start_date=DateFrom, end_date=DateTo)
    			plt.plot(qundlquery)

	IndicatorNameList = []
	for SelectedIndicator in Indicator:
  		for SelectedLocations in Locations: 
    			IndicatorNameList.append(SelectedIndicator + SelectedLocations)
	
	plt.legend(IndicatorNameList)
	plt.savefig(r'C:\Users\Dylan\ZillowWebApplication\ZillowGraphs\static\ZillowGraphs\image.png')
	plt.close(f)
	
def ReturnZillowGraph(request):
	info=request.POST['info']
	ZillowGraph(info)
	return render(request,'main/ReturnZillowGraph_BelowSubmit.html')