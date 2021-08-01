#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 18:48:51 2021

@author: gabriel

(lista_nova)=[1, 2, -1, 3, -1, 4, 5, 0, 0, 1, 2, -1, -1, -1, 2, 2, -1, 3, 2, 0, 1, 1, -1, 0, 2]
sum 24
max 5
min -1
np.mean 0.96
st.mode -1
np.std 1.684755175092215 
"""
import numpy as np
import statistics as st
lista=[[1,2,-1],[3,-1,4,5],[0,0,1,2,-1],[-1,-1,2,2,-1],[3,2,0],[1,1,-1,0,2]]
i=1
lista_nova=[]
for x in lista:
    for num in x:
        lista_nova.append(num)

print(lista_nova)
soma=sum(lista_nova)
maximo=max(lista_nova)
minimo=min(lista_nova)
media=np.mean(lista_nova)
moda=st.mode(lista_nova)
desvio_padrao=np.std(lista_nova)
print('+++++++++ Resultados Finais++++++')
print('%6.2f %6.2f %6.2f %6.2f %6.2f %6.2f' % (soma,maximo,minimo,media,moda,desvio_padrao))
      