def Hop(arr1, arr2):
    # Khởi tạo mảng kết quả rỗng
    result = []
    # Tạo một set từ mảng arr1 để tối ưu việc kiểm tra tồn tại
    set_arr1 = set(arr1)
    # Duyệt qua từng phần tử trong mảng arr1
    for num in arr1:
        # Nếu phần tử chưa tồn tại trong mảng kết quả, thêm vào
        if num not in result:
            result.append(num)
    
    # Duyệt qua từng phần tử trong mảng arr2
    for num in arr2:
        # Nếu phần tử chưa tồn tại trong mảng kết quả, thêm vào
        if num not in result:
            result.append(num)
    
    # Sắp xếp mảng kết quả
    result.sort()
    return result

# Ví dụ sử dụng:
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]

# Tìm các phần tử có trong mảng a hoặc mảng b
hop_ab =Hop(a, b)
print("Các phần tử có trong mảng a hoặc mảng b:", hop_ab)
