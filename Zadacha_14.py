# Требуется вывести все целые степени двойки (т.е. числа
# вида 2 в степени k), не превосходящие числа N.


N = int(input('Введите максимальное число: '))
list = []
k = 0
while 2**k <= N:
    list.append(2**k)
    k += 1

print(*list)