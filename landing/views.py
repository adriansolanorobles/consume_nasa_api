from django.shortcuts import render,redirect
from django.http import Http404
import requests
import pprint

def index(request):
    p = {'api_key': 'eWJcHyYyYOlQQxeyVaf30JQEgjwM0EKcix6aDdJG','start_date':'2017-04-28','end_date':'2017-04-29'}
    r = requests.get('https://api.nasa.gov/neo/rest/v1/feed', params=p)
    data_asteroids = []
    data_list = r.json()
    near_earth_objects_dict = data_list['near_earth_objects']
    count = 1
    for date_items in near_earth_objects_dict:
        ##print(type(near_earth_objects_dict[date_items]))
        for date_items_values in near_earth_objects_dict[date_items]:
            #print(type(date_items_values))
            #print(date_items_values['name'])
            data_asteroids.append(
                {
                    'id': count,
                    'name': date_items_values['name'],
                    'url' : date_items_values['nasa_jpl_url'],
                    'is_hazardous': date_items_values['is_potentially_hazardous_asteroid'],
                    'diameter_max': date_items_values['estimated_diameter']['kilometers']['estimated_diameter_max'],
                    'diameter_min': date_items_values['estimated_diameter']['kilometers']['estimated_diameter_min']
                }
            )
            count +=1
    return render(request,"landing/index.html",{"asteroids":data_asteroids})