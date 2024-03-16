# Chúng ta sử dụng hai ngăn xếp stack_push và stack_pop để thêm phần tử vào và loại bỏ phần tử từ hàng đợi.
# Khi cần loại bỏ một phần tử từ hàng đợi (pop), chúng ta chuyển tất cả các phần tử từ stack_push sang stack_pop trước khi loại bỏ phần tử đầu tiên của stack_pop. Điều này đảm bảo rằng các phần tử được loại bỏ theo thứ tự đúng của hàng đợi.
# Phương thức is_empty được triển khai để kiểm tra xem hàng đợi có trống không.
# Phương thức __str__ được ghi đè để cung cấp một biểu diễn chuỗi của đối tượng hàng đợi, hữu ích để in trạng thái của hàng đợi.

class QueueUsingStacks:
    def __init__(self):
        self.stack_push = []  
        self.stack_pop = [] 

    def push(self, value):
        self.stack_push.append(value)  

    def pop(self):
        if not self.stack_pop: 
            if not self.stack_push:  
                return None  
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
        return self.stack_pop.pop()  

    def is_empty(self):
        return not self.stack_push and not self.stack_pop  

    def __str__(self):
        return "Push Stack: " + str(self.stack_push) + "\nPop Stack: " + str(self.stack_pop)



queue = QueueUsingStacks()

queue.push(1)
queue.push(2)
queue.push(3)

print(queue)

print(queue.pop())  
print(queue.pop())  

queue.push(4)

print(queue)

print(queue.pop())  
print(queue.pop())  
print(queue.pop()) 
