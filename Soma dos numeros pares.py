#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 15:24:40 2021

@author: gabriel
Break e Continue
"""
n=int(input("Qnt de numeros = "))
cont=1
s=0
while cont <=n: # Menor ou Igual à 'N' = quantidades de Loops que vai dar
                  #Posso trocar o N p/ ter o maximo Ex; Multiplos de 5 até "20"
        s=s+cont
        if s % 2 ==0: break    
        cont=cont+1
        print(s)