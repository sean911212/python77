a = list(str(input("輸入一字元為:")))
b = ""
for i in range(len(a) - 1, -1, -1):
    b += a[i]
a = "".join(a)
if b == a:
    print("YES")
else: print("NO")