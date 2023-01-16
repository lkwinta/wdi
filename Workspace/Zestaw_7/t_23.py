class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def policz(poczatek : Node):
    a = poczatek
    while a is not None:
        a = a.next