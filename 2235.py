x, y, z = [int(x) for x in input().split(" ")]

if x == y or y == z or x == z or x+y == z or x+z == y or y+z == x:
    print("S")
else:
    print("N")