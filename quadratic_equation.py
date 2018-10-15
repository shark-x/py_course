from math import sqrt


def quadratic_eq(a,b,c):
    d = b*b-4*a*c
    if d<0:
        print("No solutions")
    elif d==0:
        x = -b/(2*a)
        print("One solution, x = " + str(x))
    elif d>0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        print("Two solutions, x1 = " + str(x1) + ", x2 =" + str(x2))
    else:
        print("Ошибка ввода/Исключение")


quadratic_eq(1,1,1)
quadratic_eq(1,2,1)
quadratic_eq(1,5,6)
quadratic_eq(2,3,4)
