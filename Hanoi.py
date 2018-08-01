def hanoi(scale):
    scale_i = int(scale)
    return int(pow(2, scale_i)) - 1


n = input("Scale:")

print(hanoi(n))
