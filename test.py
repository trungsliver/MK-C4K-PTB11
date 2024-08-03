# # Đây là câu lệnh in ra màn hình
# # print('Hello "123" world')

# # Biến số - Variables
# # name = 'Bùi Đức Trung'

# # print('Xin chào', name)
# # print('Xin chào ' + str(name))

# # Kiểu dữ liệu - Data Types
#     # String - chuỗi ký tự
#     # Int - số nguyên
#     # Float - số thực
#     # Bool - True/False

# print("Hãy nhập thông tin của bạn")
# name = input('Hãy nhập tên của bạn: ')
# age = int(input('Hãy nhập tuổi của bạn: '))
# gpa = float(input('Nhập điểm trung bình của bạn: '))

# print('\nThông tin của bạn')
# print('Họ tên:', name)
# print('Tuổi:', age)
# print('Điểm trung bình:', gpa)

# print('\nChương trình kiểm tra chẵn - lẻ')
# num = int(input('Nhập số nguyên cần kiểm tra: '))

# if num % 2 == 0:
#     print(num, "là số chẵn.")
# else:
#     print(num, "là số lẻ.")

# # $ git remote add origin https://github.com/trungsliver/MK-C4K-PTB11.git


a = input('Nhập phần tử: ')
arr = a.split()
print(arr)

# Cách 1:
arr2 = []
for item in arr:
    x = float(item)
    arr2.append(x)
print(arr2)

# Cách 2
arr3 = [float(item) for item in arr]
print(arr3)