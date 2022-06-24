data = [[123, "Tom", "DTGD"],[456, "Cat", "CSIE"], [789, "Nana", "ASIE"], [321, "Lim", "DBA"], [654, "Won", "FDD"]]
a = int(input("輸入查詢的學號為:"))
b = 0
for i in range(len(data)):
    if data[i][0] == a:
        s = str(data[i][0]) + " " + data[i][1] + " " + data[i][2]
        print("學生資料為:%s" %s)
        b = 1
        break
    else:
        b = 0
if b == 0:
    print("找不到該學生")