# import numpy as np
# A = np.array([[1,2],[3,4]])
# print(A)
# print(type(A))
# print(A.ndim)
# print(A.dtype)
# print(A.max(),A.mean(),A.min(),A.sum())
import pandas as pd
s = pd.Series([0.0,3.6,2.0,5.8,4.2,8.0,5.5,6.7,4.2]) #시리즈 생성
s.index = pd.Index([0.0,1.2,1.8,3.0,3.6,4.8,5.9,6.8,8.0]) #시리즈 인덱스
# print(s.describe())
s.index.name = 'MY_IDX'
s.name = 'MY_SERIES'
import matplotlib.pyplot as plt
plt.title("ELLIOTT_WAVE")
plt.plot(s,'bs--')
plt.xticks(s.index)
plt.yticks(s.values)
plt.grid(True)
plt.show()
plt.savefig('엘리어트.png')
