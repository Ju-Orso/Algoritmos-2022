# -*- coding: utf-8 -*-
"""Lista de ativides 9 Marcelo C.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zSjwy_F9D_iWiCNO-iRbhQJuzp6Z3pHr
"""

import math
numeros = [1,2,3,4,5,6,7,8,9]
def isPrime(numeros):
  print (isPrime);

numeros = [5,8,9,48,248,658,6,98,74]

for numero in numeros:
  print (numero)

import math
def isPrime(n):
    start = 2;

    while start <= math.sqrt(n):
        if n % start < 1:
            return False;
        start += 1;

    return n > 1;


print(isPrime(13));