#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 15:24:40 2021

@author: gabriel
Continue
"""
n=int(input("Qnt de numeros = "))
cont=1
s=0
while cont <=n: # Menor ou Igual à 'N' = quantidades de Loops que vai dar
        s=s+cont
        if s % 2 ==0: continue 
        cont=cont+1
        print(s)