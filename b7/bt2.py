# Chúng ta duy trì một ngăn xếp phụ được gọi là min_stack để theo dõi các phần tử tối thiểu gặp phải cho đến nay.
# Khi đẩy một phần tử mới vào ngăn xếp chính:
# Chúng ta so sánh nó với phần tử đầu tiên của min_stack.
# Nếu phần tử mới nhỏ hơn hoặc bằng phần tử đầu tiên của min_stack, chúng ta cũng đẩy nó vào min_stack.
# Khi lấy một phần tử ra khỏi ngăn xếp chính:
# Chúng ta kiểm tra xem phần tử được lấy ra có phải là tối thiểu hiện tại không.
# Nếu đúng, chúng ta cũng lấy ra phần tử đầu tiên của min_stack.
# Hàm min() đơn giản trả về phần tử đầu tiên của min_stack, đại diện cho phần tử tối thiểu hiện tại trong ngăn xếp.

class MinStack:
    def __init__(self):
        self.stack = []  
        self.min_stack = []  
    def day(self, gia_tri):
        self.stack.append(gia_tri)  
        if not self.min_stack or gia_tri <= self.min_stack[-1]:
            self.min_stack.append(gia_tri)  

    def lay(self):
        if not self.stack:
            return None
        gia_tri = self.stack.pop() 
        if gia_tri == self.min_stack[-1]: 
            self.min_stack.pop()  
        return gia_tri

    def min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]  

ngan_xep = MinStack()
ngan_xep.day(5)
ngan_xep.day(3)
ngan_xep.day(8)
ngan_xep.day(2)

print(ngan_xep.min())  
ngan_xep.lay()

print(ngan_xep.min())  


