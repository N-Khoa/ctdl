# 1. Chia danh sách thành ba phần: Bạn sẽ chia danh sách Python thành ba phần bằng cách chia độ dài danh sách cho ba. Điều này sẽ tạo ra ba phần có độ dài gần bằng nhau.

# 2. Sử dụng các chỉ số cho mỗi ngăn xếp: Bạn sẽ sử dụng các chỉ số để xác định vị trí của các phần của từng ngăn xếp trong danh sách. Ví dụ, ngăn xếp đầu tiên sẽ sử dụng chỉ số từ 0 đến kích thước ngăn xếp - 1, ngăn xếp thứ hai sẽ sử dụng các chỉ số từ kích thước ngăn xếp đến 2 * kích thước ngăn xếp - 1, và tương tự cho ngăn xếp thứ ba.

# 3. Triển khai các hoạt động cơ bản: Bạn sẽ cần triển khai các hoạt động cơ bản như push (đẩy), pop (lấy ra), peek (xem), và kiểm tra xem ngăn xếp có trống không.

class BaNganXep:
    def __init__(self, kich_thuoc):
        self.danh_sach = [None] * kich_thuoc * 3
        self.kich_thuoc = kich_thuoc
        self.chi_so = [0, kich_thuoc, 2 * kich_thuoc]

    def day(self, ngan_xep, gia_tri):
        if self.chi_so[ngan_xep] < self.chi_so[ngan_xep] + self.kich_thuoc:
            self.danh_sach[self.chi_so[ngan_xep]] = gia_tri
            self.chi_so[ngan_xep] += 1
        else:
            print("Tràn ngăn xếp.")

    def lay(self, ngan_xep):
        if self.chi_so[ngan_xep] > ngan_xep * self.kich_thuoc:
            self.chi_so[ngan_xep] -= 1
            return self.danh_sach[self.chi_so[ngan_xep]]
        else:
            print("Ngăn xếp trống.")

    def xem(self, ngan_xep):
        if self.chi_so[ngan_xep] > ngan_xep * self.kich_thuoc:
            return self.danh_sach[self.chi_so[ngan_xep] - 1]
        else:
            print("Ngăn xếp trống.")

    def rong(self, ngan_xep):
        return self.chi_so[ngan_xep] == ngan_xep * self.kich_thuoc


# Sử dụng ví dụ:
kich_thuoc_ngan_xep = 5
ba_ngan_xep = BaNganXep(kich_thuoc_ngan_xep)

ba_ngan_xep.day(0, 1)
ba_ngan_xep.day(0, 2)
ba_ngan_xep.day(1, 10)
ba_ngan_xep.day(2, 100)

print(ba_ngan_xep.xem(0))  
print(ba_ngan_xep.lay(1))   
print(ba_ngan_xep.rong(2))  