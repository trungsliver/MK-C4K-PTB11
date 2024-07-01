# Vòng lặp hữu hạn - Vòng lặp for

    # Hàm range(n): lấy từ 0 cho đến n-1
        # VD: range(100): lấy từ 0-99

    # Hàm đầy đủ: range(start, stop, step)
        # start: số bắt đầu (không bắt buộc, mặc định = 0)
        # stop: số kết thúc (bắt buộc)
        # step: không bắt buộc (bước nhảy, mặc định = 1)

# Ví dụng vòng lặp for
    # Thứ tự biến chỉ số (index): i,j,k

    # Ex1: range(n)
# for i in range(5):
#     print(i)

    # Ex2: range(start,stop)
# for i in range(5,10):
#     print(i)

    # Ex3: range(start,stop,step)
# for i in range(10,30,2):
#     print(i)

#  Đề bài: Nhập 2 số nguyên a và b từ bàn phím. 
#  In ra tất cả các số trong khoảng từ a đến b (tính cả a và b) hoặc ngược lại.
# a = int(input('Nhập số a:'))
# b = int(input('Nhập số b:'))

# if b >= a:
#     for i in range(a, b+1):
#         print(i)
# else:
#     for i in range(b, a+1):
#         print(i)

# Sử dụng random
    # Khai báo thư viện random
import random
    # Cú pháp sử dụng hàm trong thư viện: [Tên thư viện].[Tên hàm]
rd = random.randint(1,10)

# Đề bài: In ra màn hình bảng cửu chương của số vừa random 
#   Yêu cầu: sử dụng vòng lặp for
# print('Bảng cửu chương', rd)
# for i in range(1,11):
#     print(f'{rd} * {i} = {rd*i}')

# Đề bài: Nhập 2 số nguyên a và b. Tính tổng các số chẵn trong khoảng a đến b,
# a = int(input(" Nhập số a: "))
# b = int(input(" Nhập số b: "))
# sum = 0

    # Cách 1:
# for i in range(a,b+1):
#     if i % 2 == 0:
#         sum = sum + i

    # Cách 2:
# if a % 2 == 1:
#     a = a + 1

# for i in range(a, b+1, 2):
#     sum = sum + i

# print(f'Tổng các số chẵn từ {a} đến {b} là: {sum}')

# Đề bài: In các bảng cửu chương từ 1 đến 10
# for i in range(1,11):
#     print("\nBảng cửu chương", i)
#     for j in range(1,11):
#         print(f'{i} * {j} = {i*j}')
    
special_number = random.randint(1, 10)

guessed = False

while not guessed:
    guess = int(input("Hãy đoán số đặc biệt (từ 1 đến 10): "))

    if guess == special_number:
        print("Chúc mừng! Bạn đã đoán đúng số", special_number)
        guessed = True
    elif guess < special_number:
        print("Số bạn đoán nhỏ hơn số đặc biệt. Hãy thử lại.")
    else:
        print("Số bạn đoán lớn hơn số đặc biệt. Hãy thử lại.")