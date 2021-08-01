#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 23:57:37 2021

@author: gabriel
"""

lista=[['ontem','hoje','amanha'],['sp','rj','mg','ce'],['sao paulo','rio','santos','cuiaba']]
nova_lista=[]
for x in lista:
    for y in x:
        nova_lista.append(y)
print('++++++ Nova Lista ++++++')
print(nova_lista)
print('++++++ Lista Extendida ++++++')
nova_lista.extend(['ferias','negocios'])
print(nova_lista)
print('++++++ Ordem Alfabetica ++++++')
print(sorted(nova_lista))
