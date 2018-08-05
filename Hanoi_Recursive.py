def hanoi(scale, a, b, c):
    scale_i = int(scale)
    global time
    if scale_i == 1:
        time += 1
        print(time, ": Move no.", scale_i, "plate from", a, "to", c)
    else:
        hanoi(scale_i - 1, a, c, b)
        time += 1
        print(time, ": Move no.", scale_i, "plate from", a, "to", c)
        hanoi(scale_i - 1, b, a, c)


time = 0
n = input("Number of plates:")

hanoi(n, 'A', 'B', 'C')

print("Moving", n, "plates needs", time, "times")
