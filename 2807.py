a = 1
b = 1

ls = []

ls.append(a)
ls.append(b)

k = int(input())

if k == 1:
    print(1)
else:
    for i in range(k-2):
        i+=2
        ls.append(ls[i-2]+ls[i-1])

    ls.reverse()
    sarr = [str(a) for a in ls]
    print(' '.join(sarr))
