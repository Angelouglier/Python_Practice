def swag(a, b):
    global time
    if min(a) < min(b):
        b.append(min(a))
        a.pop()
        time += 1
        return True
    return False


time = 0
n = int(input("Number of plates:"))
A = [n+1]
B = [n+1]
C = [n+1]
sample_list = [n+1]

for i in range(1, n+1):
    A.append(i)
    sample_list.append(i)
A.sort(reverse=True)
sample_list.sort(reverse=True)

if n % 2 == 1:
    while C != sample_list:
        if C != sample_list:
            if swag(A, C):
                print(time, ": Move no.", min(C), "plate from A to C")
            elif swag(C, A):
                print(time, ": Move no.", min(A), "plate from C to A")
        if C != sample_list:
            if swag(A, B):
                print(time, ": Move no.", min(B), "plate from A to B")
            elif (swag(B, A)):
                print(time, ": Move no.", min(A), "plate from B to A")
        if C != sample_list:
            if swag(B, C):
                print(time, ": Move no.", min(C), "plate from B to C")
            elif swag(C, B):
                print(time, ": Move no.", min(B), "plate from C to B")

elif n % 2 == 0:
    while C != sample_list:
        if C != sample_list:
            if swag(A, B):
                print(time, ": Move no.", min(B), "plate from A to B")
            elif (swag(B, A)):
                print(time, ": Move no.", min(A), "plate from B to A")
        if C != sample_list:
            if swag(A, C):
                print(time, ": Move no.", min(C), "plate from A to C")
            elif swag(C, A):
                print(time, ": Move no.", min(A), "plate from C to A")
        if C != sample_list:
            if swag(B, C):
                print(time, ": Move no.", min(C), "plate from B to C")
            elif swag(C, B):
                print(time, ": Move no.", min(B), "plate from C to B")

print("Moving", n, "plates needs", time, "times")
