# Đề bài: cho danh sách num gồm các số từ 1 đến 30
# Yêu cầu:
    # 1. Tự động thêm phần tử vào danh sách
    # 2. Tính tổng các phần tử chia hết cho 3
    # 3. Tìm phần tử lớn nhất mà chia hết cho 4
    # 4. Tìm phần tử nhỏ nhất chia hết cho 7

# Bài làm
num = []

# 1. Tự động thêm phần tử vào danh sách
for i in range(1,31):
    num.append(i)
print(num)

# 2. Tính tổng phần tử chia hết cho 3
sum = 0
for item in num:
    if item % 3 == 0:
        sum = sum + item
print('Tổng phần tử chia hết cho 3:', sum)

# 3. Tìm phần tử lớn nhất mà chia hết cho 4
num4 = []
for item in num:
    if item % 4 == 0:
        num4.append(item)
num4.sort()
print('Phần tử chia hết cho 4 lớn nhất: ', num4[-1])

# 4. Tìm phần tử nhỏ nhất mà chia hết cho 7
num7 = []
for item in num:
    if item % 7 == 0:
        num7.append(item)
num4.sort()
print('Phần tử chia hết cho 7 nhỏ nhất: ', num7[0])