from often import *

pd.set_option('display.unicode.ambiguous_as_wide',True)
pd.set_option('display.unicode.east_asian_width',True)

IDdata = open("IDSearch.txt","r",encoding="utf-8")
Str_IDdata = IDdata.read()
Dict_IDdata = json.loads(Str_IDdata)

# with open('QuickSearch.csv', 'w',encoding="utf-8") as f:  
#     writer = csv.writer(f)
#     for c in convertedDict:
#         for k, v in c.items():
#             writer.writerow([k, v])
#             print(c)

today = Get_Now()
city = input("cities: ")
area = input("areas: ")

for data in Dict_IDdata:
    if data['label'] == city + area:
        id = data['ID']
        break

Weather_URL = f'https://www.cwb.gov.tw/V8/C/W/Town/MOD/Week/{id}_Week_PC.html?T={today}'
Weather_HTML = crawler(Weather_URL)
soup = BeautifulSoup(Weather_HTML, 'html.parser')

temp_list = []
columns_list = []
values_list = []
trs = soup.find_all('tr')
i = 0
for tr in trs:
    if i == 0:
        temp_list = tr.text.split('\n')
        del temp_list[0], temp_list[-1]
        columns_list = temp_list
        i = 1
    else:
        temp_list = tr.text.split('\n')
        del temp_list[0], temp_list[-1]
        if len(temp_list) == 15:
            values_list.append(temp_list)

temp_list.clear()
i = 0
for c in columns_list:
    if i == 0:
        temp_list.append(c)
        i = 1
    else:
        temp_list.append(c)
        temp_list.append(c)
columns_list = temp_list

# print(len(th_list))
# print(th_list)
# print(len(tr_list))
# print(tr_list)

Weather_df = pd.DataFrame(columns=columns_list)
for c in values_list:
    Weather_df.loc[len(Weather_df)] = c
    
Weather_df.set_index("日期", inplace=True)
print(Weather_df)