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
CLIENT_ID = secret_values[0]
CLIENT_SECRET = secret_values[1]
REDIRECT_URI = secret_values[2]
AUTHORIZATION_URL = secret_values[3]
ACCESS_TOKEN_URL = secret_values[4]
USER = secret_values[5]
PASSWD = secret_values[6]
PERMISSIONS = ['r_basicprofile', 'r_emailaddress']

# Gerando a URL para POST no Autenticador...
authentication = linkedin.LinkedInAuthentication(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, PERMISSIONS)

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

# Ajustando cabeçalhos
#headers = {'x-li-format': 'json', 'Content-Type': 'application/json'}

csrf = login_form.find("input", {"id":"csrfToken-oauth2SAuthorizeForm"})["value"]

headers =   {
             'x-li-format':'json'
            ,'Content-Type':'application/json'
            ,'Csrf-Token':csrf
            ,'X-RestLi-Protocol-Version':'2.0.0'
            }

login_information = {'csrfToken':csrf}

# Ajustando parâmetros do requests.Session.request
kw = dict(headers=headers, params=login_information, timeout=60)

# Submetendo os valores para o formulário
response = state.submit(form=login_form, url=login_page.url, **kw)
message = str(response.content)
print(message)
