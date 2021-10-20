from __future__ import print_function
import numpy
import PIL.Image 
import pickle
import requests
  
# # url variable store url
# url = "https://maps.googleapis.com/maps/api/staticmap?"
  
# # center defines the center of the map,
# # equidistant from all edges of the map. 
# center = "Dehradun"

# api_key = 'AIzaSyAUPAr7xVEf5TqH7xzJJAkWBHSLEB3NQ-g'
# # zoom defines the zoom
# # level of the map
# zoom = 10
# size = '400x400'

# url = url + "center=" + center + "&zoom=" +\
#                    str(zoom) + "&size=" + size + "&key=" +\
#                              api_key + "&sensor=false"
# print(url)
# # get method of requests module
# # return response object
# r = requests.get(url)

# with open('test.bin',mode='wb') as f:
# 	pickle.dump(r.content,f)
# # print(r.content)

with open('test.bin', mode='rb') as f:
	arr = pickle.load(f) #載入並反序列化資料
print(arr)
rows = arr.shape[0] #rows=5