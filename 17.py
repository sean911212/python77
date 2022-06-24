list1 = []
list2 = []
a = list(map(int, input().split()))
N1 = a[0]
M1 = a[1]
for i in range(N1):
    while True:
        a = list(map(int, input().split()))
        if len(a) == M1:
            break
        print("請輸入正確數量")
    list1.append(a)
b = list(map(int, input().split()))
N2 = b[0]
M2 = b[1]
for i in range(N2):
    while True:
        b = list(map(int, input().split()))
        if len(b) == M2:
            break
        print("請輸入正確數量")
    list2.append(b)
list3 = list1
if(N1 == N2 and M1 == M2):
    for i in range(N1):
        for j in range(M1):
            list3[i][j] = list1[i][j] + list2[i][j]
            print(str(list3[i][j]) + " ", end="")
        print()
else:
    print("兩陣列不能相加")