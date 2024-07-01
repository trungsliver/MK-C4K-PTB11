# # Đề bài: In ra màn hình từ 0 -> 5
#     # Vòng lặp for - Vòng lặp hữu hạn
# for i in range(6):
#     print(i)

#     # Vòng lặp while - Vòng lặp vô hạn
# k = 0
# while k < 6:
#     print(k)
#     k = k + 1           # k += 1

# Đề bài 1: Nhập số nguyên trong khoảng [0,100]
# nếu nhập sai (n<0 hoặc n>100) thì yêu cầu nhập lại

# n = int(input('Nhập số nguyên trong khoảng [0,100]: '))

# while n < 0 or n > 100:
#     print('Bạn đã nhập sai, vui lòng nhập lại !!!')
#     n = int(input('\nNhập số nguyên trong khoảng [0,100]: '))
# print('Nhập dữ liệu thành công !!!')

#  Đề bài: Tạo Mysterious Game
    # Yêu cầu: tạo ra 1 số đặc biệt để đoán (random)
    #  Người chơi cần nhập đến khi nào đoán đúng số đặc biệt thì dừng game

# import random
# number = random.randint(0,20)
# print('Số cần tìm (bí mật nhé):',number)

# n = int(input('Nhập dự đoán của bạn: '))
# count = 1

# while n != number:
#     if n > number:
#         print(n, 'lớn hơn số cần tìm.')
#     if n < number:
#         print(n, 'nhỏ hơn số cần tìm.')
#     if count >= 10:
#         print('\nBạn đã thua')
#         exit()
#     n = int(input('\nNhập dự đoán của bạn: '))
#     count = count + 1

# print(f'Bạn đã đoán đúng sau {count} lần.')

# Đề bài 2: Nhập vào số nguyên dương n
# Tính tổng tất cả các chữ số của n

n = int(input('Nhập 1 số nguyên dương: '))
sum = 0

while n > 0:
    sum = sum + n%10
    n = n // 10

print('Tổng các chữ số là:', sum)

