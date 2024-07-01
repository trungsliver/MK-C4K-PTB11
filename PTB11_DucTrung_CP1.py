# Quy tắc đặt tên: Tenlop_HoTen_CP1.py
# Trắc nghiệm
    # 1A 2B 3C 4D .....
# Tự luận

# import turtle
# t = turtle.Pen()
# turtle.bgcolor("black")
# colors = ["red", "yellow", "blue", "green"]
# for x in range(200):
#     t.pencolor(colors[x%4])
#     t.forward(x)
#     t.left(91)

a = int(input('Nhập 1 số nguyên: '))
check = True

for i in range(2,a):
    if a % i == 0:
        check = False

if a <= 1:
    print(f'{a} không phải là số nguyên tố.')
else:
    if check == True:
        print(f'{a} là số nguyên tố.')
    else:
        print(f'{a} không phải là số nguyên tố.')