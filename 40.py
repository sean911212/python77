a = int(input())
k = 1
if a % 2 == 1:
    for i in range(1, a + 1):
        if i != (a + 1) // 2:
            print(" " * ((a - 1) // 2), end="")
            print(k)
            k += 2
        else:
            for j in range(1, a + 2, 2):
                print(j, end="")
                k = 1
        if i == (a + 1) // 2:
            for j in range(1, a, 2):
                print(j, end="")
            print()