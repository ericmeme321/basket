from __future__ import print_function
from io import BytesIO
from pprint import pprint
import base64
import PIL.Image
import requests
import matplotlib.pyplot
import googlemaps

from app import get_API_KEY

# url variable store url
url = "https://maps.googleapis.com/maps/api/staticmap?"
  
# center defines the center of the map,
# equidistant from all edges of the map. 
api_key = get_API_KEY()

gmaps = googlemaps.Client(key=api_key)

# citys = ["台北市", "基隆市", "新北市", "連江縣", "宜蘭縣", "新竹市", "新竹縣", "桃園市",
# 		"苗栗縣", "台中市", "彰化縣", "南投縣", "嘉義市", "嘉義縣", "雲林縣", "台南市",
# 		"高雄市", "澎湖縣", "金門縣", "屏東縣", "台東縣", "花蓮縣"]

home = ["蘆洲運動中心"]
home_result = gmaps.geocode(home)
home_loc = home_result[0]['geometry']['location']
center = str(home_loc['lat'])+","+str(home_loc['lng'])

# zoom defines the zoom
# level of the map
zoom = 17
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