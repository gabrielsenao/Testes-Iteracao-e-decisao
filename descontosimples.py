#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 12:54:23 2021

@author: gabriel
Desconto simples
"""
compra=float(input("Quanto deu a compra? "))
if compra <= 20:
    print("Desconto de 5%, novo valor: ",compra-compra*0.05)
elif compra>=21 and compra<=50:
    print("Desconto de 10%, novo valor: ",compra-compra*0.10)
elif compra>=51 and compra<=100:
    print("Desconto de 15%, novo valor: ",compra-compra*0.15)    
elif compra>=101 and compra<=1000:
    print("Desconto de 20%, novo valor: ",compra-compra*0.20)
else:
    print("Desconto de 30%, novo valor: ",compra-compra*0.30)
    