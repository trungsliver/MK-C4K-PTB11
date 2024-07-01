# Đề bài: in số từ 1 => 10
    # Vòng lặp for - Vòng lặp hữu hạn
# for i in range(1,11):
#     print(i)

    #  Vòng lặp while - Vòng lặp vô hạn
# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1

# Đề bài 1: Nhập số nguyên n trong khoảng (0,100)
# nếu nhập sai (n<0 hoặc n>100) thì yêu cầu nhập lại

# n = int(input('Nhập số tronng khoảng [0,100]: '))

# while n > 100 or n < 0:
#     print('Bạn đã nhập sai, Vui lòng nhập lại !!!')
#     n = int(input('Nhập số tronng khoảng [0,100]: '))
# print('\nNhập dữ liệu thành công')

#  Đề bài: Tạo Mysterious Game
    # Yêu cầu: tạo ra 1 số đặc biệt để đoán (random)
    #  Người chơi cần nhập đến khi nào đoán đúng số đặc biệt thì dừng game

# import random
# number = random.randint(0,20)
# print("Số cần tìm (bí mật thôi nhé):", number)

# n = int(input('\nNhập dự đoán của bạn: '))
# while n != number:
#     if n > number:
#         print(n, 'lớn hơn mysterious number')
#     else:
#         print(n, 'nhỏ hơn mysterious number')
#     n = int(input('\nNhập dự đoán của bạn: '))

# print('Dự đoán thành công !!!')

# Kiểm tra kiểu dữ liệu khi nhập

# x = input("Input anything: ")

# try:
#     val = int(x)
#     print('Data type: int')
# except ValueError:
#     try:
#         val = float(x)
#         print('Data type: float')
#     except ValueError:
#         print('Data type: string')

# val = int(x)

# Đề bài 2: Nhập vào số nguyên dương n
# Tính tổng tất cả các chữ số của n

n = int(input('Nhập số nguyên dương n: '))
sum = 0

while n > 0:
    sum = sum + n%10
    n = n // 10

print('Tổng các chữ số của n là:', sum)