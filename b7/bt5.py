# Chúng ta duy trì hai hàng đợi, hang_doi_cho và hang_doi_mèo, để chứa chó và mèo tương ứng.
# Khi một con vật được thêm vào, chúng ta thêm một tuple chứa loại vật thể và thứ tự đến nơi vào hàng đợi tương ứng.
# Đối với các phép thao tác làm cấy, làm_cấy trả về con vật cũ nhất, bất kể loại nào. Nó kiểm tra xem hàng đợi nào (chó hoặc mèo) có con vật cũ nhất dựa trên thứ tự đến nơi và trả về con vật đó từ hàng đợi đó.
# làm_cấy_chó và làm_cấy_mèo trả về chó và mèo cũ nhất từ hàng đợi của chúng.

class TrạiThú:
    def __init__(self):
        self.hang_doi_cho = []  
        self.hang_doi_mèo = [] 
        self.thu_tu = 0  

    def nhận_trại(self, loại):
        if loại == "chó":
            self.hang_doi_cho.append((loại, self.thu_tu))
        elif loại == "mèo":
            self.hang_doi_mèo.append((loại, self.thu_tu))
        self.thu_tu += 1

    def làm_cấy(self):
        if not self.hang_doi_cho and not self.hang_doi_mèo:
            return None
        elif not self.hang_doi_cho:
            return self.hang_doi_mèo.pop(0)[0]  
        elif not self.hang_doi_mèo:
            return self.hang_doi_cho.pop(0)[0]  
        else:
            if self.hang_doi_cho[0][1] < self.hang_doi_mèo[0][1]:
                return self.hang_doi_cho.pop(0)[0]  #
            else:
                return self.hang_doi_mèo.pop(0)[0]  

    def làm_cấy_chó(self):
        if not self.hang_doi_cho:
            return None  
        return self.hang_doi_cho.pop(0)[0] 

    def làm_cấy_mèo(self):
        if not self.hang_doi_mèo:
            return None  
        return self.hang_doi_mèo.pop(0)[0]  


# Sử dụng ví dụ:
trại = TrạiThú()
trại.nhận_trại("chó")
trại.nhận_trại("mèo")
trại.nhận_trại("chó")
trại.nhận_trại("mèo")

print(trại.làm_cấy())  
print(trại.làm_cấy_chó()) 
print(trại.làm_cấy_mèo())  
