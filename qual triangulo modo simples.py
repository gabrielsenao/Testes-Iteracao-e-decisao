#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 12:28:08 2021

@author: gabriel
Exercicio 
Dados tres lados de um triangulo qualquer, fazer um programa para descobrir
se o triangulo e equilatero, isoceles ou escaleno. Entrar com os valores com
input

isoceles = 2 lados iguais
equilateros = 3 lados iguais

"""
x=int(input("X do triangulo: "))
y=int(input("Y do triangulo: "))
z=int(input("Z do triangulo: "))

if x==y:
    if x==z:
        print("equilatero")
    else:
        print("isosceles")
elif x==z:
    print("iscoceles")
elif y==z:
    print("iscoceles")
else:
    print("escaleno")
        