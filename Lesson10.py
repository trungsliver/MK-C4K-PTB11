# Bài 1: Viết chương trình nhập từ bàn phím danh sách a. 
# Hãy trả về kết quả các phần tử trong danh sách theo thứ tự tăng dần.
arr = [9,5,7,6,4,2,1,3]
arr.sort()
print(arr)

# Bài 2: Viết chương trình nhập từ bàn phím danh sách a. 
# Hãy tìm ra phần tử lớn nhất và nhỏ nhất từ danh sách a và trả về kết quả.
print('Phần tử lớn nhất:', max(arr))
print('Phần tử nhỏ nhất:', min(arr))

# Bài 3: Viết chương trình nhập từ bàn phím danh sách a. 
# Hãy tính giá trị trung bình của các phần tử trong danh sách a và trả về kết quả giá trị trung bình.
sum = 0
for item in arr:
    sum = sum + item
avg = sum/len(arr)
print('TBC:', avg)

# Bài 4: Viết chương trình nhập từ bàn phím danh sách a. 
# Tính tổng các số lẻ và tổng các số chẵn trong danh sách a.
sum_odd = 0
sum_even = 0
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        sum_even = sum_even + arr[i]
    else:
        sum_odd = sum_odd + arr[i]
print('Tổng các số lẻ:', sum_odd)
print('Tổng các số chẵn:', sum_even)

# Bài 5: Viết chương trình khai báo sẵn danh sách a. 
# Viết chương trình bao gồm các chức năng: 
    # hiện toàn bộ phần tử danh sách, 
    # thêm phần tử vào danh sách, 
    # sửa phần tử danh sách, 
    # xóa phần tử trong danh sách.
print('Hiện phần tử danh sách:')
for i in range(len(arr)):
    print(f'[{i}] {arr[i]}')

    # Thêm phần tử vào danh sách
arr.append(10)
arr.insert(7, 8)
print(arr)

    # Sửa phần tử danh sách
arr[-1] = 'Khang Anh'
print(arr)

    # Xóa phần tử danh sách
arr.pop(0)
arr.remove('Khang Anh')
print(arr)

# Quy tắc đặt tên: PTB11_HoTen_CP2.py