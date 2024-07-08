from django.shortcuts import render
import requests
import datetime
 # Create your views here.
def index(request):
    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city="Kochi"


    appid='059a013e96364dd89a151249241002'
    URL= 'http://api.weatherapi.com/v1/forecast.json'
    PARAMS= {'q':city,'key':appid,'days':3}
    r= requests.get(url=URL,params=PARAMS)
    res= r.json()
    ctime=res['location']['localtime']
    temp=res['current']['temp_c']
    description=res['current']['condition']['text']
    icon= res['current']['condition']['code']
    today=res['forecast']['forecastday'][0]['day']['avgtemp_c']



    tomorrow=res['forecast']['forecastday'][1]['day']['avgtemp_c']



    thirdtemp=res['forecast']['forecastday'][2]['day']['avgtemp_c']


    
    return render(request,'weatherapp/index.html',{'temp':temp,'text':description,'tdate':today,
                                                   'tomtemp':tomorrow,'city':city,'time':ctime,
                                                   'thirdtemp':thirdtemp})