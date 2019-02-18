import numpy as np

a = np.array([1010, 1000, 990])

print_val = np.exp(a) / np.sum(np.exp(a)) # ソフトマックス関数の計算

print(print_val) # 正しく計算されない

c = np.max(a) #1010

print(c)

print_val = a-c

print(print_val)

print_val = np.exp(a-c) / np.sum(np.exp(a-c))


print(print_val) # array([9.99954600e-01, 4.539786e-05, 2.06106005e-090]

