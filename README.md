## Problema

Este projeto surgiu da necessidade de capturar informações de empresas contidas no Linkedin.

Para desenvolver a atividade, é disponibilizada a REST API do [Organization Lookup API do Linkedin v2](https://developer.linkedin.com/docs/guide/v2/organizations/organization-lookup-api).

Basicamente será fornecida uma lista contendo nomes de empresas e, para cada uma dessas empresas, a solução deverá retornar  apenas os dados dos campos solicitados abaixo:

- Situação **(entityStatus)**
- Nome **(vanityName)**
- Id **(id)**
- Tipo da indústria (internet, alimentos, vestuário, etc) **(industries)**
- Ano da fundação **(foundedOn)**
- Site **(website)**
- Especialidade (recolocação de profissionais, alimentação vegana, roupas esportivas, etc) **(specialties)**
- Quantidade de funcionários **(staffCountRange)**

## Requisitos

1. Criar um [aplicativo](https://www.linkedin.com/secure/developer) na rede social Linkedin;
2. Entender a sistemática de [autenticação OAUTH 2.0 do Linkedin](https://developer.linkedin.com/docs/oauth2) proposta para uso da REST API e configurar o aplicativo criado;

## Resultados

O formato da saída da requisição da consulta deverá ser exibida em tela e/ou a exportação para um arquivo JSON para cada empresa consultada contendo os dados solicitados.

## Lógica da solução desenvolvida

- O Linkedin utiliza OAUTH 2.0. Após a criação da aplicação na rede social, é gerado automaticamente duas informações: **ClienteID** e **ClientSecret**. A combinação de **ClienteID**, **ClientSecret** e a **URL de Redirecionamento** irá gerar um **Código de Autorização**. Esse código é passado para o autenticador da rede social, que finalmente irá gerar o **token**, que nada mais é que a combinação das informações: **ClienteID**, **ClientSecret** e **Código de Autorização**. Através deste token (que tem tempo de expiração, maiores detalhes ver documentação do Linkedin), será possível efetuar requisições para a rede social.

- Utilização da biblioteca [requests-oauthlib](https://github.com/requests/requests-oauthlib) para requisições contra a REST API do Linkedin;

- Criação de uma classe "Company", contendo os atributos necessários para servir de camada de abstração dos objetos retornados pelo Linkedin, assim como métodos utilizados pela classe (geração de arquivo JSON, exibição resultados em tela, etc);

## Requerimentos de ambiente

- S.O.: Linux
- Interpretador Python 3.6 ou versão mais recente.

## Instalação

1. Clonar este projeto via GIT ou download.
2. Instalar as dependências do projeto (Python Libraries): via terminal do Linux, acessar a pasta onde se encontra o arquivo "requirements.txt". Após, digite/execute o comando à seguir: pip install -r requirements.txt

## Geração do Token

Para efetuar requisições ao Linkedin, é necessário gerar o **token de acesso**. Para tanto, siga as instruções:

1. Após efetuar o clone deste repositório, editar o arquivo "**linkedin_config**". Este arquivo de configuração contêm os seguintes campos:

  [Secrets]<br />
  CLIENT_ID=XXXXXX<br />
  CLIENT_SECRET=YYYYYYYYYYY<br />
  REDIRECT_URI=https://localhost:8080<br />
  AUTHORIZATION_URL=https://www.linkedin.com/uas/oauth2/authorization<br />
  ACCESS_TOKEN_URL=https://www.linkedin.com/uas/oauth2/accessToken<br />
  REDIRECT_RESPONSE=<br />

A instrução é colocar valores válidos para os campos **CLIENT_ID**, **CLIENT_SECRET** e **REDIRECT_URI** após o sinal de "=", sem espaçamentos ou aspas envolvidas, salvar e fechar o arquivo. Importante lembrar que antes de tudo, você deve ter uma aplicação registrada no Linkedin, para de fato ter informações para preencher o arquivo de configuração "linkedin_config".

2. No terminal do Linux, executar o script python: **authorization.py**. Após, será fornecida uma mensagem de que você deve copiar a URL gerada, colar no navegador de internet e clicar em ENTER. Feito isso, faça a autorização do APP: forneça suas credenciais no Linkedin, e AUTORIZE o APP. Será redirecionado para a página de REDIRECT configurada no APP.

3. COPIE TODO O CONTEÚDO da URL que foi redirecionda. Algo como: https://localhost:8080/?code=AQT_EcUxnuLX_npEy8L9S13cVxueJt7wY_ngrfnmBaaMa8nXs4Jpe7CPPOD1OGU781GICNibxJ1yiXLVdhqj5XIyDVjUa_XyzD_fhN9L27CqD-zxA5DviASQ6tvLoEc5s4CGb5Pe8eQhD-hsb6E&state=MwPhX3lTngermCjwZ5NXrqeOo8Byb6#!

4. Abra o arquivo "**linkedin_config**" novamente. COLE o conteúdo gerado pela URL redirecionada (ver passo 3!) logo após:

REDIRECT_RESPONSE=

Vai ficar algo como: 

REDIRECT_RESPONSE=https://localhost:8080/?code=AQT_EcUxnuLX_npEy8L9S13cVxueJt7wY_ngrfnmBaaMa8nXs4Jpe7CPPOD1OGU781GICNibxJ1yiXLVdhqj5XIyDVjUa_XyzD_fhN9L27CqD-zxA5DviASQ6tvLoEc5s4CGb5Pe8eQhD-hsb6E&state=MwPhX3lTngermCjwZ5NXrqeOo8Byb6#!

5. Salve e feche o arquivo "**linkedin_config**".

6. Execute o script "**token-generate.py**". Será gerado o token de acesso pelo Linkedin, e escrito o valor do TOKEN dentro do arquivo "**new_token**". Guarde-o, pois o token será usado nas requisições ao Linkedin.

## Execução

Para a etapa de executação, considere que o TOKEN já esteja gerado. A partir disso, siga as etapas para executar o projeto:

1. Abrir o prompt de comando do terminal Linux
2. Fazer a chamada ao script **main.py**, passando por parâmetro o(s) nome(s) da(s) empresa(s) que se deseja efetuar a requisição da consulta, conforme exemplo abaixo:
  - python main.py 'nome_empresa_01' 'nome_empresa_02' 'nome_empresa_N'
  - Exemplo REAL: **python main.py 'devtestco1' 'petrobras'**
3. Será exibido em tela o resultado, assim como será gerado um arquivo .JSON com a extração dos resultados.
  - O nome padrão de cada arquivo se dará no seguinte formato: **nome_empresa_X_20180514-142230.json**, identificando o momento que foi efetuada a consulta e geração do arquivo da respectiva empresa.
