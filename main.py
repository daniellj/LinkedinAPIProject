#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: daniellj
"""
import json
from company import Company
import sys
import time

def main(company_name):
    # Ajustando o seletor de campos de retorno
    selectors = ['entityStatus','vanityName','id','industries','foundedOn','website','specialties','staffCountRange']
    extracted_data = []

    for comp in company_list:
        # chamando a função para efetuar a consulta das empresas er colocando o resultado em uma lista
        extracted_data.append(Company.search_company_by_vanityName(vanityName=comp, selectors=selectors))

        if extracted_data:
            print('')
            print('ERRO: conteúdo retornado vazio -->>', extracted_data)
        else:
            print('')
            print('Resultado da requisição em tela da empresa', comp, extracted_data)
            print('')        
            # Coletando o "datetime" do momento da geração do arquivo para montar o nome do arquivo distinto por coleta
            filename = comp + '_' + time.strftime("%Y%m%d-%H%M%S") + '.json'
            print('Exportando resultado da requisição para o seguinte arquivo JSON:', filename)
            f = open(filename, 'w')
            json.dump(extracted_data, f, indent=4)
            print('Exportação finalizada com sucesso!')

if __name__ == "__main__":
    # A chamado à função principal deve ser feita pelo comando: python main.py 'nome_empresa_01' 'nome_empresa_02' 'nome_empresa_N'
                                                 #Exemplo REAL: python main.py 'devtestco1' 'petrobras'
    company_list = sys.argv[1:]
    main(company_list)
