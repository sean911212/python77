c = 0
A = []
B = ""
while True:
    n = int(input())
    if n > 0 and n < 10 ** 6:
        break
    else:
        print("請輸入1到10的六次方的整數")
while True:
    A.append(n)
    c += 1
    if n == 1:
        break
    if n % 2 == 1:
        n = 3 * n + 1
    else:
        n = n / 2
for i in range(len(A)):
    A[i] = str(int(A[i]))
B = " ".join(A)
print("數列:%s" %B)
print("cycle length為:%d" %c)