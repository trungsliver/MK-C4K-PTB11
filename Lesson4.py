# Chữa BTVN buổi 3
# 1A 2D 3A 4D 5C 6D 7.Kết quả 1 8A

# Biểu thức logic
    # Chỉ trả về giá trị True hoặc False

    # Phép and 
    # True and True => True
    # True and False => False
    # False and True => False
    # False and False => False

    # Phép or
    # True or True => True
    # True or False => True
    # False or True => True
    # False or False => False

    # Phép not
    # not True => False
    # not False => True

# x,y,z = 10,6,8
# a = x < 12 and z > 6    # True and True => True
# b = x > 15 or y < 8     # False or True => True
# c = not b               # not True => False
# print(a,b,c)

# Câu điều kiện
    # Câu điều kiện dạng thiếu
# age = int(input('Hãy nhập tuổi của bạn: '))
# if age >= 18:
#     print('Bạn đã đủ 18 tuổi hehee.')

    # Câu điều kiện dạng đủ
# a = int(input("\nHãy nhập 1 số nguyên: "))
# if a%5 == 0:
#     print(a, 'chia hết cho 5.')
# else:
#     print(a, 'không chia hết cho 5.')

    # Câu điều kiện dạng đa nhánh
        # 8-10: Giỏi, 6.5-8: Khá, 5-6.5: Trung Bình, 0-5: Yếu
# diem = float(input('Hãy nhập điểm trung bình của bạn (thang 10): '))

# if diem >= 8 and diem <= 10:
#     print('Học lực: Giỏi')
# elif diem >= 6.5 and diem < 8:
#     print('Học lực: Khá')
# elif diem >= 5 and diem < 6.5:
#     print('Học lực: Trung Bình')
# elif diem >= 0 and diem < 5:
#     print('Học lực: Khá')
# else:
#     print('Nhập điểm không hợp lệ.')

# Ví dụ
kW = float(input("Nhập số kW điện đã sử dụng: "))
price = 0

if kW < 0:
    print('Nhập sai, vui lòng nhập lại!')
elif kW <= 100:
    price = kW * 3000
    print('Số tiền điện phải trả:', price)
elif kW <= 600:
    price = 100*3000 + (kW - 100)*4000
    print('Số tiền điện phải trả:', price)
else:
    price = 100*3000 + 500*4000 + (kW-600)*5000
    print('Số tiền điện phải trả:', price)
