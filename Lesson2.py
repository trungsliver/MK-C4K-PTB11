# Chữa BTVN
    # Trắc nghiệm
# 1D 2B 3B 4A 5B 6
# Câu 7 print("Học lập trình với Python")
# Câu 8: print("12 x 4 = ", 12*4)
    # Thực hành
# print("""
#       1
#       11
#       111
#       1111
#       11111
#       111111
#       """
# )

#  Biến số - phép gán
x = 10
y = 11
z = 12
a,b,c = 1,2,3

# Data Type - Kiểu dữ liệu
    # String - chuỗi ký tự
name = 'Bui Duc Trung'

    # Int - số nguyên
age = 27

    # Float - số thực
gpa = 1.9

    # Boolean - True/False
male = True

# Hiển thị ra màn hình
# print(f'Họ và tên: {name}')
# print(f'Tuổi: {age}')
# print(f'Điểm trung bình: {gpa}')
# print(f'Giới tính nam: {male}')

#  Biến và từ khóa
ptb11 = 11

#  Quy tắc đặt tên biến
    # - Chỉ gồm chữ cái tiếng anh, số, ký tự gạch dưới
    # - Không bắt đầu bằng số
    # - Phân biệt chữ hoa và chữ thường
    # - Không dùng từ khóa để đặt tên biến (phần 3)

    # VD đúng: school, luffy, gojo, j, tungbeo123, khang_anh, Gojo
    # VD sai: if, 1jack, 1/2, 50%, 

#  Xác định kiểu dữ liệu - data types: type()
# print('Kiểu dữ liệu của biến name:', type(name))
# print('Kiểu dữ liệu của biến age:', type(age))
# print('Kiểu dữ liệu của biến gpa:', type(gpa))
# print('Kiểu dữ liệu của biến male:', type(male))

# Kiểm tra dữ liệu khi nhập vào
name = str(input('Hãy nhập tên của bạn: '))
age = int(input('Hãy nhập tuổi của bạn: '))
gpa = float(input('Điểm trung bình năm học trước: '))
male = bool(input('Bạn có phải là nam không: '))

    # Hiển thị dữ liệu ra màn hình
print(f'Họ và tên: {name}')
print(f'Tuổi: {age}')
print(f'Điểm trung bình: {gpa}')
print(f'Giới tính nam: {male}')

a = float(input('Nhập chiều dài: '))
b = float(input('Nhập chiều rộng: '))
dientich = a * b
print(f'Diện tích HCN với chiều dài {a} và chiều rộng {b} là {dientich}')
