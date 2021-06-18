# 1012 - Area
pi = 3.14159
a = float(input())
b = float(input())
c = float(input())

i = (a*c)/2
j = pi*pow(c, 2)
k = ((a+b)/2)*c
l = b*b
m = a*b

print("TRIANGULO: %0.3f\n" % i)
print("CIRCULO: %0.3f\n" % j)
print("TRAPEZIO: %0.3f\n" % k)
print("QUADRADO: %0.3f\n" % l)
print("RETANGULO: %0.3f\n" % m)