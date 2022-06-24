a = int(input("請輸入陣列大小:"))
list1 = []
list2 = []
list3 = []
max = 0
for k in range(a):
    list2 = []
    for q in range(a):
        list2.append(0)
    list1.append(list2)
list2 = []
for i in range(a):
    b = list(map(int, input().split()))
    for j in range(a):
        list1[i][j] = b[j]
        list2.append(b[j])
for i in range(len(list2) - 1, -1, -1):
    for j in range(len(list2) - 1, -1, -1):
        if list2[i] < list2[j]:
            list2[i], list2[j] = list2[j], list2[i]
for i in range(a):
    max += list2[i]
print(list2)
print("最大值為:%d" %max)
for i in range(a):
    for j in range(a):
        for k in range(a):
            if list2[i] == list1[j][k]:
                list3.append("(%d,%d)" %(j + 1, k + 1))
s = ""
for i in range(len(list3)):
    s += list3[i] + " "
print("位置為:%s" %s)