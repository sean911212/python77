a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = 1 / (a[0]*b[1] - a[1]*b[0])
a[0], b[1] = c*b[1], c*a[0]
a[1], b[0] = c*(-a[1]), c*(-b[0])
print("%.1f %.1f" %(a[0], a[1]))
print("%.1f %.1f" %(b[0], b[1]))