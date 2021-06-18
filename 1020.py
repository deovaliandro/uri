# 1020 - Age in Days
day, month, year = 0, 0, 0
myday = int(input())

year = myday/365
myday = myday % 365
month = myday/30
myday = myday % 30

day = myday

if month >= 12:
    aa = month/12
    year+=aa
    month %= 12

print("%d ano(s)\n%d mes(es)\n%d dia(s)\n" % (year, month, day))