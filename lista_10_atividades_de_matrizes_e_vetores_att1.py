# -*- coding: utf-8 -*-
"""Lista 10 atividades de matrizes e vetores.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r-yPqYUGIFLOkNF6qKO9BgoLTDrf7wf3
"""

import random
nota = []
notas = []
saida = []
for i in range(10):
  linha = [0] * 20
  notas.append(linha)
  print (linha)
  saida.append(random.choice(range(100)))
  print (saida)
  print (i)

#for i in range(5):
  #for j in range(3):
#nota[i][j] = int((random.choice(range(100))))