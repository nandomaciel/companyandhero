# Company and Hero

## API
[companyandhero](https://companyandhero.heroku.com/)

## Problema
Eu como Dev Frontend na Company Hero, gostaria criar empresas com um formulário simples. Preciso saber quais dados enviar em JSON e para qual URL. A ideia é criar um diretório de empresas e seus funcionários, estes funcionários seriam os usuários da plataforma porem precisamos considerar que um usuário pode pertencer a mais de uma empresa.

## Deploy

**Via CLI**

- Crie o ambiente para instalação das dependências
``` shell
python -m venv env
```
- Ative o ambiente 
``` shell
source env/bin/activate
```
- Instale os pacotes necessarios para executar o projeto
``` shell
pip install -r requirements.txt
```
- Execute a criação das tabelas do banco de dados
``` shell
python manage.py makemigrations
python manage.py migrate
```
- Criando um super usuário para acessar o Django Admin _(opcional)_
``` shell
python manage.py createsuperuser
```
- Execute o projeto
``` shell
python manage.py runserver
```
Se todos os passos ocorreram sem apresentar nenhum erro. O projeto vai estar executando no endereço:

[127.0.0.1:8000](http://127.0.0.1:8000)

**Docker**

_Em breve!_

## Endpoints

_Em breve!_
