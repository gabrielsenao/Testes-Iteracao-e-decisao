#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 15:24:40 2021

@author: gabriel
Gerar Multiplos de 5 ate 20
"""
n=int(input("Qnt de numeros = "))
cont=0
s=0
while cont <=n: # Menor ou Igual à 'N' = quantidades de Loops que vai dar
    if cont % 2 ==0:            #Posso trocar o N p/ ter o maximo Ex; Multiplos de 5 até "20"
        s=s+cont
        print(s)
    cont=cont+1
