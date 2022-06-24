a = int(input("輸入一組四位數字為:"))
a = list(str(a))
for i in range(len(a)):
    a[i] = (int(a[i]) + 7) % 10
c = 0
d = 0
c, d = a[0], a[1]
a[0], a[1] = a[2], a[3]
a[2], a[3] = c, d
b = ""
for i in range(len(a)):
    b += str(a[i])
print("輸出加密後的數字為:%s" %b)