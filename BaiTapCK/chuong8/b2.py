class TuDien:
    def __init__(self):
        self.tudien = {}

    def NhapTu(self, tu, dongnghia=None, trai_nghia=None):
        key = tu[0].lower()
        if key not in self.tudien:
            self.tudien[key] = {'tu': tu, 'dongnghia': set(), 'trai_nghia': set()}
        if dongnghia:
            self.tudien[key]['dongnghia'].add(dongnghia)
        if trai_nghia:
            self.tudien[key]['trai_nghia'].add(trai_nghia)

    def DongNghia(self, tu):
        key = tu[0].lower()
        if key in self.tudien:
            return self.tudien[key]['dongnghia']
        else:
            return []

    def TraiNghia(self, tu):
        key = tu[0].lower()
        if key in self.tudien:
            return self.tudien[key]['trai_nghia']
        else:
            return []

# Ví dụ sử dụng:
tudien = TuDien()

# Nhập từ vào từ điển
tudien.NhapTu('bóng đá', 'football', 'volleyball')
tudien.NhapTu('chó', 'dog', 'cat')
tudien.NhapTu('mèo', 'cat', 'dog')

# Tra từ đồng nghĩa
tu_dongnghia = tudien.DongNghia('bóng đá')
print("Từ đồng nghĩa của 'bóng đá':", tu_dongnghia)

# Tra từ trái nghĩa
tu_trai_nghia = tudien.TraiNghia('chó')
print("Từ trái nghĩa của 'chó':", tu_trai_nghia)
