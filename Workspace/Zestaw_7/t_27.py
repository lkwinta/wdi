class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def dodaj(h : Node, t : Node, x : int) -> (Node, Node):
    if h == None:
        h = Node(x)
        t = h
        return (h,t)
    else:
        t.next = Node(x) # type: ignore
        t = t.next
        return (h,t)

def scal(T1, T2):
    l1 = len(T1)
    l2 = len(T2)
    i1 = 0
    i2 = 0

    head = None
    tail = None

    while i1 < l1 and i2 < l2:
        if T1[i1] < T2[i2]:
            (head, tail) = dodaj(head, tail, T1[i1]) # type: ignore
            i1 += 1
        else:
            (head, tail) = dodaj(head, tail, T1[i1]) # type: ignore
            i2 += 1
        
    while i1 < l1:
        (head, tail) = dodaj(head, tail, T1[i1]) # type: ignore
        i1 += 1
    
    while i2 < l2:
        (head, tail) = dodaj(head, tail, T2[i2]) #type: ignore
        i2 += 1
    
    return (head, tail)

T1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
T2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

(h, t) = scal(T1, T2)

while(h is not None):
    print(h.value)
    h = h.next
