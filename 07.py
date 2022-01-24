# 首先import Basemap的package
from mpl_toolkits.basemap import Basemap
import netCDF4 as nc
# 其他的套件
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm        # color map
import datetime
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
