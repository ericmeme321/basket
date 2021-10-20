from __future__ import print_function
from io import BytesIO
import os, base64
import PIL.Image
import requests
import matplotlib.pyplot

# url variable store url
url = "https://maps.googleapis.com/maps/api/staticmap?"
  
# center defines the center of the map,
# equidistant from all edges of the map. 
center = "Dehradun"

api_key = 'AIzaSyAUPAr7xVEf5TqH7xzJJAkWBHSLEB3NQ-g'
# zoom defines the zoom
# level of the map
zoom = 10
size = '400x400'

url = url + "center=" + center + "&zoom=" +\
                   str(zoom) + "&size=" + size + "&key=" +\
                             api_key + "&sensor=false"
print(url)
# get method of requests module
# return response object
r = requests.get(url)

image = PIL.Image.open(BytesIO(r.content))

# 圖片的base64編碼
ls_f = base64.b64encode(BytesIO(r.content).read())

# base64編碼解碼
imgdata = base64.b64decode(ls_f)

matplotlib.pyplot.imshow(image)
matplotlib.pyplot.show()
# 圖片文件保存
file = open('test.jpg','wb')
file.write(imgdata)
file.close()