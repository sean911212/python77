T = int(input())
for i in range(T):
    A = []
    for j in range(4):
        a = int(input())
        A.append(a)
    for i in range(4):
        for j in range(3):
            if A[i] < A[j]:
                A[i], A[j] = A[j], A[i]
    d = A[1] - A[0]
    k = A[1] / A[0]
    c = 0
    e = 0
    for x in range(1, 4):
        if A[x] - A[x - 1] == d:
            c = 1
        else:
            c = 0
            break
    for x in range(1, 4):
        if A[x] / A[x - 1] == k:
            e = 1
        else:
            e = 0
            break
    for i in range(4):
        A[i] = str(A[i])
    if c == 1 or e == 1:
        if c == 1 and e == 1:
            A.append(str(int(A[3]) + d))
            print(" ".join(A))
            print("此為等差也是等比數列")
        elif e == 0:
            A.append(str(int(A[3]) + d))
            print(" ".join(A))
            print("此為等差數列")
        elif c == 0:
            A.append(str(int(A[3]) * int(k)))
            print(" ".join(A))
            print("此為等比數列")
    else:
        print("不為等比或等差數列")