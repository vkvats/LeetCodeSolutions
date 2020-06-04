def addBinary(a,b):
    a, b = int(a, 2), int(b, 2)
    return bin(a + b).replace("0b", "")