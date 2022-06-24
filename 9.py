b = list(str(input("輸入s1為:")))
a = list(str(input("輸入s2為:")))
b1 = "".join(b)
s = ""
for i in range(len(a)):
    if a[i] == b[0]:
        for j in range(len(b)):
            if a[i] == b[j]:
                s += a[i]
                i += 1
            else:
                s = ""
                break
    if s == b1:
        break
if s == b1:
    print("YES")
else:
    print(s)
    print("NO")