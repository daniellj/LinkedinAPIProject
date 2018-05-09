# -*- coding: utf-8 -*-
"""
Automatizando a autorização e gerando o TOKEN
"""

from linkedin import linkedin

from mechanicalsoup import StatefulBrowser
import configparser as cp

# Read secrets:
cfg_file = 'linkedin_config'
config = cp.ConfigParser()
config.read(cfg_file)
if not config.has_section('Secrets'):
    raise RuntimeError('no secrets specified')
secrets = {}
for s in config.items('Secrets'):
    secrets[s[0]] = s[1]

# Colocando os valores sensíveis em uma lista
secret_values = []
for key, value in secrets.items():
    secret_values.append(value)

# Atribuindo os valores sensíveis para variáveis
API_KEY = secret_values[0]
API_SECRET = secret_values[1]
RETURN_URL = secret_values[2]
USER = secret_values[3]
PASSWD = secret_values[4]
PERMISSIONS = ['r_basicprofile', 'r_emailaddress']

# Gerando a URL para POST no Autenticador...
authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, PERMISSIONS)

# Instanciando objeto de navegador de internet
state = StatefulBrowser (
                         soup_config={'features': 'lxml'}
                        ,raise_on_404=True
                        ,user_agent='info'
                        )

# Abrindo a URL desejada...
login_page = state.open(url=authentication.authorization_url)

# Nível do modo verbose
state.set_verbose(verbose=2)

# Exibindo o conteúdo da página aberta no momento
#print(state.get_current_page())

# Setando valores para o formulário "oauth2SAuthorizeForm"
login_form = login_page.soup.find("form", {"class":"grant-access"})
#print(login_form)

# Setando valores para os campos do formulário
login_form.find("input", {"id": "session_key-oauth2SAuthorizeForm"})["value"] = USER
login_form.find("input", {"id": "session_password-oauth2SAuthorizeForm"})["value"] = PASSWD

# Setando qual botão será acionado no SUBMIT
#form.Form.choose_submit(submit='authorize')

# Submetendo os valores para o formulário
response = state.submit(login_form, login_page.url)
message = str(response.content)
print(message)