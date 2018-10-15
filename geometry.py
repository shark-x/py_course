from geom2d import *

# Равенство объектов и списков
print("\nРавенство объектов и списков")
l1 = [Point(0, 0), Point(1, 2), Point(4, 0)]
l2 = [Point(0, 0), Point(1, 2), Point(4, 0)]
l3 = l1
l4 = list(l1)
l4[0] = Point(0, 0)
print("l1 = " + str(l1))
print("l2 =" + str(l2))
print("l1 равно l2? " + str(l1 == l2))
print("l3 =" + str(l3))
print("l1 равно l3? " + str(l1 == l3))
print("l4 =" + str(l4))
print("l1 равно l4? " + str(l1 == l4))

# Сортировка списков и лямбда - выражения
print("\nСортировка списков и лямбда - выражения")


def x(p):
    return p.x


def y(p):
    return p.y


l5 = [Point(0, 0), Point(4, 3), Point(3, 5)]
l6 = sorted(l5, key=x)
l7 = sorted(l5, key=y)
l8 = sorted(l5, key=lambda p: p.x)
l9 = sorted(l5, key=lambda p: p.distance(Point(0, 0)))
print("Обычный список l5= " + str(l5))
print("Сортированный по х l5, l6 = " + str(l6))
print("Сортированный по y l5, l7 = " + str(l7))
print("Сортированыый по х l5, с помощью ламбда-выражения, l8 = " + str(l8))
print("Сортированный по началу координат l5, с помощью ламбда-выраженияб, l9 = " + str(l9))

# Циклы
print("\nЦиклы")
l10 = []
l11 = []

for i in range(-5, 6):
    l10.append(Point(i, i*i))

i = 1
for element in l10:
    print(str(i) + " точка = " + str(element))
    i += 1

for element in l10:
    l11.append(Point(element.x, -element.y))

print("l10 = " + str(l10))
print("l11 = " + str(l11))

# List Comprehention - Генератор списков
print("\nList Comprehention - Генератор списков")
l12 = [Point(i, i*i) for i in range(-5, 6)]
l13 = [Point(element.x, -element.y) for element in l12]
print("l12 = " + str(l12))
print("l13 = " + str(l13))

# Элементы функционального программирования: map и filter
print("\nЭлементы функционального программирования: map и filter")
l14 = list(map(lambda j: Point(j, j*j), range(-5, 6)))
l15 = list(map(lambda p: Point(p.x, -p.y), l14))
l16 = list(filter(lambda p: p.x > 0, l14))
l17 = list(filter(lambda p: p.x%2 == 0, l14))
print("map:")
print("l14 = " + str(l14))
print("l15 = " + str(l15))
print("filter:")
print("фильтрациия элементов списка l14, если координата x > 0, l16 = " + str(l16))
print("фильтрациия элементов списка l14, если координата x имеет четное значение, l17 = " + str(l17))




