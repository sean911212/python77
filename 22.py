data = [[123, 456, 9000],[456, 789, 5000], [789, 888, 6000], [336, 558, 10000], [775, 666, 12000], [556, 221, 7000]]
N = int(input("輸入查詢組數為:"))
list1 = []
for j in range(N):
    a = list(map(int, input().split()))
    b = 0
    for i in range(len(data)):
        if data[i][0] == a[0] and data[i][1] == a[1]:
            list1.append(data[i][2])
            b = 1
            break
        else:
            b = 0
    if b == 0:
        list1.append("error")
for k in range(len(list1)):
    print(list1[k])