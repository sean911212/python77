a = list(map(int, input("輸入月及日為:").split()))
print(a)
if a[0] == 1:
    if a[1] < 21:
        print("Capricorn")
    else: print("Aquarius")
elif a[0] == 2:
    if a[1] < 19:
        print("Aquarius")
    else: print("Pisces")
elif a[0] == 3:
    if a[1] < 21:
        print("Pisces")
    else: print("Aries")
elif a[0] == 4:
    if a[1] < 21:
        print("Aries")
    else: print("Taurus")
elif a[0] == 5:
    if a[1] < 22:
        print("Taurus")
    else: print("Gemini")
elif a[0] == 6:
    if a[1] < 22:
        print("Gemini")
    else: print("Cancer")
elif a[0] == 7:
    if a[1] < 23:
        print("Cancer")
    else: print("Leo")
elif a[0] == 8:
    if a[1] < 24:
        print("Leo")
    else: print("Virgo")
elif a[0] == 9:
    if a[1] < 24:
        print("Virgo")
    else: print("Libra")
elif a[0] == 10:
    if a[1] < 24:
        print("Libra")
    else: print("Scorpio")
elif a[0] == 11:
    if a[1] < 23:
        print("Scorpio")
    else: print("Sagittarius")
elif a[0] == 12:
    if a[1] < 22:
        print("Sagittarius")
    else: print("Capricorn")