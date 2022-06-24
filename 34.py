while True:
    a = int(input("輸入一正整數:"))
    if a < 11 or a > 1000:
        print("請輸入11到1000的整數")
    else:
        break
if a % 2 == 0 and a % 11 == 0 and a % 5 != 0 and a % 5 != 7:
    print("%d為新公倍數?:Yes" %a)
else:
    print("%d為新公倍數?:No" %a)