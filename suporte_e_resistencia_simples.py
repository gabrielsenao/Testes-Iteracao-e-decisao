#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 18:46:50 2021

@author: gabriel
"""
preco=float(input("Preco Atual da Acao: "))
Baixa_historica=float(input("Baixa Historica: "))
Alta_historica=float(input("Alta Historica: "))
suporte=(Baixa_historica+(Alta_historica-Baixa_historica)*0.3)
resistencia=(Baixa_historica+(Alta_historica-Baixa_historica)*0.6)

print("suporte:",suporte)
print("resistencia:",resistencia)

if (preco>=suporte) and (preco<=resistencia):
    print("Esta dentro do Suporte e Resistencia")
else:
    print("Esta fora da faixa de Suporte e Resistencia")
    