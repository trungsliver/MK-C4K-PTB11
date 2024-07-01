# Cấu trúc của xâu ký tự
# a = 'Khang Anh'
# print(len(a))       # Độ dài chuỗi ký tự
# print(a[6])         # Ký tự thứ 6 của chuỗi

# Lệnh duyệt ký tự của xâu (tương tự như duyệt phần tử danh sách)
    # Cách 1:
# for i in range(len(a)):
#     print(a[i])

    # Cách 2:
# for i in a:
#     print(i)

# # Xâu con
# str1 = 'ductrung123456'
# str2 = 'trung123'
# str3 = '789'
#     # Kiểm tra xâu con: hàm in
# print(str2 in str1)
# print(str3 in str1)
#     # Kiểm tra vị trí của xâu con: find()
# print(str1.find(str2))      # Vị trí của str2 trong str1
# print(str1.find(str3))      # str3 không phải xâu con, trả về -1
#     # Cấu trúc đầy đủ hàm find(): [Xâu mẹ].find([xâu con], start, stop)
# print(str1.find('123', 3, 14))

# Các lệnh thường gặp với xâu/chuỗi
#     # split() - tách chuỗi
# name = 'english,sleep,mouse,table,stupid,smart,camera'
# eng = name.split(',')
# print(eng)

# money = input('Nhập số tiền tiêu trong tuần, phân biệt bởi khoảng trắng: ')
# arr = money.split()
# print(arr)
#     # Chuyển các phần tử trong danh sách: string => int
# a = 0
# arr2 = []
# for i in arr:
#     a = int(i)
#     arr2.append(a)
# print(arr2)

#     # replace() - Thay thế
# x = 'Khang Anh likes Skibidi'
# y = x.replace('Skibidi', 'chocolate')
# print(y)
#         # replace đầy đủ
# x = 'Tu KA Tung Tu KA Tung Tu KA Tung Tu KA Tung '
# y = x.replace('KA', 'Dang', 2)
# print(y)

# Thực hành:
    # Bài 1: Nhập 2 xâu ký tự, 
        # Kiểm tra xem xâu 2 có nằm trong xâu 1 hay không
# xau1 = input('Nhập chuỗi ký tự 1: ')
# xau2 = input('Nhập chuỗi ký tự 2: ')
# if xau2 in xau1:
#     print('Xâu 2 nằm trong xâu 1')
# else:
#     print('Xâu 2 không nằm trong xâu 1')

    # Bài 2: Nhập 2 thông tin: họ, tên. In ra màn hình tên đầy đủ
# ho = input("Nhập họ của bạn: ")
# ten = input('Nhập tên của bạn: ')
# hoten = ho + ' ' + ten
# print(hoten)

    # Bài 3: Nhập vào 1 xâu ký tự định dạng dd/mm/yyyy
        # Tách ngày ngày tháng năm và hiển thị ra màn hình
# date1 = input('Nhập chuỗi dạng dd/mm/yyyy: ')
#             # Cách 1: dùng slpit()
# x = date1.split('/')
# day = x[0]
# month = x[1]
# year = x[2]
# print("Ngày:", day, '\nTháng:', month, '\nNăm:', year)

#             # Cách 2: dùng replace()
# date2 = date1.replace('/', ' tháng ', 1)
# date3 = date2.replace('/', ' năm ')
# print(date3)

    # Bài 4: Nhập vào thông tin dạng username:password
            # kiểm tra xem thông tin vừa nhập có trùng với thông tin có sẵn
username = 'admin'
password = '123456'

info = input('Nhập thông tin dạng "username:password": ')

while (':' not in info):
    print('Nhập sai định dạng, vui lòng nhập lại.')
    info = input('Nhập thông tin dạng "username:password": ')

info_split = info.split(':')
while (info_split[0] != username or info_split[1] != password):
    print('Nhập sai thông tin đăng nhập.')
    info = input('Nhập thông tin dạng "username:password": ')
    info_split = info.split(':')

print('Đăng nhập thành công!')