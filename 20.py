a = int(input("組數為:"))
for i in range(a):
    b = list(map(int, input().split()))
    print("第%d組應收費用:%d" %(i + 1, b[0] * 250 + b[1] * 175))