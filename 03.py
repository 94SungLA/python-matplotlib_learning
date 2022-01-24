import numpy as np
'''
# 輸出
# ndarray型態屬性
'''
num = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"此一維陣列為{num}")
print(f"陣列維度={num.ndim}")  # n=1
print(f"陣列形狀為{num.shape}")  # 以元組(tuple)表示，每個整數代表各維度的元素個數
print(f"陣列元素個數={num.size}")  # 陣列元素個數
# 為python內建的資料型態或NumPy提供的int16, int32, int64, floar64等
print(f"陣列元素的資料型態為{num.dtype}")
print(f"陣列元素的大小={num.itemsize}")  # 以位元組為單位，1 byte= 8 bits

'''
# 索引取值
# 變數指定
'''
print(f"第0個值={num[0]}")
print(f"第1個值={num[1]}")
print(f"第2個值={num[2]}")
# ...依此類推
print(f"第9個值={num[9]}")
num[0] = 100
print(f"更新後的陣列={num}")

'''
# 陣列走訪-1
'''
for i in num:
    print(i)

for i, j in enumerate(num):
    print(f"第{i}個值={j}")

for i in range(len(num)):
    print(f"第{i}個值={num[i]}")

'''
# 自動生成陣列元素
# arange()
# random()
'''
A1 = np.arange(1, 11, 1, dtype=int)  # arange:array range, like range()
print(f"陣列=\n{A1}")

A2 = np.arange(11, dtype=float)
print(f"陣列=\n{A2}")

A3 = np.arange(0, 1, 0.1)
print(f"陣列=\n{A3}")

A4 = np.random.rand(5)
print(f"陣列=\n{A4}")

A5 = np.random.randint(1, 10, 5)
print(f"陣列=\n{A5}")

'''
# 自動生成陣列元素
# linspace()
'''
B1 = np.linspace(0, 1, 10)  # linspace:linear space
print(f"B1陣列={B1}")

B2 = np.linspace(1, 100, 10)
print(f"陣列={B2}")

B3 = np.linspace(1, 100)
print(f"陣列={B3}")

'''
# 基本操作
# 加、減、乘、除、指數、不等符號的使用
'''
A = np.array([1, 2, 3, 4, 5])
B = np.array([1, 1, 1, 1, 1])
print(f"陣列相加={A+B}")
print(f"陣列相減={A-B}")
print(f"陣列相乘={A*B}")
print(f"陣列相除={A/B}")
print(f"陣列元素平方={A**2}")
print(f"陣列元素是否大於等於2={A>=2}")
print(f"陣列內積={A@B}")

'''
通用函式
add(), subtract(), multiply(), divide(), mod(), power(), dot()
'''
print(f"陣列相加={np.add(A,B)}")
print(f"陣列相減={np.subtract(A,B)}")
print(f"陣列相乘={np.multiply(A,B)}")
print(f"陣列相除={np.divide(A,B)}")
print(f"陣列相除取餘數={np.mod(A,B)}")
print(f"陣列冪次方運算={np.power(A,B)}")
print(f"陣列內積={np.dot(A,B)}")

'''
通用函式
sum(), max(), min(), floor(), ceil(), sqrt(), square()
'''
print(f"陣列中的元素總和={np.sum(A)}")
print(f"陣列中的最大值={np.max(A)}")
print(f"陣列中的最小值={np.min(A)}")
print(f"小於等於陣列中元素的最大整數={np.floor(A)}")
print(f"大於等於陣列中元素的最小整數={np.ceil(A)}")
print(f"陣列中元素的平方根={np.sqrt(A)}")
print(f"陣列中元素的平方={np.square(A)}")

'''
通用函式
sin(), cos(), tan(), asin(), acos(), atan()
'''
x = np.arange(-2*np.pi, 2*np.pi, 0.25*np.pi)
print(f"正弦函數值=\n{np.sin(x)}")
print(f"餘弦函數值=\n{np.cos(x)}")
print(f"正切函數值=\n{np.tan(x)}")

'''
通用函式
exp(), exp2(), log(), log2(), log10()
'''
x = np.arange(1, 11, 1)
print(f"自然指數值=\n{np.exp(x)}")
print(f"2的冪次方值=\n{np.exp2(x)}")
print(f"自然對數值=\n{np.log(x)}")
print(f"底數為2的對數值=\n{np.log2(x)}")
print(f"底數為10的對數值=\n{np.log10(x)}")

'''
通用函式
exp(), exp2(), log(), log2(), log10()
'''
x = np.arange(1, 11, 1)
print(f"自然指數值=\n{np.exp(x)}")
print(f"2的冪次方值=\n{np.exp2(x)}")
print(f"自然對數值=\n{np.log(x)}")
print(f"底數為2的對數值=\n{np.log2(x)}")
print(f"底數為10的對數值=\n{np.log10(x)}")
