from often import *

pd.set_option('display.unicode.ambiguous_as_wide',True)
pd.set_option('display.unicode.east_asian_width',True)

today = Get_Now()
time_stamp = Get_Now_Plus()

Now_Weather_URL = f'https://www.cwb.gov.tw/Data/js/GT/TableData_GT_T_65.js?T={today}&_={time_stamp}'
Now_Weather_Str = crawler(Now_Weather_URL)
Now_Weather_Str = Now_Weather_Str[Now_Weather_Str.find("var GT ="):-1].replace("var GT = ", "").replace(";", "").replace("'", "\"")
Now_Weather_Dic = json.loads(Now_Weather_Str)

IDdata = open("IDSearch.txt","r",encoding="utf-8")
Str_IDdata = IDdata.read()
Dict_IDdata = json.loads(Str_IDdata)

City = input("Cities: ")
Area = input("Areas: ")

for data in Dict_IDdata:
    if data['label'] == City + Area:
        id = data['ID']
        break

for k, v in Now_Weather_Dic[id].items():
    print(str(k)+": "+str(v))