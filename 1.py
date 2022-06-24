a = list(str(input("請輸入正整數：")))
b = []
s = ""
s1 = 0
for j in range(len(a)):
    s = ""
    for i in range(j, len(a)):
        s += a[i]
        s1 = int(s)
        c = 0
        if s1 > 1:
            for i in range(2, s1):
                if s1 % i == 0:
                    c = 0
                    break
                else: c = 1
            if c == 1:
                b.append(s1)
for j in range(len(b)):
    for i in range(len(b) - 1):
        if b[i] < b[i + 1]:
            b[i], b[i + 1] = b[i + 1], b[i]
if b == []:
    print("No prime found")
else:
    print("子字串中最大的質數是%d" %b[0])