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
obs: float x int
"""
x=float(input("X do triangulo: "))
y=float(input("Y do triangulo: "))
z=float(input("Z do triangulo: "))

if (x!=y) and (x!=z) and (y!=z):
    print("escaleno")
elif (x==y) and (x==z) and (y==z):
    print("equilatero")
else:
    print("isoceles")
    