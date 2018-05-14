#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: daniellj
"""

import requests
import contextlib
from linkedin_v2.utils import to_utf8, StringIO, raise_for_error

class LinkedInSelector(object):
    @classmethod
    def parse(cls, selector):
        with contextlib.closing(StringIO()) as result:
            if type(selector) == dict:
                for k, v in selector.items():
                    result.write('%s:(%s)' % (to_utf8(k), cls.parse(v)))
            elif type(selector) in (list, tuple):
                result.write(','.join(map(cls.parse, selector)))
            else:
                result.write(to_utf8(selector))
            return result.getvalue()

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

    def make_request(method, url, headers=None, data=None, params=None, timeout=60):
        # abrindo o arquivo de origem
        file_o = open('new_token', 'r+')
        # escrevendo o conteúdo do arquivo em uma variável
        print('Abrindo conexão para coleta do TOKEN...')
        content = file_o.readlines()
        ACCESS_TOKEN_VALUE = content[0] # escrevendo o conteúdo do TOKEN em uma variável: está na primeira linha!
        print('Fechando conexão.', file_o)
        print('')
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
        kw = dict(headers=headers, data=data, params=params, timeout=timeout)
        return(requests.request(method.upper(), url, **kw))
    
    def search_company_by_vanityName(vanityName, selectors=None, headers=None, params=None):
        #Campos para seleção do vanityName: entityStatus,vanityName,id,industries,foundedOn,website,specialties,staffCountRange
        url_vanityName = 'https://www.linkedin.com/company/' + str(vanityName)

        if selectors is not None:
            url_vanityName = '%s:(%s)' % (url_vanityName, LinkedInSelector.parse(selectors))

        response = Company.make_request(method='GET', url=url_vanityName, headers=headers, params=params)
        # Tratamento de erros
        raise_for_error(response)
        
        if response.status_code == 200:
            return(response.json())
        else:
            print('Ocorreram problemas na requisição à URL:', response.url)
            print('')
            print('Status Code:', response.status_code)
        #print(response.content)
