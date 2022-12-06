def opory(oporniki, r_docelowy, r_z = 0, wybrane = 0, index = 0) -> bool:
    if wybrane == 3:
        if r_docelowy == r_z:
            return True
        else:
            return False
    if index >= len(oporniki):
        return False

    if opory(oporniki, r_docelowy, r_z + oporniki[index], wybrane + 1, index + 1):
        return True
    if wybrane >= 1:
        if opory(oporniki, r_docelowy, r_z*oporniki[index]/(r_z+oporniki[index]), wybrane + 1, index + 1):
            return True
    if opory(oporniki, r_docelowy, r_z, wybrane, index + 1):
        return True
        
    return False
    

T = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(opory(T, 8))
             
    