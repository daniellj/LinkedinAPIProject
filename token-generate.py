#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 20:24:54 2018

@author: daniellj
"""

import configparser as cp
from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import linkedin_compliance_fix
from io import open

# Read secrets:
cfg_file = 'linkedin_config'
config = cp.ConfigParser()
config.read(cfg_file)
if not config.has_section('Secrets'):
    raise RuntimeError('no secrets specified')
secrets = {}
for s in config.items('Secrets'):
    secrets[s[0]] = s[1]

CLIENT_ID = secrets.get('client_id')
CLIENT_SECRET = secrets.get('client_secret')
REDIRECT_URI = secrets.get('redirect_uri')
ACCESS_TOKEN_URL = secrets.get('access_token_url')
REDIRECT_RESPONSE = secrets.get('redirect_response')

oauth = OAuth2Session(client_id=CLIENT_ID, redirect_uri=REDIRECT_URI)

# Get the authorization verifier code from the callback url
#redirect_response = input('Paste the full redirect URL here:')

redirect_response = REDIRECT_RESPONSE

# Fetch the access token
linkedin = linkedin_compliance_fix(oauth)
linkedin.fetch_token(ACCESS_TOKEN_URL, client_secret=CLIENT_SECRET, authorization_response=redirect_response)

#print(linkedin.token)
token_value = linkedin.token
ACCESS_TOKEN_VALUE = token_value.get('access_token')

print('Valor do ACCESS TOKEN fornecido:')
print(ACCESS_TOKEN_VALUE)

try:
    # abrindo o arquivo de origem
    file_o = open('new_token', 'w+')
    # escrevendo o conteúdo do arquivo
    file_o.write(ACCESS_TOKEN_VALUE)
finally:
    print('Fechando o arquivo de origem', file_o)
    file_o.closed

'''
access_token = 'AQXygyThmXuWMfAw6ZqN6QYTp3erKx_WoR0puXyp7sfwpuZOhUy1amOSNptdayD6GEOlAFix6pLx-49o-bX0ct11kokBSRGtbsZwp998sjVgOaD-z7G6bMSeMOfqhd0wXmLgJFBIyZhmXDbjMDvE6gag1zxX5eKLamJKm3Ps7T5-FAchD6_0LIdUG0lSLN6sITLsK3q5K8oXts3OmjMR-VVNhHKQe-vxLTeKd-rg52midl_RdT_z-qwjlE7GD-OmXHMbFo9fykJv4R_qnNTIEpgtpuegIXqsMYIaaQVVdWsxOj4amc0CMfp8899g2XVIU_lJI7ssvFWO4_CrHTqo82wzGAbaZw'
{'token_type': 'Bearer', 'expires_in': 5183999, 'expires_at': 1530920358.1948643, 'access_token': 'AQXygyThmXuWMfAw6ZqN6QYTp3erKx_WoR0puXyp7sfwpuZOhUy1amOSNptdayD6GEOlAFix6pLx-49o-bX0ct11kokBSRGtbsZwp998sjVgOaD-z7G6bMSeMOfqhd0wXmLgJFBIyZhmXDbjMDvE6gag1zxX5eKLamJKm3Ps7T5-FAchD6_0LIdUG0lSLN6sITLsK3q5K8oXts3OmjMR-VVNhHKQe-vxLTeKd-rg52midl_RdT_z-qwjlE7GD-OmXHMbFo9fykJv4R_qnNTIEpgtpuegIXqsMYIaaQVVdWsxOj4amc0CMfp8899g2XVIU_lJI7ssvFWO4_CrHTqo82wzGAbaZw'}
'''