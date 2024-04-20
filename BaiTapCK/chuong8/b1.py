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

    def TraTu(self, tu):
        key = tu[0].lower()
        if key in self.tudien:
            return self.tudien[key]['dongnghia'], self.tudien[key]['trai_nghia']
        else:
            return None, None

# Ví dụ sử dụng:
tudien = TuDien()

# Nhập từ vào từ điển
tudien.NhapTu('bóng đá', 'football', 'volleyball')
tudien.NhapTu('chó', 'dog', 'cat')
tudien.NhapTu('mèo', 'cat', 'dog')

# Tra từ trong từ điển
tu_dongnghia, tu_trai_nghia = tudien.TraTu('bóng đá')
if tu_dongnghia:
    print("Từ đồng nghĩa của 'bóng đá':", tu_dongnghia)
else:
    print("Không có từ đồng nghĩa của 'bóng đá'.")

if tu_trai_nghia:
    print("Từ trái nghĩa của 'bóng đá':", tu_trai_nghia)
else:
    print("Không có từ trái nghĩa của 'bóng đá'.")
