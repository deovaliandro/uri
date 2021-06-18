# 1019 - Time Conversion
hour, minute, second = 0, 0, 0
se = int(input())

if se >= 3600:
    hour = se / 3600
    se = se % 3600

if se >= 60:
    minute = se / 60
    se = se % 60

second = se

print("%d:%d:%d\n" % (hour, minute, second))