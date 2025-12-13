#1А

#Задачи на арифметические операции

"""a = int(input())
b = int(input())
print(b // a)""" #1А Груши

"""a = int(input())
b = int(input())
print(b % a)""" #1А Тоже груши

"""a = int(input())
print(a % 10)""" #1А Последняя цифра

"""a = int(input())
print(a // 10)""" #1А Количество десятков двузначного числа

"""a = int(input())
print ( a // 10 % 10)""" #1А Количество десятков

"""a = int(input())
print(a // 100 + a // 10 % 10 + a % 10 % 10)""" #1А Сумма цифр

"""m = int(input())
m = m % (24 * 60)
print(m // 60, m % 60)""" #1А Электронные часы

"""a = int(input())
b = int(input())
k = int(input())
total_a = a * k
total_b = b * k
print(total_a + total_b // 100, total_b % 100)""" #1А Стоимость булочек

"""h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
tot_sec1 = h1 * 3600 + m1 * 60 + s1
tot_sec2 = h2 * 3600 + m2 * 60 + s2
delta = tot_sec2 - tot_sec1
print(delta)""" #1А Разность времён

"""import math
a = int(input())
b = int(input())
print(math.sqrt (a**2 + b**2))""" #1А Длина гипотенузы

"""a = int(input())
print("The next number for the number ", a, " is ", a + 1, ".", sep="")
print(f"The next number for the number {a} is {a + 1}.")
print(f"The previous number for the number {a} is {a - 1}.")""" #1А После и перед (sep и f-строку)

#Задачи на условный оператор

"""a = int(input())
b = int(input())
if a >= b:
    print(a)
else:
    print(b)""" #1А Максимум из двух

"""a = int(input())
b = int(input())
if a > b:
    print("1")
elif a < b:
    print("2")
else:
    print("0")""" #1А Какое больше?

"""a = int(input())
if a > 0:
    print("1")
elif a < 0:
    print("-1")
else: 
    print("0")""" #1А Сравни с нулём

"""a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c: 
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)""" #1А Максимум из трёх

"""a = int(input())
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print("YES")
else:
    print("NO")""" #1А Високосный год

#Задачи на условный оператор

"""a = int(input())
b = int(input())
for i in range (a, b + 1):
    if i % 2 == 0:
        print(i)""" #1А Чётные числа

"""n = int(input())
a = 1
for i in range (1, n + 1):
    a *= i
print(a)""" #1А Факториал

"""n = int(input())
a = 0
if n == 0:
    print("0")
else:
    n = abs(n)
    while n != 0:
        a += n**2
        n -= 1
    print(a)""" #1А Сумма квадратов

"""n = int(input())
st = ""
for i in range (1, n + 1):
    if n % i == 0:
        st += str(i) + " "
print(st)""" #1А Все делители

"""n = int(input())
k = 0
for i in range (n):
    a = int(input())
    if a == 0:
        k = 1
if k == 1:
    print("YES")
else:
    print("NO")""" #1А Есть ли нули?

"""n = int(input())
a = 1
while a**2 <= n:
    print(a**2)
    a += 1 """ #1А Меньшие квадраты

"""n = int(input())
for i in range(2, n + 1):
    if n % i == 0:
        print(i)
        break""" #1А Наименьший делитель

"""k = 0
while 0 == 0:
    a = int(input())
    if a == 0:
        break
    k += 1
print(k)""" #1А Длина последовательности

"""k = 0
while 0 == 0:
    a = int(input())
    if a == 0:
        break
    k += a
print(k)""" #1А Сумма последовательности

"""k = 0
while 0 == 0:
    a = int(input())
    if a == 0:
        break
    if a % 2 == 0:
        k += 1
print(k)""" #1А Чётные числа последовательности

#1Б

#Задачи на массивы

"""n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if i % 2 == 0:
        print(a[i], end=" ")""" #1Б Четные индексы

"""n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] % 2 == 0:
        print(a[i], end=" ")""" #1Б Четные элементы

"""n = int(input())
a = list(map(int, input().split()))
k = 0
for i in range(1, n):
    if a[i] > a[i - 1]:
        k += 1
print(k)""" #1Б Больше предыдущего

"""n = int(input())
a = list(map(int, input().split()))
for i in range(n // 2):
    buf = a[i]
    a[i] = a[-i - 1]
    a[-i - 1] = buf
print(*a)""" #1Б Обратный порядок

"""n = int(input())
a = list(map(int, input().split()))
last = a[-1]
for i in range(n - 1, 0, -1):
    a[i] = a[i -1]
a[0] = last 
print(*a)""" #1Б Циклически вправо

"""n = int(input())
a = list(map(int, input().split()))
max = a[0]
for i in range(1, n):
    if a[i] > max:
        max = a[i]
print(max)""" #1Б Максимум в массиве

"""n = int(input())
a = []
k = 0 
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if a[i][j] != a[j][i]:
            k = 1
            break
    if k == 1:
        break
if k == 0:
    print("YES")
else:
    print("NO")""" #1Б Симметрия матрицы

"""n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
i_max = 0
j_max = 0
max = a[0][0]
for i in range(n):
    for j in range(m):
        if a[i][j] > max:
            max = a[i][j]
            i_max = i
            j_max = j
print(max)
print(i_max, j_max)""" #1Б Максимум в матрице

"""n, m = map(int, input().split())
a = [[1] * m for i in range(n)]
for i in range(1, n):
    for j in range(1, m):
        a[i][j] = a[i-1][j] + a[i][j-1]
for i in range(len(a)): 
    print(*a[i])""" #1Б Треугольник Паскаля

#Задачи на символы и строки

"""ch = input()
if ch >= "0" and ch <= "9":
    print("yes")
else:
    print("no")""" #1Б Цифра?

'''ch = input()
if ch >= 'a' and ch <= 'z':
    ch = chr(ord(ch) - 32)
    print(ch)
else:
    print(ch)''' #1Б Верхний регистр

'''ch1 = input()
ch2 = input()
if ch1 == ch2:
    print('yes')
else:
    print('no')''' #1Б Совпадение строк

'''ch = input()
k = 1
for i in range(len(ch)):
    if ch[i] == " ":
        k += 1
print(k)''' #1Б Количество слов

'''ch = input()
k = 'yes'
for i in range(len(ch) // 2):
    if ch[i] != ch[i - 1]:
        k = 'no'
    break
print(k)''' #1Б Палиндром без пробелов

#Задачи на вещественные числа
        