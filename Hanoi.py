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
        while C != sample_list:
            if min(A) < min(C):
                C.append(min(A))
                A.pop()
                time += 1
                print(time, ": Move no.", min(C), "plate from A to C")
                break
            elif min(A) > min(C):
                A.append(min(C))
                C.pop()
                time += 1
                print(time, ": Move no.", min(A), "plate from C to A")
                break
        while C != sample_list:
            if min(A) < min(B):
                B.append(min(A))
                A.pop()
                time += 1
                print(time, ": Move no.", min(B), "plate from A to B")
                break
            elif min(A) > min(B):
                A.append(min(B))
                B.pop()
                time += 1
                print(time, ": Move no.", min(A), "plate from B to A")
                break
        while C != sample_list:
            if min(B) < min(C):
                C.append(min(B))
                B.pop()
                time += 1
                print(time, ": Move no.", min(C), "plate from B to C")
                break
            elif min(B) > min(C):
                B.append(min(C))
                C.pop()
                time += 1
                print(time, ": Move no.", min(B), "plate from C to B")
                break

elif n % 2 == 0:
    while C != sample_list:
        while C != sample_list:
            if min(A) < min(B):
                B.append(min(A))
                A.pop()
                time += 1
                print(time, ": Move no.", min(B), "plate from A to B")
                break
            elif min(A) > min(B):
                A.append(min(B))
                B.pop()
                time += 1
                print(time, ": Move no.", min(A), "plate from B to A")
                break
        while C != sample_list:
            if min(A) < min(C):
                C.append(min(A))
                A.pop()
                time += 1
                print(time, ": Move no.", min(C), "plate from A to C")
                break
            elif min(A) > min(C):
                A.append(min(C))
                C.pop()
                time += 1
                print(time, ": Move no.", min(A), "plate from C to A")
                break
        while C != sample_list:
            if min(B) < min(C):
                C.append(min(B))
                B.pop()
                time += 1
                print(time, ": Move no.", min(C), "plate from B to C")
                break
            elif min(B) > min(C):
                B.append(min(C))
                C.pop()
                time += 1
                print(time, ": Move no.", min(B), "plate from C to B")
                break

print("Moving", n, "plates needs", time, "times")
