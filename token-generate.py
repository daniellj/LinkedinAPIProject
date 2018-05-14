#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
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

print('Valor do ACCESS TOKEN fornecido:','\n')
print(ACCESS_TOKEN_VALUE)
print('\n')
print(token_value.items())
print('\n')

# escrevendo o conteúdo do TOKEN no arquivo
with open('new_token', 'w') as file_o:
    file_o.write(ACCESS_TOKEN_VALUE)
    print('Fechando o arquivo de origem', file_o)
    file_o.closed
