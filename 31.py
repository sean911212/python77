while True:
    a = list(map(int, input("輸入矩陣的維度:").split()))
    m = a[0]
    n = a[1]
    if type(m) and type(n) == int:
        if m < 10 and m > 0 and n < 10 and n > 0:
            break
        else:
            print("請輸入0到10之間的正整數")
    else:
        print("請輸入0到10之間的正整數")
b = []
while True:
    b = list(map(int, input().split()))
    if len(b) == n:
        break
A = []
A.append(b)
while True:
    b = list(map(int, input().split()))
    if len(b) == n:
        break
A.append(b)

while True:
    b = list(map(int, input().split()))
    if len(b) == n:
        break
B = []
B.append(b)
while True:
    b = list(map(int, input().split()))
    if len(b) == n:
        break
B.append(b)

C = []

for i in range(m):
    k = []
    for j in range(n):
        k.append(A[i][j]*B[i][j])
    C.append(k)

for i in range(m):
    d = ""
    for j in range(n):
        d = d + str(C[i][j]) + " "
    print(d)