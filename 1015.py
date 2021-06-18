# 1015 - Distance Between Two Points
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

distance = sqrt(pow((x2-x1),2)+pow((y2-y1), 2))
print("%0.4f\n" % distance)