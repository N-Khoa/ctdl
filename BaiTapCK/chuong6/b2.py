def Hieu(arr1, arr2):
    # Khởi tạo mảng kết quả rỗng
    result = []
    # Tạo một set từ mảng arr2 để tối ưu việc kiểm tra tồn tại
    set_arr2 = set(arr2)
    # Duyệt qua từng phần tử trong mảng arr1
    for num in arr1:
        # Nếu phần tử không có trong mảng arr2, thêm vào mảng kết quả
        if num not in set_arr2:
            result.append(num)
    
    # Sắp xếp mảng kết quả
    result.sort()
    return result

# Ví dụ sử dụng:
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]

# Tìm các phần tử có trong mảng a nhưng không có trong mảng b
hieu_ab = Hieu(a, b)
print("Các phần tử có trong mảng a nhưng không có trong mảng b:", hieu_ab)
