class Node:
    def __init__(self, heso, somu):
        self.heso = heso
        self.somu = somu
        self.next = None

class DaThuc:
    def __init__(self):
        self.head = None

    def themSoHang(self, heso, somu):
        new_node = Node(heso, somu)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def inDaThuc(self):
        current = self.head
        while current:
            print(f"{current.heso}*x^{current.somu}", end="")
            current = current.next
            if current:
                print(" + ", end="")
        print()

    def RutGon(self):
        current = self.head
        while current:
            runner = current.next
            while runner:
                if runner.somu == current.somu:
                    current.heso += runner.heso  
                    current.next = runner.next  
                runner = runner.next
            if current.heso == 0:
                if current == self.head:
                    self.head = current.next
                else:
                    prev.next = current.next
            else:
                prev = current
            current = current.next
    
    def Cong(self, dathuc2):
        result = DaThuc()  
        current1 = self.head
        current2 = dathuc2.head
        while current1 or current2:
            if current1 is None:
                result.themSoHang(current2.heso, current2.somu)
                current2 = current2.next
            elif current2 is None:
                result.themSoHang(current1.heso, current1.somu)
                current1 = current1.next
            elif current1.somu > current2.somu:
                result.themSoHang(current1.heso, current1.somu)
                current1 = current1.next
            elif current1.somu < current2.somu:
                result.themSoHang(current2.heso, current2.somu)
                current2 = current2.next
            else:
                result.themSoHang(current1.heso + current2.heso, current1.somu)
                current1 = current1.next
                current2 = current2.next
        result.RutGon()
        return result
    
    def DoiDau(self):
        current = self.head
        while current:
            current.heso = -current.heso 
            current = current.next
