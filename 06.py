# 先import netCDF4進來
import netCDF4 as nc
# 其他的套件
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm        # color map
import datetime  # python中跟時間有關的變數型態

data = nc.Dataset("./sst.mnmean.v4.nc")
# data # show metadata information
data
# 先將經度、緯度和高度的變數型態取出
lat = data.variables['lat'][:]
lon = data.variables['lon'][:]
#lev = data.variables['zlev'][:]
print(lat.shape)
print(lon.shape)

# NC檔中有time的資訊，我們將它讀出，並使用.units獲得它的單位
time = data.variables['time'][:]  # get value of time
time_units = data.variables['time'].units  # get unit
# get date using NetCDF num2date function
date_ = nc.num2date(time, units=time_units, calendar='standard')
print(time)
print('=====')
print(time_units)
print('======')
print(date_)

# 來看一下sst的變數
print(data.variables['sst'])

sstt = data.variables['sst'][0, :, :]  # 維度分別是時間、緯度、經度
print(sstt.shape)

# 將結果畫出
plt.figure(figsize=(10, 6), dpi=100)

CS = plt.contourf(lon, lat, sstt, cmap='seismic')  # 經度的問題？
plt.colorbar(CS, orientation='vertical')
##可以試著改變contour類型, colormap, levels看看有何不同

# 將時間資料轉換成字串
date = date_[0].strftime('%Y/%m/%d')
plt.title('SST ' + date)

plt.show()

# 嘗試抓出某一緯度的值
print(np.where(np.abs(lat-24) == 0))  # 找出緯度在資料中的位置
print(np.ndim(np.where(np.abs(lat-24) == 0)))
ilat = np.where(np.abs(lat-24) == 0)[0][0]  # 只取值
print(ilat)
plt.figure(dpi=100)  # 設定解析度，預設為100
plt.plot(lon-180, sstt[ilat, :])
plt.xlabel('lon')
plt.ylabel('SST($^o$C)')
plt.title('SST variation at 24$^o$N')
plt.show()

# Ex1. Global map, basic projection and layout
lon2, lat2 = np.meshgrid(lon, lat)  # 將經緯度轉為2D-array
plt.figure(figsize=(10, 6))
# 畫 Base map
m = Basemap(projection='cyl', lon_0=180, lat_0=0)
# resolution='i',
# llcrnrlon=100.0 , llcrnrlat=0.0,
# urcrnrlon=140.0, urcrnrlat=30.0) # 可調整地圖大小
# 以下code是畫海岸線和國界的指令
m.drawcoastlines()  # 畫海岸線
m.drawcountries()  # 畫國界
m.fillcontinents(color='white')
# 畫經緯度線
parallels = np.arange(-90., 90, 30.)
meridians = np.arange(0., 360., 60.)
m.drawparallels(parallels, labels=[1, 1, 0, 0], fontsize=10)  # 緯度度線、在左右兩邊加緯度標
m.drawmeridians(meridians, labels=[0, 0, 0, 1], fontsize=10)  # 經度線、在下方加經度標籤
# 開始畫圖
cx, cy = m(lon2, lat2)  # 將經緯度轉為地圖座標
#
CS = m.contourf(cx, cy, sstt, cmap='seismic', alpha=0.8)
# 加上顏色指標
plt.colorbar(CS, orientation='horizontal')
date = date_[0].strftime('%Y/%m/%d')
plt.title('SST '+date)
plt.show()
