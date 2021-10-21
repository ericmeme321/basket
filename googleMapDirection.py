import googlemaps
import webbrowser
import os
from pprint import pprint

api_key = 'AIzaSyAUPAr7xVEf5TqH7xzJJAkWBHSLEB3NQ-g'
gmaps = googlemaps.Client(api_key)
address = "新北市淡水區文化里6鄰新生街20-3號3樓"
destination = "水碓籃球場"
directions = gmaps.directions(address, destination)
# pprint(directions)
html_str = ""
i=1
for step in directions[0]['legs'][0]['steps']:
    html_str+= "Step"+str(i)+":<br> 行走距離: "+step['distance']['text']+"所需時間: "+step['duration']['text']+"<br> 導航: "+str(step['html_instructions'])+"<br><br>"
    # print("Step"+str(i))
    # print("行走距離: "+step['distance']['text']+"所需時間: "+step['duration']['text'])
    # print("導航: "+str(step['html_instructions']))
    # print()
    i+=1

Html_file= open("Direction.html","w",encoding='utf-8')
Html_file.write(html_str)
Html_file.close()

filename = 'file:///'+os.getcwd()+'/' + 'Direction.html'
webbrowser.open_new_tab(filename)