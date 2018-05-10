#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: daniellj
"""

from linkedin.utils import raise_for_error
import configparser as cp
import requests


class Company:
    def __init__(self, entityStatus, vanityName, Id, industries, foundedOn, website, specialties, staffCountRange):
        self.entityStatus = entityStatus
        self.vanityName = vanityName
        self.Id = Id
        self.industries = industries
        self.foundedOn = foundedOn
        self.website = website
        self.specialties = specialties
        self.staffCountRange = staffCountRange
        
    def make_request(method, url, data=None, params=None, headers=None, timeout=60):
        # Read TOKEN:
        try:
            # abrindo o arquivo de origem
            file_o = open('new_token', 'r+')
                # escrevendo o conteúdo do arquivo
            content = file_o.readlines()
            ACCESS_TOKEN_VALUE = content[0] # Está na primeira linha!
        finally:
            print('Fechando o arquivo de origem', file_o)
            file_o.closed
    
        # Ajustando cabeçalhos
        if headers is None:
            headers = {'x-li-format': 'json', 'Content-Type': 'application/json'}
        else:
            headers.update({'x-li-format': 'json', 'Content-Type': 'application/json'})
    
        # Ajustando parâmetros
        if params is None:
            params = {}
        
        # Inserindo o token nos parâmetros
        params.update({'oauth2_access_token': ACCESS_TOKEN_VALUE})
        kw = dict(data=data, params=params, headers=headers, timeout=timeout)
        return(requests.request(method.upper(), url, **kw))
    
    def search_company_by_vanityName(vanityName):
        #Campos para projeção do vanityName: entityStatus,vanityName,id,industries,foundedOn,website,specialties,staffCountRange
        url_vanityName = 'https://www.linkedin.com/in/' + str(vanityName) + '?projection=(entityStatus,vanityName,id,industries,foundedOn,website,specialties,staffCountRange~)'
        print(url_vanityName)
    
        response = make_request(method='GET', url=url_vanityName)
        # Tratamento de erros
        raise_for_error(response)
        print(response.json())
