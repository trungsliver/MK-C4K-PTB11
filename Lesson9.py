# Đề bài: Viết chương trình quản lý bán hàng với các thao tác CRUD
#           Lưu ý: Sử dụng switch - case để chọn chức năng

    # Khai báo danh sách các mặt hàng và giỏi hàng
product = ['Quần', 'Áo', 'Người', 'Laptop', 'Đồ ăn', 'Vũ khí']
cart = []

    # Switch - case: để chọn chức năng
while True:
    print('\n=============== SHOPPING CART ===============')
    print('1. Xem danh sách sản phẩm.')
    print('2. Xem giỏ hàng.')
    print('3. Thêm sản phẩm vào giỏ hàng.')
    print('4. Xóa sản phẩm khỏi giỏ hàng.')
    print('5. Thoát.')
    print('===============================================')
    choice = int(input('Hãy nhập lựa chọn của bạn: '))

    # Chức năng 1
    if choice == 1:
        print('\n========== Danh sách sản phẩm ==========')
        for i in range(len(product)):
            print(f'[{i+1}] {product[i]}')
        print('==========================================')
    elif choice == 2:
        if not cart:
            print('Giỏ hàng trống.')
        else:
            print('\n========== Sản phẩm trong giỏ hàng ==========')
            for i in range(len(cart)):
                print(f'[{i+1}] {cart[i]}')
            print('===============================================')
    elif choice == 3:
        print('\n========== Thêm sản phẩm vào giỏ hàng ==========')
        addPro = int(input('Nhập chỉ số sản phẩm bạn muốn thêm vào giỏ hàng: '))
        addPro = addPro - 1     # Đưa index đúng với danh sách
        if abs(addPro) < len(product):
            cart.append(product[addPro])
            print('Thêm sản phẩm thành công!')
        else:
            print('Thêm sản phẩm thất bại!')
        print('==================================================')
    elif choice == 4:
        print('\n========== Xóa sản phẩm khỏi giỏ hàng ==========')
        delPro = int(input('Nhập chỉ số sản phẩm bạn muốn xóa khỏi giỏ hàng: '))
        delPro = delPro - 1     # Đưa index đúng với danh sách
        if abs(delPro) < len(cart):
            cart.pop(delPro)
            print('Xóa sản phẩm thành công!')
        else:
            print('Xóa sản phẩm thất bại!')
        print('==================================================')
    else:
        break

# Bài tập 2: Tính tổng các phần tử có trong danh sách là số lẻ
    # Khởi tạo danh sách
num = []
sum = 0

    # Thêm phần tử vào danh sách
for i in range(1,21):
    num.append(i)

    # Hiện danh sách
print(num)

    # Tính tổng số lẻ
for i in num:
    if i%2 == 1:
        sum = sum + i

print('Tổng các phần tử trong danh sách là:', sum)

    # In ra phần tử lớn nhất và nhỏ nhất của danh sách
        # Cách 1:
print('Phần tử lớn nhất là:', max(num))
print('Phần tử nhỏ nhất là:', min(num))

    # Cách 2:
num.sort()
        # sau khi sort, thứ tự sẽ là số bé => số lớn
    # Phần tử lớn nhất là số cuối cùng, có index = -1
print('Phần tử lớn nhất là:', num[-1])
    # Phần tử nhỏ nhất là số đầu tiên, có index = 0
print('Phần tử nhỏ nhất là:', num[0])
