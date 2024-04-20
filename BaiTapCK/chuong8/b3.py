class TuDien:
    def __init__(self):
        self.albums = {}

    def NhapAlbum(self, ten_album, danh_sach_bai_hat):
        self.albums[ten_album] = danh_sach_bai_hat

    def XemAlbum(self, ten_album):
        if ten_album in self.albums:
            print(f"Thông tin album '{ten_album}':")
            for i, bai_hat in enumerate(self.albums[ten_album], start=1):
                print(f"Bài hát {i}:")
                print(f"  Tên bài hát: {bai_hat['ten']}")
                print(f"  Nhạc sĩ sáng tác: {bai_hat['nhac_si']}")
                print(f"  Ca sĩ: {bai_hat['ca_si']}")
        else:
            print(f"Album '{ten_album}' không tồn tại trong từ điển.")

# Ví dụ sử dụng:
tudien = TuDien()

# Nhập thông tin các album
tudien.NhapAlbum("Những bài hát hay nhất của Sơn Tùng M-TP", [
    {"ten": "Em của ngày hôm qua", "nhac_si": "Sơn Tùng M-TP", "ca_si": "Sơn Tùng M-TP"},
    {"ten": "Chạy ngay đi", "nhac_si": "Sơn Tùng M-TP", "ca_si": "Sơn Tùng M-TP"},
    {"ten": "Nơi này có anh", "nhac_si": "Sơn Tùng M-TP", "ca_si": "Sơn Tùng M-TP"}
])

tudien.NhapAlbum("Những ca khúc bất hủ của Tuấn Hưng", [
    {"ten": "Bình yên những phút giây", "nhac_si": "Tuấn Hưng", "ca_si": "Tuấn Hưng"},
    {"ten": "Đến giờ phút này", "nhac_si": "Tuấn Hưng", "ca_si": "Tuấn Hưng"},
    {"ten": "Chỉ còn những mùa nhớ", "nhac_si": "Tuấn Hưng", "ca_si": "Tuấn Hưng"}
])

# Xem thông tin album
tudien.XemAlbum("Những bài hát hay nhất của Sơn Tùng M-TP")
tudien.XemAlbum("Những ca khúc bất hủ của Tuấn Hưng")
tudien.XemAlbum("Album không tồn tại")
