from pprint import pp, pprint
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyAUPAr7xVEf5TqH7xzJJAkWBHSLEB3NQ-g')

# citys = ["台北市", "基隆市", "新北市", "連江縣", "宜蘭縣", "新竹市", "新竹縣", "桃園市",
# 		"苗栗縣", "台中市", "彰化縣", "南投縣", "嘉義市", "嘉義縣", "雲林縣", "台南市",
# 		"高雄市", "澎湖縣", "金門縣", "屏東縣", "台東縣", "花蓮縣"]

home = ["新北市淡水區文化里新生街20-3號3樓"]
test = ["新北市淡水區"]
keyword = "籃球場"
places = []

home_result = gmaps.geocode(home)
home_loc = home_result[0]['geometry']['location']

i=1
for city in test:
    geocode_result = gmaps.geocode(city)
    loc = geocode_result[0]['geometry']['location']
    basketball_courts = gmaps.places_nearby(keyword=keyword, location=loc, radius=3000)['results']
    print("以"+city+"為中心半徑3公里的籃球場數量: "+str(len(basketball_courts)))
        
    for place in basketball_courts:
        directions_result = gmaps.distance_matrix(home_loc, place['geometry']['location'])
        print(str(i)+"."+place['name']+" 距離: "+str(directions_result['rows'][0]['elements'][0]['distance']['text']))
        print(" 用戶評分: "+str(place['rating']))
        print(" 評分人數: "+str(place['user_ratings_total']))
        print(" 場所分類: "+str(place['types']))
        try:
            if place['opening_hours']['open_now'] == True:
                print(" O 此場所 目前開放中")
            else:
                print(" X 此場所 目前尚未開放")
        except KeyError:
            print(" 此場所 不對外開放")
        print()
        # places.append(place)
        i+=1

# # path = 'newtaipei.txt'
# # f = open(path, 'w', encoding='utf-8')
# # f.writelines([temp])
# # f.close()

