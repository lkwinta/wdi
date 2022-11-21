first = 1
second = 1
current = first + second

print(first)
print(second)

while current < 1000000:
    print(current)
    first = second
    second = current
    current = first + second
    
