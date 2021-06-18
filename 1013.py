# 1013 - The Greatest
a = int(input())
b = int(input())
c = int(input())

temp = (a+b+abs(a-b))/2
temp = (temp+c+abs(temp-c))/2

print("%d eh o maior\n" % temp)