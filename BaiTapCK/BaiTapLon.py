# Tạo ra 1 lớp để lưu mô tả của một từ trong từ điển.
class MoTa:
    def __init__(self, loaiTu, moTa, viDu):
        self.tuLoai = loaiTu
        self.moTa = moTa
        self.viDu = viDu

# Tạo ra 1 lớp đại diện cho 1 từ trong từ điển
class Tu:
    def __init__(self, tu):
        self.tu = tu
        self.moTa = []

    # Them các nghĩa của từ vào trong 
    def ThemMoTa(self, loaiTu, moTa, viDu):
        moTa = MoTa(loaiTu, moTa, viDu)
        self.moTa.append(moTa)

#T Tạo ra 1 lớp để lưu từ diển
class TuDien:
    def __init__(self):
        self.tuDien = []    #từ điển ban đầu chưa có giá trị nào

    #Thêm 1 từ vào từ điển
    def ThemTu(self, tu, loaiTu=None, moTa=None, viDu=None):
        tuLoai = Tu(tu) #Tạo ra 1 từ trong từ điển - chưa có mô ta
        tuLoai.ThemMoTa(loaiTu, moTa, viDu)  
        self.tuDien.append(tuLoai) # Thêm từ vừa tạo vào từ điển

    # Xóa 1 từ khỏi từ điển
    def LoaiBoTu(self, tuMuonXoa):
        for tuCanXoa in self.tuDien: # Tìm kiếm từ cần xóa trong từ điển
            if tuCanXoa.tu == tuMuonXoa:
                self.tuDien.remove(tuCanXoa)
                return True
        return False

    def TraCuuNghia(self,tuMuonTraCuu):
        for tuCanTra in self.tuDien:
            if tuCanTra.tu == tuMuonTraCuu:
                return tuCanTra.moTa
        return False

    def LuuTuDien(self):
        with open("BaiTapCK/n20dcat030_mang.txt", "a") as file:
            for x in self.tuDien:
                file.write(x.tu + ":\n")
                for y in x.moTa:
                    file.write(f"- {y.tuLoai}: {y.moTa} (Example: {y.viDu})\n")

    def DocFile(self):
        with open("BaiTapCK/n20dcat030_mang.txt", "r") as file:
            lines = file.readlines()
            tuMoi = None
            for line in lines:
                if line.strip() and line.strip()[-1] == ":":
                    tu = line.strip()[:-1]
                    tuMoi = Tu(tu)
                    self.tuDien.append(tuMoi)
                elif tuMoi:
                    parts = line.strip().split(":")
                    if len(parts) == 3:
                        tuLoai = parts[0].strip().strip(" -").strip()
                        moTa = parts[1].strip().rstrip(" (Example")
                        viDu = parts[2].strip().rstrip(")")
                        tuMoi.ThemMoTa(tuLoai, moTa, viDu)

def BaiTapLon():  
    while True:
        print("--------------------------BÀI TẬP LỚN----------------------")
        print("---------------------------Main Menu-----------------------")
        print("1. Thêm một mục từ mới vào từ điển.")
        print("2. Loại bỏ một mục từ của từ điển.")
        print("3. Tra cứu các nghĩa của một mục từ trong từ điển.")
        print("4. Lưu từ điển vào các tập tin.")
        print("5. Nạp từ điển từ các tập tin.")
        print("6. Thoát chương trình.")
        print("------------------------------------------------------------")
        choice = input("Nhập lựa chọn: ")

        if choice == "1":
            tuMuonThem = ""
            while tuMuonThem=="":
                tuMuonThem = input("Nhập từ mà bạn muốn thêm: ")
                if tuMuonThem=="":
                    print("Vui lòng nhập từ muốn thêm vào!")
            loaiTu= input("Nhập loài từ của từ vừa rồi: ")
            moTa = input("Nhập mô tả của từ vừa rồi: ")
            viDu = input("Nhạp ví dụ của từ vừa rôi: ")
            tuDien.ThemTu(tuMuonThem,loaiTu,moTa,viDu)

        elif choice == "2":
            tuMuonXoa = input("Nhập từ mà bạn muốn xóa: ")
            if tuDien.LoaiBoTu(tuMuonXoa):
                print("Đã xóa")
            else:
                print("Từ bạn cần xóa không có trong từ điển")
            
        elif choice == "3":
            tuMuonTraCuu = input("Nhập từ mà bạn muốn Tra cứu nghĩa: ")
            nghia = tuDien.TraCuuNghia(tuMuonTraCuu)
            if nghia:
                print(tuMuonTraCuu)
                for x in nghia:
                    print(f"-{x.tuLoai}: {x.moTa} (Example:{x.viDu})")
            else:
                print("Từ bạn cần tra không có trong từ điển!")

        elif choice == "4":
            tuDien.LuuTuDien()
            print("Đã lưu!")

        elif choice == "5":
            tuDien.DocFile()
            print("Đã đọc!")
        elif choice == "6":
            print("Bạn đã thoát chương trình.")
            break
        else:
            print("Vui lòng nhập một số nguyên!")
            


if __name__ == "__main__":
    tuDien = TuDien()
    BaiTapLon()
