#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 00:20:08 2021

@author: gabriel
"""
let=['a','b','c','a','d','f','a','b','b','d','c']
let_nov=[]
for i in let:
    if i not in let_nov: #Not in faz o inverso do in, ele cria uma nova lista colocando
        let_nov.append(i) # 1 variavel sem repeti-la

print('++++++ Nova Lista ++++++')
print(let_nov)