a = list(str(input()))
while True:
    b = list(str(input()))
    if "".join(b) == "0000":
        break
    A = 0
    B = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if int(a[i]) == int(b[j]):
                if i == j:
                    A += 1
                else:
                    B += 1
    print("%dA%dB" %(A, B))