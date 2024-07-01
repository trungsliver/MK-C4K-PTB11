# Vòng lặp hữu han - Vòng lặp for

    # Hàm range(n)=> lặp lại từ 0 đến n-1
# for i in range(5):
#     print(i)

    # Hàm range(start, stop, step)
            # start: số bắt đầu (không bắt buộc)
            # stop: số kết thúc (bắt buộc)
            # step: bước nhảy (không bắt buộc)
# for i in range(1,10,3):
#     print(i)

# # # Ex1: range(stop)
# print('Ex1: range(stop)')
# for i in range(5):
#     print(i)

# # # Ex2: range(start, stop)
# print('Ex2: range(start, stop)')
# for i in range(5, 10):
#     print(i)

# # # Ex3: range(start, stop, step)
# print('Ex3: range(start, stop, step)')
# for i in range(1, 10, 2):
#     print(i)

#  Đề bài: Nhập 2 số nguyên a và b từ bàn phím. 
#  In ra tất cả các số trong khoảng từ a đến b (tính cả a và b) hoặc ngược lại.
# a = int(input(" Nhập số a: "))
# b = int(input(" Nhập số b: "))

# if a <= b:
#     for  i in range(a, b+1):
#         print(i)
# else:
#     for  i in range(b, a+1):
#         print(i)

# # Sử dụng random 
#     # Khai báo sử dụng thư viện
# import random
#     # Cú pháp sử dụng hàm trong thư viện: [Tên thư viện].[Tên hàm]
# rd = random.randint(1,10)

# # Đề bài: In ra màn hình bảng cửu chương của số vừa random 
# #   Yêu cầu: sử dụng vòng lặp for
# print(f"Bảng cửu chương {rd}:")
# for i in range(1,11):
#     print(f'{rd} * {i} = {rd*i}')

# Đề bài: NHập 2 số nguyên a và b. Tính tổng các số chẵn trong khoảng a đến b,
# a = int(input(" Nhập số a: "))
# b = int(input(" Nhập số b: "))
# sum = 0

# # Cách 1
# for i in range(a,b+1):
#     if i % 2 == 0:
#         sum = sum + i   # sum += i

# # Cách 2
# if a % 2 == 1:
#     a = a + 1
# for i in range(a, b+1, 2):
#     sum = sum + i

# print(f'Tổng các số chẵn từ {a} đến {b} là: {sum}')

# Đề bài: In các bảng cửu chương từ 1 đến 10
for i in range(1,11):
    print("\nBảng cửu chương", i)
    for j in range(1,11):
        print(f'{i} * {j} = {i*j}')
    
