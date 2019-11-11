import requests
from dotenv import load_dotenv
import os

load_dotenv()


# this function finds the lat, long of a place using autocomplete by Mapbox
# due to multiple place could be found, sample indicates which index of address
def get_coordi(borough, sample = 0):
  MAPBOX_BASE_URL = 'https://api.mapbox.com/geocoding/v5/mapbox.places/'
  MAPBOX_KEY = os.getenv("MAPBOX_KEY")
  options = '&autocomplete=true&country=gb'
  url = MAPBOX_BASE_URL+borough+'.json?access_token='+MAPBOX_KEY + options

  response = requests.get(url)
  if response.status_code == 200:
    # print(borough,'API ok')
    resp = response.json()

  longitude = resp['features'][sample]['center'][0]
  latitude = resp['features'][sample]['center'][1]

  return latitude, longitude


# this function finds the lat, long of a place using defined number of points
def get_multi_coordi(borough, points = 3):
  coordi_list = []
  for point in range(points):
    coordi_list.append(get_coordi(borough, point))
  return coordi_list


def get_air_quality(lat, long, hours=6):
  AQI_BASE_URL='https://api.breezometer.com/air-quality/v2/historical/hourly?'
  BREEZO_KEY = os.getenv("BREEZO_KEY")
  options = "lat=%s&lon=%s&key=%s&hours=%s" %(lat,long,BREEZO_KEY,hours)
  url = AQI_BASE_URL+options

  r = requests.get(url)
  call = r.json()

  aqi_list = []

  for data in call['data']:
      if data['data_available']==True:
          aqi_list.append(data['indexes']['baqi']['aqi'])

  return aqi_list


# get the air quality data of a place, returns a list
def get_place_aqi(borough):
  coordi_list = get_multi_coordi(borough)
  print(coordi_list)

  aqi_list = []
  for coordi in coordi_list:
    aqi_list.append(get_air_quality(coordi[0],coordi[1]))

  return aqi_list





