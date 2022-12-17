class Item:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def czy_parzyste(n : int) -> bool:
    licznik_1 = 0
    while n != 0:
        licznik_1 += n%2
        n //= 2
    return licznik_1 % 2 == 0

global head

def usun(h: Item):
    if h == None:
        return

    while h != None:
        if not czy_parzyste(h.value):
            if h.next == None:
                h.prev.next = None
                h = h.next

            elif h.prev == None:
                h.next.prev = None
                
            else:
                h.prev.next = h.next
                h.next.prev = h.prev
        head = h.next


e1 = Item(7)
e2 = Item(6)
e3 = Item(8)

head = e1
e1.next = e2 # type: ignore
e1.prev = None

e2.next = e3 # type: ignore
e2.prev = e1 # type: ignore

e3.next = None
e3.prev = e2 # type: ignore

usun(head)

while(head is not None):
    print(head.value)
    head = head.next

