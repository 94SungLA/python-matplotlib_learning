# coding=UTF-8
import urllib.request
import csv

url = 'https://data.epa.gov.tw/api/v1/aqx_p_434?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=csv'  # CSV檔的網址
webpage = urllib.request.urlopen(url)  # 開啟網頁
data = csv.reader(webpage.read().decode('utf-8').splitlines())  # 讀取資料到data陣列中
# SiteId(測站編號)、SiteName(測站名稱)、MonitorDate(監測日期)、AQI(空氣品質指標)、SO2SubIndex(二氧化硫副指標)、COSubIndex(一氧化碳副指標)、O3SubIndex(臭氧副指標)、PM10SubIndex(懸浮微粒副指標)、NO2SubIndex(二氧化氮副指標)、O38SubIndex(臭氧8小時副指標)、PM25SubIndex(細懸浮微粒副指標)


for i in data:
    print(i)
    # print(f"{i[0]:7}\t{i[1]:8}\t{i[2]:15}\t{i[3]:5}\t{i[4]:15}\t{i[5]:15}\t{i[6]:15}\t{i[7]:15}\t{i[8]:15}\t{i[9]:15}\t{i[10]:15}")
