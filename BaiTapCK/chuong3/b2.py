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