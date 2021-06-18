kl = input()

fp,sc = kl.split(" ")
x1,y1 = ord(fp[0]), int(fp[1])
x2, y2 = ord(sc[0]), int(sc[1])

v = [-2, -1, 1, 2]

k1 = x2 - x1
k2 = y2 - y1

if k1 in v and k2 in v:
    print("VALINDO")
else:
    print("INVALINDO")

# if x1 - x2 == 2 and y2 - y1 == 1:
#     print("VALIDO")
# elif x1 - x2 == 1 and y2 - y1 == 2:
#     print("VALIDO")
# elif x2 - x1 == 1 and y2 - y1 == 2:
#     print("VALIDO")
# elif x2 - x1 == 2 and y2 - y1 == 1:
#     print("VALIDO")
# elif x1 - x2 == 2 and y1 - y2 == 1:
#     print("VALIDO")
# elif x1 - x2 == 1 and y1 - y2 == 2:
#     print("VALIDO")
# elif x2 - x1 == 1 and y1 - y2 == 2:
#     print("VALIDO")
# elif x2 - x1 == 2 and y1 - y2 == 1:
#     print("VALIDO")
# else:
#     print("INVALIDO")
