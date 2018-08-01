def hanoi(scale):
    scale_i = int(scale)
    if scale_i == 1:
        result = 1
    else:
        result = hanoi(1) + 2 * hanoi(scale_i - 1)
    return int(result)


n = input("Scale:")

print(hanoi(n))
