# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = int(input())

for i in range (n):
    arr = [int(i) for i in input().split()]
    arr.pop(0)

    print(sum(arr)-len(arr)+1)