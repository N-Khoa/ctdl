# Chúng ta duy trì một danh sách ngan_xep để lưu trữ các ngăn xếp riêng lẻ.
# Khi đẩy các phần tử, chúng ta kiểm tra xem ngăn xếp cuối cùng có đầy đủ hay không hoặc không có ngăn xếp nào tồn tại. Nếu có, chúng ta tạo một ngăn xếp mới và đẩy giá trị vào đó.
# Khi lấy các phần tử, chúng ta lấy phần tử từ ngăn xếp cuối cùng và loại bỏ nếu nó trở thành trống sau khi lấy.
# Phương thức lay_tai cho phép lấy từ một ngăn xếp cụ thể tại chỉ số chi_so.
# Phương thức __str__ được ghi đè để cung cấp một biểu diễn chuỗi của đối tượng SetOfStacks, hữu ích cho việc in trạng thái của các ngăn xếp.

class SetOfStacks:
    def __init__(self, dung_luong):
        self.dung_luong = dung_luong
        self.ngan_xep = []

    def day(self, gia_tri):
        if not self.ngan_xep or len(self.ngan_xep[-1]) >= self.dung_luong:
            self.ngan_xep.append([gia_tri])
        else:
            self.ngan_xep[-1].append(gia_tri)

    def lay(self):
        if not self.ngan_xep:
            return None  
        gia_tri = self.ngan_xep[-1].pop()
        if not self.ngan_xep[-1]: 
            self.ngan_xep.pop()  
        return gia_tri

    def lay_tai(self, chi_so):
        if chi_so < 0 or chi_so >= len(self.ngan_xep):
            return None 
        gia_tri = self.ngan_xep[chi_so].pop()  
        if not self.ngan_xep[chi_so]:  
            self.ngan_xep.pop(chi_so)  
        return gia_tri

    def __str__(self):
        return '\n'.join(map(str, self.ngan_xep))

tap_ngan_xep = SetOfStacks(dung_luong=3)

for i in range(10):
    tap_ngan_xep.day(i)

print(tap_ngan_xep)


print(tap_ngan_xep.lay())  
print(tap_ngan_xep.lay_tai(1))  

print(tap_ngan_xep)
