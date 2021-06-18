# 1037 - Interval
inter = float(input())

if inter <= 25.0 and inter >= 0:
    print("Intervalo [0,25]\n")
elif inter <= 50.0 and inter > 25:
    print("Intervalo (25,50]\n")
elif inter <= 75.0 and inter > 50:
    print("Intervalo (75,100]\n")
elif inter <= 100.0 and inter > 75:
    print("Intervalo (75,100]\n")
else:
    print("Fora de intervalo\n")