from django.shortcuts import render

# Create your views here.
class Geocoding :
    def Geocoding (self, request):
       area = request.area
       city = request.city
       state = request.state
       country = request.country
       # for url-encoded palce use urllib.parse
       ... 

class Geosearch :
    # looking for 
    ...