def Giao(arr1, arr2):
    # Khởi tạo mảng kết quả rỗng
    result = []
    # Tạo một set từ mảng arr1 để tối ưu việc kiểm tra tồn tại
    set_arr1 = set(arr1)
    # Duyệt qua từng phần tử trong mảng arr2
    for num in arr2:
        # Nếu phần tử có trong cả mảng arr1 và không trùng với các phần tử đã thêm vào mảng kết quả, thêm vào mảng kết quả
        if num in set_arr1 and num not in result:
            result.append(num)
    
    # Sắp xếp mảng kết quả
    result.sort()
    return result

# Ví dụ sử dụng:
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]

# Tìm các phần tử có trong cả mảng a và mảng b
giao_ab = Giao(a, b)
print("Các phần tử có trong cả mảng a và mảng b:", giao_ab)
