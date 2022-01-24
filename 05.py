# 環境設定
# %matplotlib inline
import numpy as np
import datetime
import pandas as pd
import matplotlib.cm as cm        # color map
import matplotlib.pyplot as plt
# 讀入所有自動氣象站資料
auto = pd.read_fwf("202112_auto_hr.txt")
print(auto.head())
# 將測站代碼設為資料的index
auto = pd.read_fwf("202112_auto_hr.txt", index_col="# stno")
print(auto.head())
# 將時間更改欄位名稱、改變格式
auto = auto.rename(columns={"yyyymmddhh": "datetime"})
auto['datetime'] = pd.to_datetime(
    auto["datetime"], format='%Y%m%d%H', errors='coerce')
print(auto.head())

# 取出特定氣象站的資料
C0A520 = auto.loc['C0A520']
# 將index改為時間
C0A520.set_index('datetime', inplace=True)
# 去除缺失資料
# -9991:儀器故障待修
# -9996:資料累計於後
# -9997:因不明原因或故障而無資料
# -9998:雨跡(Trace)
# -9999:未觀測而無資料
C0A520 = C0A520.replace([-9991, -9996, 9997, -9998, -9999], np.nan)
print(C0A520.head())
print(C0A520.dtypes)

# 搜尋dataframe中滿足特定條件的值：df[條件式]
C0A520[C0A520.TX01 > 100]

# 計算平均值
PS_m = C0A520.TX01.mean()
print(PS_m)
# 統計數據整理：dataframe名稱.describe()
C0A520.describe()

#plt.plot(x, y, 'style_code')
C0A520.TX01.plot()
plt.show()
