# Chữa BTVN buổi 2
# 1B 2A 3C 4D 5C 6A
# 7 name = 'John'
# 8 float

# Ôn tập lệnh print

# a = int(input("Nhập a: "))
# b = int(input("Nhập b: "))

# print("Tổng của a và b là: ", a+b)
# print("Hiệu của a và b là: " + str(a-b))
# print(f"Tích của a và b là: {a*b}")
# print(f"Thương của {a} và {b} là: {a/b}")
# print("""
#     123
#     456
#     789
# """)

# Lệnh input
# Chuyển đổi giữa các kiểu dữ liệu

    # Lệnh int() có chức năng chuyển đối số thực hoặc chuỗi chứa số nguyên
    # Lệnh int() không thể chuyển đổi được chuỗi chứa số thực
    # Lệnh float() dùng để chuyển đổi số nguyên và chuỗi ký tự
    # Lệnh str() có thể chuyển đổi tất cả các kiểu dữ liệu khác
    # int() và float() không thể chuyển đổi chuỗi có công thức
    # str() có thể chuyển đổi cả công thức

# a = '123'
# b = '123jqk'
# c = 5
# d = 2.5
# print(type(a), type(b), type(c), type(d))

# convert = int(c*d)
# print(convert, type(convert))

# Các phép toán
# print("a \nb \nc")

# Bài tập
# print('Chào mừng bạn đến với Currency Converter - chuyển đổi tiền tệ')
# dollar = int(input("Vui lòng nhập số tiền cần chuyển (đô la Mỹ): $"))
# print('Số tiền sẽ được quy đổi ra Việt Nam Đồng (VNĐ)')
# vnd = dollar * 25000
# vnd = int(vnd)
# print(f"${dollar} quy đổi ra được {int(vnd)}đ")
# print("$" + str(dollar) + " quy đổi ra được " + str(vnd) + 'đ')

# câu điều kiện
    # Câu điều kiện dạng đủ
a = int(input('Hãy nhập 1 số nguyên: '))
if a % 2 == 0:
    print(a, "là số chẵn")
else:
    print(a, "là số lẻ")

    # Câu điều kiện dạng thiếu
a = input('Hãy nhập tên lớp của bạn: ')
if a == "PTB11" or a == "MK-C4K-PTB11":
    print('Bạn là học sinh lớp thầy Trung.')

# Câu 10 (1.0đ): Viết chương trình nhập vào một số nguyên s là số giây cần xử lý. Hãy đối số giây cho trước thành số giờ, phút, giây và in kết quả ra màn hình.
# Gợi ý: Sử dụng các phép toán chia lấy nguyên và chia lấy số dư với cách chuyển đổi sau:
#  - 1 giờ = 3 600 giây 
# - 1 phút = 60 giây
