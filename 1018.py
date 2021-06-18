# 1018 - Banknotes
a, b, c, d, e, f, g = 0, 0, 0, 0, 0, 0, 0
n = int(input())

if n >= 100:
    a = n / 100
    n = n % 100

if n >= 50 & n < 100:
    b = n / 50
    n = n % 50

if n >= 20 & n < 50:
    c = n / 20
    n = n % 20

if n >= 10 & n < 20:
    d = n / 10
    n = n % 10

if n >= 5 & n < 10:
    e = n / 5
    n = n % 5

if n >= 2 & n < 5:
    f = n / 2
    n = n % 2

if n >= 1 & n < 2:
    g = n / 1
    n = n % 1

print("%d nota(s) de R$ 100,00" % a)
print("%d nota(s) de R$ 50,00" % b)
print("%d nota(s) de R$ 20,00" % c)
print("%d nota(s) de R$ 10,00" % d)
print("%d nota(s) de R$ 5,00" % e)
print("%d nota(s) de R$ 2,00" % f)
print("%d nota(s) de R$ 1,00\n" % g)