# CRUD: Create - Read - Update - Delete

# Create - Khởi tại danh sách
    # Khởi tạo danh sách trống
array1 = []
    # Khởi tạo danh sách với các phần tử cho trước
dsPTB11 = ['Bao', 'Minh', 'Dang', 'Tu', 'Tung', 'Khang Anh', 'Phuc']

    # Hàm len() - trả về kích thước / độ dài danh sách
# human = 'Bao Phuc'
# print(len(human))
# print(len(dsPTB11))

# Read - Đọc/Hiện các phần tử danh sách
    # Hiện phần tử bằng chỉ số index
# print(dsPTB11[6])
    # Hiện phần tử cuối cùng của danh sách, index = -1
# print(dsPTB11[-1])

    # Hiện toàn bộ phần tử của danh sách
        # Cách 1:
# for i in range(len(dsPTB11)):
#     print(dsPTB11[i])

        # Cách 2:
# for item in dsPTB11:
#     print(item)

        # Cách 3:
# for index, item in enumerate(dsPTB11):
#     print(f'[{index}] {item}')

# Update - chỉnh sửa phần tử danh sách
    # Thêm phần tử vào cuối danh sách - append(value)
dsPTB11.append('Duc Trung')

    # Thêm phần tử vào vị trí chỉ định - insert(index, value)
dsPTB11.insert(1, 'Imposter')

    # Chỉnh sửa phần tử theo index
dsPTB11[1] = 'hihi'
print(dsPTB11)

# Delete - Xóa phần tử danh sách
    # Xóa phần tử bằng giá trị - remove()
# del_item = 'hihi'
# for item in dsPTB11:
#     if item == del_item:
#         dsPTB11.remove(del_item)

    # Xóa phần tử bằng index - pop()
del_index = -100
        # Hàm lấy giá trị tuyệt đối - abs()
if abs(del_index) < len(dsPTB11):
    dsPTB11.pop(del_index)

    # Xóa tất cả phần tử trong danh sách - clear()
# dsPTB11.clear()

print(dsPTB11)

arr_num = [19, -58, 45, 69, 2, 5, 4, -7]
# Sắp xếp phần tử trong danh sách
    # sắp xếp từ nhỏ tới lớn
arr_num.sort()
# dsPTB11.sort()
# print(dsPTB11)
print(arr_num)

    # sắp xếp từ lớn tới nhỏ
arr_num.sort(reverse=True)
print(arr_num)

# Bài tập: Tìm phần tử chung của 2 danh sách
arr1 = []
arr2 = []

        # Thêm phần tử cho 2 danh sách
for i in range(1,11):
    arr1.append(i)
for i in range(5,16):
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