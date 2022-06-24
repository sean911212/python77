a = list(map(int, input("輸入N及M為:").split()))
b = []
c = []
N = a[0]
M = a[1]
for i in range(N):
    while True:
        x = list(map(int, input("輸入矩陣值第%d列為:" %(i + 1)).split()))
        if len(x) == M:
            break
        print("請輸入正確數量")
    b.append(x)
for i in range(M):
    d = []
    for j in range(N):
        d.append(str(b[j][i]))
    s = " ".join(d)
    print("輸出矩陣值第%d列為%s" %(i + 1, s))