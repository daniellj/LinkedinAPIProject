#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: daniellj
"""
import json
from company import Company

if __name__ == "__main__":
    # Ajustando o seletor de campos de retorno
    selectors = ['entityStatus','vanityName','id','industries','foundedOn','website','specialties','staffCountRange']
    extracted_data = []
    
    # Criando uma lista de empresas
    #company_list = ['Gerdau', 'Agibank', 'Multiplan', 'Petrobras', 'Google']
    company_list = ['devtestco1']
    
    for comp in company_list:
        # chamando a função para efetuar a consulta das empresas er colocando o resultado em uma lista
        extracted_data.append(Company.search_company_by_vanityName(vanityName=comp, selectors=selectors))

    if extracted_data:
        print('')
        print('ERRO: conteúdo retornado vazio -->>', extracted_data)
    else:
        print('')
        print('Resultado da requisição em tela:', extracted_data)
        print('')        
        print('Exportando resultado da requisição para o arquivo data.json...')
        f = open('data.json', 'w')
        json.dump(extracted_data, f, indent=4)
        print('Exportação finalizada com sucesso!')
