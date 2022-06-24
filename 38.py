while True:
    n = int(input())
    if n < 2 or n > 10:
        print("請輸入2到10的整數")
    else:
        break
m = []
for i in range(n):
    while True:
        k = int(input())
        if k < 1 or n > 100:
            print("請輸入1到100的整數")
        else:
            break
    m.append(k)
d = 0
for i in range(len(m)):
    if m[i] % 9 == 0 or m[i] % 11 == 0:
        print("第%d的點%d" %(i, m[i]))
        d = 1
if d == 0:
    print(0)