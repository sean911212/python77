a = int(input("輸入一個度數(正整數):"))
if a <= 120:
    print("Summer month:%.2f\nNon-Summer month:%.2f" %(a * 2.10, a * 2.10))
elif a >= 121 and a <= 330:
    b = a - 120
    print("Summer month:%.2f\nNon-Summer month:%.2f" %(b * 3.02 + 120 * 2.10, b * 2.68 + 120 * 2.10))
elif a >= 331 and a <= 500:
    b = a - 120 - 210
    print("Summer month:%.2f\nNon-Summer month:%.2f" %(b * 4.39 + 120 * 2.10 + 210 * 3.02, b * 3.61 + 120 * 2.10 + 210 * 2.68))
elif a >= 507 and a <= 700:
    b = a - 120 - 210 - 170
    print("Summer month:%.2f\nNon-Summer month:%.2f" %(b * 4.97 + 120 * 2.10 + 210 * 3.02 + 170 * 4.39, b * 4.01 + 120 * 2.10 + 210 * 2.68 + 170 * 3.61))
else:
    b = a - 120 - 210 - 170 - 194
    print("Summer month:%.2f\nNon-Summer month:%.2f" %(a * 5.63 + 120 * 2.10 + 210 * 3.02 + 170 * 4.9 + 194 * 4.97, a * 4.50 + 120 * 2.10 + 210 * 2.68 + 170 * 3.61 + 194 * 4.01 ))