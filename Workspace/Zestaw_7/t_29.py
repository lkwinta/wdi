class Node:
    def __init__(self, value):
        self.next = None
        self.previous = None
        self.value = value

head1 = Node(-1000)
head2 = Node(-1000)

#1 2 4 6 9
#1 4 7 8 9

def usun(head1, head2):
    ptr1 = head1.next
    ptr2 = head2.next

    while ptr1 != None and ptr2 != None:
        while ptr1 != None and ptr2 != None and ptr1.value < ptr2.value:
            ptr1.previous.next = ptr1.next
            ptr1 = ptr1.next
        
        while ptr1 != None and ptr2 != None and ptr1.value > ptr2.value:
            ptr2.previous.next = ptr2.next
            ptr2 = ptr2.next

        else:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

def add(head, val):
    ptr = head
    while ptr.next != None:
        ptr = ptr.next
    
    ptr.next = Node(val)
    ptr.next.previous = ptr


add(head1, 1)
add(head1, 2)
add(head1, 3)
add(head1, 6)
add(head1, 9)

add(head12, 1)
add(head2, 4)
add(head2, 7)
add(head1, 8)
add(head1, 9)

def wypisz(head):
    ptr = head.next

    while ptr != None:
        print(f"{ptr.value}", end= ' ')
        ptr = ptr.next

    print("\n")

wypisz(head1)
wypisz(head2)