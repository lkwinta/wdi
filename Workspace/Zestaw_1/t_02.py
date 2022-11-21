start = 1

while start < 2022: 
    first = start
    second = first
    current = first + second

    while current < 2022:
        first = second
        second = current
        current = first + second
    
    if current == 2022:
        break
    
    start = start + 1

print(start)