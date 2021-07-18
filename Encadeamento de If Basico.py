# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Encadeamento de If
"""

ask=str(input("Temer sai?"))
if ask=="s":
    ask2=str(input("Maia assume a presidencia?"))
    if ask2=="s":
        ask3=str(input("Antecipa a eleicao?"))
        if ask3=="s":
            print("comprar Petrobras")
        else: 
            print("comprar Usiminas")
    else:
        ask3=str(input("Antecipa Eleicao?"))
        if ask3=="s":
            print("comprar Gerdau")
        else:
            print("comprar Vale")
else:
    ask2=str(input("Greve de caminhoneiros?"))
    if ask2=="s":
        print("comprar Dolar") 
    else:
        print("comprar Ouro")