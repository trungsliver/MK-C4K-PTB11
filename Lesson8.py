# CRUD: Create - Read - Update - Delete

# Create - Khởi tạo danh sách
dsPTB11 = ['Bao', 'Minh', 'Dang', 'Tu', 'Tung', 'Khang Anh']

    # Hàm len() - trả về kích thước 
# human = 'Khang Anh'
# print(len(human))
# print(len(dsPTB11))

# Read - Đọc, hiện các phần tử danh sách
    # Hiện 1 phần tử bằng chỉ số index (đếm từ 0)
# print(dsPTB11[3])

    # Hiện phần tử cuối dùng của danh sách
# print(dsPTB11[-1])

#     # Hiện toàn bộ phần tử danh sách
#         # Cách 1:
# for i in range(len(dsPTB11)):
#     print(f'[{i+1}] {dsPTB11[i]}')

#         # Cách 2:
# for item in dsPTB11:
#     print(item)

#         # Cách 3:
# for index, item in enumerate(dsPTB11):
#     print(f"[{index + 1}] {item}")

# Update - Chỉnh sửa danh sách
    # Thêm phần tử vào cuối danh sách - append()
dsPTB11.append('Phuc')

    # Thêm phần tử vào vị trí chỉ định - insert()
dsPTB11.insert(2, 'Imposter')

    # Update phần tử trong danh sách
dsPTB11[2] = 'Ching Chong'

# print(dsPTB11)

# Delete - Xóa phần tử danh sách
    # Xóa phần tử bằng giá trị - remove()
dsPTB11.remove('Ching Chong')

    # Xóa phần tử bằng chỉ số index - pop()
dsPTB11.pop(6)

    # Xóa tất cả phần tử của danh sách - clear()
dsPTB11.clear()

arr_num = [19, 16, 6, -1, 12, 15]

# Sắp xếp các phần tử trong danh sách - sort
    # Sắp xếp từ nhỏ tới lớn
arr_num.sort()
# print(arr_num)

    # Sắp xếp từ lớn tới nhỏ
arr_num.sort(reverse=True)
# print(arr_num)

# Bài tập: tìm phần tử chung của 2 danh sách
arr1 = []
arr2 = []
    # Thêm phần tử cho arr1
for i in range(1,16):
    arr1.append(i)
    # Thêm phần tử cho arr2
for i in range(10,25):
    arr2.append(i)
    # Hiện phần tử của 2 danh sách
print(arr1)
print(arr2)

    # arr3 dùng để chứa phần tử chung của arr1 và arr2
arr3 = []

for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i] == arr2[j]:
            arr3.append(arr1[i])

print('Phần tử chung của 2 danh sách là: ', arr3)