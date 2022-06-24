x = int(input("X軸座標:"))
y = int(input("Y軸座標:"))
a = x*x + y*y
if x == 0 and y == 0:
    print("該點為原點")
elif x > 0 and y > 0:
    print("該點位於第一象限，離原點距離為根號%d" %a)
elif x < 0 and y > 0:
    print("該點位於第二象限，離原點距離為根號%d" %a)
elif x < 0 and y < 0:
    print("該點位於第三象限，離原點距離為根號%d" %a)
elif x > 0 and y < 0:
    print("該點位於第四象限，離原點距離為根號%d" %a)
elif x == 0:
    print("該點位於y軸上，離原點距離為根號%d" %a)
elif y == 0:
    print("該點位於x軸上，離原點距離為根號%d" %a)