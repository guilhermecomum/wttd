# Eventex
Sistema de eventos

[![Build Status](https://travis-ci.org/guilhermecomum/wttd.svg?branch=master)](https://travis-ci.org/guilhermecomum/wttd)
[![Maintainability](https://api.codeclimate.com/v1/badges/7a2342b397b4cc71dedd/maintainability)](https://codeclimate.com/github/guilhermecomum/wttd/maintainability)

## Desenvolvendo

1. Clone o respositório.
2. Crie um virtualenv com `Python 3.7`
3. Ative o virtualenv
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes

```console
git clone git@github.com:guilhermecomum/wttd.git
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Deploy

1. Crie uma instância no Heroku
2. Envie as configurações para o Heroku
3. Defina uma `SECRET_KEY` segura para instância
4. Defina `DEBUG=False`
5. Configure o serviço de email.
6. Envie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:Set DEBUG=False
# configura o email
git push heroku master -f
```
