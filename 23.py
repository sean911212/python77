n = 0
while n != -1:
    n = int(input("輸入值n為:"))
    if n > 0:
        print(round(n*n*n/3, 1))
    else:
        if n != -1:
            print("請輸入正整數")