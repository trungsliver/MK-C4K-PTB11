# Hàm có giá trị trả về
def dtich_HCN(a, b):
    s = a * b
    return s

# Hàm không có giá trị trả về
def dtich_HCN2(a, b):
    s = a * b
    print(s)

# hcn1 = dtich_HCN(2,4) + dtich_HCN(2,5) + dtich_HCN(5,10)
# print(hcn1)

# dai = float(input('Nhập chiều dài: '))
# rong = float(input('Nhập chiều rộng: '))
# print(dtich_HCN(dai,rong))

# Bài tập: Viết hàm/chương trình con để tìm vị trí phần tử lớn nhất của danh sách
    # Yêu cầu: Hàm có giá trị trả về, return index của phần tử lớn nhất
A = [1, 9, 8, 15, 6, 29, 12, 7]

def findIndexMax(arr):
    max_item = max(arr)
    for i in range(len(arr)):
        if arr[i] == max_item:
            return i
# print(findIndexMax(A))

# Thư viện Math
import math
    # Tìm UCLN của 2 số
print(math.gcd(20,45))

# Thư viện string
import string
name = 'dUc tRuNG vIp pRO'
# print(string.upper(name))
print(string.capwords(name))
a = string.upper(name)
print(a)
