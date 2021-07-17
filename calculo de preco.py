# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Calculo Faixa de Preço
"""
p1=float(input("preco 1 = "))

if p1<=18:
    print("barato")
elif (p1>18) and  (p1<=25):
    print("adequado")
elif (p1>25) and (p1<=32):
    print("caro")
else:
    print("extremamente caro")