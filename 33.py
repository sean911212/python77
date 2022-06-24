A = []
S = int(input("國文:"))
A.append(S)
S = int(input("英文:"))
A.append(S)
S = int(input("微積分:"))
A.append(S)
S = int(input("體育:"))
A.append(S)
S = int(input("程式設計:"))
A.append(S)
C = ["國文", "英文", "微積分", "體育", "程式設計"]
B = []
for i in range(len(A)):
    B.append(A[i])
for i in range(len(A)):
    for j in range(len(A) - 1):
        if A[i] < A[j]:
            A[i], A[j] = A[j], A[i]
M = A[4]
m = A[0]
avg = 0
total = 0
for i in range(len(A)):
    total += A[i]
avg = total / 5
print("平均分數:%.2f" %(avg))
for i in range(len(A)):
    if M == B[i]:
        print("最高分科目:%s%d分" %(C[i], M))
for i in range(len(A)):
    if m == B[i]:
        print("最低分科目:%s%d分" %(C[i], m))