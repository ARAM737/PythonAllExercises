from math import sin, cos, e, log1p, tan, fabs

##1.1
print("Задача 1.1")


def f1(x, y):
    return (y ** 8 - sin(y)) ** 3 - x ** 6 / 46 - (e ** y - y ** 3 + 67) / (y ** 6 + y ** 3) - (
            41 * y ** 7 - 39 * x ** 5 - 1) / (88 * x ** 8 + 87 * y ** 4)


print("{:.2e}".format(f1(-51, -26)))
print("{:.2e}".format(f1(-42, -3)))

# 1.2
print("Задача 1.2")


def f2(x):
    if x < -50:
        return 30 * (x / 46 - x ** 5 + 94) ** 5 - x ** 6
    if -50 <= x < 26:
        return (x ** 6 + x ** 3) ** 7 / 73 - log1p(x)
    if 26 <= x < 52:
        return fabs(39 * x ** 3) + tan(x)
    if x >= 52:
        return 99 * (30 * x ** 6 + 68 * x ** 2) ** 3 - 54 * x ** 5


print("{:.2e}".format(f2(-68)))
print("{:.2e}".format(f2(22)))

# 1.3
print("Задача 1.3")


def f31(n, m):
    sum1 = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            sum1 += (cos(j) - (i ** 4))
    return sum1

def f32(n, m):
    sum2 = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            sum2 += (j + (j ** 4))
    return sum2

def f3(n, m):
    return (f31(n, m) / 71) - (5 * f32(n, m))


print("{:.2e}".format(f3(42, 55)))
print("{:.2e}".format(f3(46, 77)))


#1.4
print("Задача 1.4")


def f4(n):
    if n == 0:
        return 9
    elif n == 1:
        return 8
    else:
        return tan(f4(n - 2)) - fabs(f4(n - 2))


print("{:.2e}".format(f4(2)))
print("{:.2e}".format(f4(13)))