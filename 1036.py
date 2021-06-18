# 1036 - Bhaskara's Formula
import math

a = float(input())
b = float(input())
c = float(input())

if a > 0.0 or b > 0.0 or c > 0.0 :
    aa = ((b*(-1)) + (math.sqrt(pow(b,2)-(4*a*c))))/(2*a)
    ab = ((b*(-1)) - (math.sqrt(pow(b,2)-(4*a*c))))/(2*a)

    print("R1 = %0.5f\n" % aa)
    print("R2 = %0.5f\n" % ab)
else :
    print("Impossivel calcular")