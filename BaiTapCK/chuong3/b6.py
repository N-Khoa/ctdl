class Node:
    def __init__(self, heso, somu):
        self.heso = heso
        self.somu = somu
        self.next = None

class DaThuc:
    def __init__(self):
        self.head = None

    class Node:
        def __init__(self, heso, somu):
            self.heso = heso
            self.somu = somu
            self.next = None

    def themSoHang(self, heso, somu):
        new_node = self.Node(heso, somu)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def Chep(self):
        copied_dathuc = DaThuc()
        current = self.head
        while current:
            copied_dathuc.themSoHang(current.heso, current.somu)
            current = current.next
        return copied_dathuc

    def inDaThuc(self):
        current = self.head
        while current:
            print(f"{current.heso}*x^{current.somu}", end="")
            current = current.next
            if current:
                print(" + ", end="")
        print()


