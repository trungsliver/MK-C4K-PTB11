# Chữa BTVN
# 1C 2B 3B 4B 5C 6D 7C 8C

# Hàm không có giá trị trả về
    # Tự định nghĩa 1 chương trình con
def hello():
    print('Xin chào Tuấn Minh')
    print('Xin chào Chí Bảo')
    print('Xin chào Bảo Phúc')
    print('Xin chào Khang Anh')
    # Gọi tên chương trình con khi cần sử dụng
# hello()

    # Bài tập 1: Viết hàm nhập 1 số nguyên dương n
    # Tính tổng các số chẵn từ 1 đến n
def sum_even():
    n = int(input('Input n: '))
    sum = 0
    for i in range(1, n+1):
        if i%2 == 0:
            sum += i

    # Bài tập 2: Viết hàm nhập vào số thực n
    # In ra màn hình giá trị tuyệt đối của số đó
def abs_float():
    n = float(input('Input n: '))
    if n < 0:
        abs = n * -1
    else:
        abs = n  
    print('Giá trị tuyệt đối của n là:', abs) 

    # Bài tập 3: Viết hàm nhập vào số nguyên dương n
    # Tính kết quả n giai thừa (n!)
    # VD: 6! = 1*2*3*4*5*6
def giaiThua():
    n = int(input('Input n: '))
    gt = 1
    for i in range(1, n+1):
        gt = gt * i
    print(f'{n}! = {gt}')
# giaiThua()

# Truyền dữ liệu cho hàm
PTB11 = ['Tuan Minh', 'Chi Bao', 'Bao Phuc', 'Khang Anh']
arr_num = [1,2,3,4,5,6,7]

def print_arr(arr):
    for i in range(len(arr)):
        print(f'[{i}] {arr[i]}')

# print_arr(PTB11)
# print_arr(arr_num)

# Bài tập: Đăng ký - Đăng nhập
users = ['admin:123456']        # Cấu trúc tài khoản trong danh sách: 'username:password'

#     # Đăng ký
def register():
    username = input('Nhập username: ')
    password = input('Nhập password: ')
    check = True
    # Nếu để trống username hoặc password thì không đăng ký được
    if username == '' or password == '':
        check = False
        print('Nhập thiếu thông tin!')
    else:
        # Duyệt các tài khoản có trong danh sách users
        for user in users:
            # Chia 1 user thành 2 phần username và password
            stored_username, stored_password = user.split(':')
            # Nếu trùng tên tài khoản thì không đăng ký được
            if username == stored_username:
                check = False
                print('Tài khoản đã tồn tại!')
    # Kiểm tra xem có đăng ký thành công không
    if check == True:
        # Nếu đăng đăng ký thành công thì add tài khoản mới vào danh sách users
        new_acc = username + ':' + password     
        users.append(new_acc)
        print('Đăng ký thành công!')
    else:
        print('Đăng ký không thành công!')


#     # Đăng nhập
def login():
    username = input('Nhập username: ')
    password = input('Nhập password: ')
    check = False
    for user in users:
        stored_username, stored_password = user.split(":")
        if stored_username == username and stored_password == password:
            check = True
    
    if check == True:
        print("Đăng nhập thành công")
    else:
        print("Đăng nhập không thành công.")

def main():
    while True:
        print('\n---------------DEF---------------')
        print("1. Đăng ký")
        print("2. Đăng nhập")
        print("3. Thoát")
        print('---------------------------------')
        choice = input('Nhập lựa chọn của bạn: ')

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            break
        else:
            print('Lựa chọn không hợp lệ!')

main()