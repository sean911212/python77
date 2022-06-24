while True:
    M = int(input("小明身上有幾元:"))
    if M <= 0 or M >= 100:
        print("請輸入0到100的整數")
    else:
        break
while True:
    N = int(input("販賣機有幾種飲料:"))
    if N <= 1 or N >= 30:
        print("請輸入0到100的整數")
    else:
        break
a = 0
for i in range(N):
    P = int(input())
    if P <= M:
        a += 1
print(a)