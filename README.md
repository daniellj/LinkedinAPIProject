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

O formato da saída da requisição da consulta deverá ser exibida em tela e/ou um único arquivo JSON contendo os dados requisitados de todas as empresas fornecidas na lista de entrada.

# Lógica da solução desenvolvida

- O Linkedin utiliza OAUTH 2.0. Após a criação da aplicação na rede social, é gerado automaticamente duas informações: **ClienteID** e **ClientSecret**. A combinação de **ClienteID**, **ClientSecret** e a **URL de Redirecionamento** irá gerar um **Código de Autorização**. Esse código é passado para o autenticador da rede social, que finalmente irá gerar o **token**, que nada mais é que a combinação das informações: **ClienteID**, **ClientSecret** e **Código de Autorização**. Através deste token (que tem tempo de expiração, maiores detalhes ver documentação do Linkedin), será possível efetuar requisições para a rede social.

- Utilização da biblioteca [requests-oauthlib](https://github.com/requests/requests-oauthlib) para requisições contra a REST API do Linkedin;

- Criação de uma classe CompanyLinkedin, contendo os atributos necessários para servir de camada de abstração dos objetos retornados pelo Linkedin, assim como métodos utilizados pela classe (geração de arquivo JSON, exibição resultados em tela, etc);

## Requerimentos de ambiente

- S.O.: Linux
- Interpretador Python 3.6 ou versão mais recente.

## Instalação

Em desenvolvimento.

## Execução

Em desenvolvimento.
