#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: daniellj
"""

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
        
    def search_company_by_vanityName(companyname):
        #url_companies = 'https://api.linkedin.com/v2/organizations?q=vanityName&vanityName=' + str(companyname) + '?oauth2_access_token=' + str(access_token)
        url_companies = 'https://api.linkedin.com/v2/organizations?q=(entityStatus,vanityName,id,industries,foundedOn,website,specialties,staffCountRange)&vanityName=' + str(companyname) + '?oauth2_access_token=' + str(access_token)
        response = requests.post(url_companies, timeout=20)
        response = response.json()
        print(response)