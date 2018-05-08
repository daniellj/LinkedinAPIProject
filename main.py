#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 01:16:07 2018

@author: daniellj
"""

from linkedin import search_company_by_vanityName
from company import Company

company_list = ['Gerdau', 'Agibank', 'Multiplan', 'Petrobras', 'Google']
#r = oauth.get('https://api.linkedin.com/v2/organizations?q=vanityName&vanityName=devtestco1')

for comp in company_list:
    search_company_by_vanityName(comp)
    
# mapear os valores de saída da função para os atributos da classe "Company".

# imprimir os valores dos atributos da classe
    