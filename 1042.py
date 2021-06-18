# 1042 - Simple Sort
a = int(input())
b = int(input())
c = int(input())

temp2, temp3 = 0, 0

temp1 = ((a+b) - abs(a-b))/2
temp2 = ((a+b) + abs(a-b))/2
dummy1 = temp1
temp1 = ((temp1+c) - abs(temp1-c))/2
temp3 = ((dummy1+c) + abs(dummy1-c))/2
dummy2 = temp2
temp2 = ((temp3+temp2) - abs(temp3-temp2))/2
temp3 = ((temp3+dummy2) + abs(temp3-dummy2))/2

print("%d\n%d\n%d\n" % (temp1, temp2, temp3))