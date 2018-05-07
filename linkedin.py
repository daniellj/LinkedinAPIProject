#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: daniellj
"""
#from PyLinkedinAPI.PyLinkedinAPI import PyLinkedinAPI
from requests_oauthlib import OAuth2Session
import requests

client_id = r'77pm3rcwpgc8xu'
client_secret = r'CQtVXv6bxGxeRpkw'
redirect_uri = 'https://localhost:8080'

AUTH_URL = 'https://www.linkedin.com/uas/oauth2/authorization'
ACCESS_TOKEN_URL = 'https://www.linkedin.com/uas/oauth2/accessToken'

oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)
#authorization_url, state = oauth.authorization_url(AUTH_URL)

#print('Please go to %s and authorize access.' % authorization_url)
authorization_response = input('https://localhost:8080/?code=AQR9j3GW_CKTGBJwgyVYDJRsYal8sNkxz_schk8-z1fYhDt5PcLTQLDrVvM82doijgXEkzWs86laiS4DyO4tY7jneNEigBAEm4XrrwSbOJcz7mrKFF5OkugIrH9FXf5zfCT7C9K_z2YO5qEM9iA&state=WI8EkaLf3CjMOX0aaMwphmOQZtzANw#!')

                               
token = oauth.fetch_token(ACCESS_TOKEN_URL, authorization_response=authorization_response, client_secret=client_secret, client_id=client_id, timeout=15)
print(token)

access_token = token
#linkedin = PyLinkedinAPI(access_token)


def search_company_by_vanityName(companyname):
    #url_companies = 'https://api.linkedin.com/v2/organizations?q=vanityName&vanityName=' + str(companyname) + '?oauth2_access_token=' + str(access_token)
    url_companies = 'https://api.linkedin.com/v2/organizations?q=(entityStatus,vanityName,id,industries,foundedOn,website,specialties,staffCountRange)&vanityName=' + str(companyname) + '?oauth2_access_token=' + str(access_token)
    response = requests.post(url_companies, timeout=20)
    response = response.json()
    print(response)