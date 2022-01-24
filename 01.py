# coding=UTF-8
import urllib.request
import ssl
import json

# JSON下載的網址
url = 'https://data.epa.gov.tw/api/v1/aqx_p_434?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=json'
context = ssl._create_unverified_context()

with urllib.request.urlopen(url, context=context) as jsondata:
    # 將JSON進行UTF-8的解碼，並把解碼後的資料載入data陣列中
    data = json.loads(jsondata.read().decode('utf-8'))
# SiteId(測站編號)、SiteName(測站名稱)、MonitorDate(監測日期)、AQI(空氣品質指標)、SO2SubIndex(二氧化硫副指標)、COSubIndex(一氧化碳副指標)、O3SubIndex(臭氧副指標)、PM10SubIndex(懸浮微粒副指標)、NO2SubIndex(二氧化氮副指標)、O38SubIndex(臭氧8小時副指標)、PM25SubIndex(細懸浮微粒副指標)
# print(data)
aqi = data["records"]
for i in aqi:
    print(f'{i["SiteId"]:7}\t{i["SiteName"]:8}\t{i["MonitorDate"]:15}\t{i["AQI"]:5}\t{i["SO2SubIndex"]:15}\t{i["COSubIndex"]:15}\t{i["O3SubIndex"]:15}\t{i["PM10SubIndex"]:15}\t{i["NO2SubIndex"]:15}\t{i["O38SubIndex"]:15}\t{i["PM25SubIndex"]:15}')
