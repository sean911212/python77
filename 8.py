while True:
    a = int(input("輸入第一行正整數為:"))
    b = list(map(int, input("第二行中數列中的數字為:").split()))
    if len(b) == a:
        break
    print("請輸入正確的正整數數量")



#每個數字出現的次數
c = []
for i in range(0, len(b)):
    k = 0
    for j in range(0, len(b)):
        if b[i] == b[j]:
            k += 1
    c.append(k)
p = []
for i in range(len(c)):
    p.append(c[i])



#排列取得最大值
for i in range(len(c)):
    for j in range(len(c) - 1):
        if c[j] < c[j + 1]:
            c[j], c[j + 1] = c[j + 1], c[j]



#保留出現次數最大數字
d = []
for i in range(0, len(b)):
    if p[i] == c[0]:
        d.append(b[i])



#判斷數列中每個數字是否剛好皆出現一次
e = 0
for i in range(0, len(d)):
    for j in range(0, len(d)):
        if d[i] == d[j]:
            e += 1
    if e != 1:
        break
    else:
        e = 0



#刪掉重複數字
h = []
for i in d:
    if i not in h:
        h.append(i)



#串列轉字串
x = ''
for i in range(0, len(h)):
    x += str(h[i]) + " "



#結果
if e == 0:
    print("每個數字剛好只出現一次")
else:
    print("最大出現次數的數字為%s" %x)
    print("出現次數為%d" %c[0])