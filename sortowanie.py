class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class List:
    def __init__(self):
        self.first = None
        self.last = None
    
    def append(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            self.last.next = Node(value) #type: ignore
            self.last = self.last.next #type: ignore
    
def sortuj(list : List):
    ptr = list.first
    flag = True
    while flag == True:
        flag = False
        if ptr.value > ptr.next.value: #type: ignore
            flag = True
            buff = ptr.next #type: ignore
            ptr.next  