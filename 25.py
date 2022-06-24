while True:
    a = list(map(int, input("請輸入考試次數及學生人數:").split()))
    if len(a) < 10:
        break
    print("考試次數或學生人數錯誤！")
stScore = []
stAvg = []
stAvgTotal = 0
Avg = 0
b = list(map(float, input("每次考試所占的比率:").split()))
for i in range(a[1]):
    c = list(map(int, input().split()))
    stScore.append(c)
    for j in range(a[0]):
        stAvg.append(round(stScore[i][j] * b[j], 2)) 
for i in range(len(stAvg)):
    stAvgTotal += stAvg[i]
Avg = round(stAvgTotal / a[1], 2)
print("全班平均%.2f" %Avg)