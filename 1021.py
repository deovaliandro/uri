# 1021 - Banknotes and Coins
a, b, c, d, e, f, g, h, i, j, k, l = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
n = float(input())

if n >= 100:
    a = n / 100
    n = n % 100

if n >= 50 and n < 100:
    b = n / 50
    n = n % 50

if n >= 20 and n < 50:
    c = n / 20
    n = n % 20

if n >= 10 and n < 20:
    d = n / 10
    n = n % 10

if n >= 5 and n < 10:
    e = n / 5
    n = n % 5

if n >= 2 and n < 5:
    f = n / 2
    n = n % 2

if n >= 1 and n < 2:
    g = n / 1
    n = n % 1

if n >= 0.50 and n < 1:
    h = n / 0.50
    n = n % 0.50

if n >= 0.25 and n < 0.50:
    i = n / 0.25
    n = n % 0.25

if n >= 0.10 and n < 0.25:
    j = n / 0.10
    n = n % 0.10

if n >= 0.05 and n < 0.10:
    i = n / 0.05
    n = n % 0.05

if n >= 0.01 and n < 0.05:
    l = n / 0.01
    n = n % 0.01

print("NOTAS:\n")
print("%d nota(s) de R$ 100.00" % a)
print("%d nota(s) de R$ 50.00" % b)
print("%d nota(s) de R$ 20.00" % c)
print("%d nota(s) de R$ 10.00" % d)
print("%d nota(s) de R$ 5.00" % e)
print("%d nota(s) de R$ 2.00" % f)

print("MOEDAS:\n")
print("%d nota(s) de R$ 1.00" % g)
print("%d nota(s) de R$ 0.50" % h)
print("%d nota(s) de R$ 0.25" % i)
print("%d nota(s) de R$ 0.10" % j)
print("%d nota(s) de R$ 0.05" % k)
print("%d nota(s) de R$ 0.01\n" % l)