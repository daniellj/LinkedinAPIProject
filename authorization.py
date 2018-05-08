#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: daniellj
"""
import configparser as cp
from requests_oauthlib import OAuth2Session

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
REDIRECT_URI = secrets.get('redirect_uri')
AUTHORIZATION_URL = secrets.get('authorization_url')
PERMISSIONS = ['r_basicprofile', 'r_emailaddress']

oauth = OAuth2Session(client_id=CLIENT_ID, redirect_uri=REDIRECT_URI)
authorization_url, state = oauth.authorization_url(url = AUTHORIZATION_URL, permissions = PERMISSIONS)
print('')
print('Please go here and authorize to generate the code:\n')
print(authorization_url)