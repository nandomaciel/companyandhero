# Company and Hero

## API
[companyandhero](https://companyandhero.heroku.com/)

## Problema
Eu como Dev Frontend na Company Hero, gostaria criar empresas com um formulário simples. Preciso saber quais dados enviar em JSON e para qual URL. A ideia é criar um diretório de empresas e seus funcionários, estes funcionários seriam os usuários da plataforma porem precisamos considerar que um usuário pode pertencer a mais de uma empresa.

## O que falta
- Exibir funcionários na listagem das empresas
- A busca por um funcionário utiliza o *filters* do Django Rest o que retornar usernames similares.

## Testes
- Foi feito um simples teste de criação de funcionario e de empresa

## Deploy

Dependendo de como for utilizar é necessario modificar as configurações para o banco de dados.

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

---
## Endpoints

| Endpoint | Método | Ação |
|--|--|--|
| /api/v1/empresa/ | GET | Listar todas as empresas cadastradas |
| /api/v1/empresa/ | GET | Cadastrar uma empresa |
| /api/v1/empresa/:id| GET | Informação de uma empresa |
| /api/v1/empresa/:id| PUT | Editar informações de uma empresa |
| /api/v1/empresa/:id| DELETE | Detelar informações uma empresa |
||||
| /api/v1/funcionario/ | GET | Listar todos os funcionários cadastrados |
| /api/v1/funcionario/ | GET | Cadastrar um funcionário |
| /api/v1/funcionario/:id| GET | Informação de um funcionário |
| /api/v1/funcionario/:id| PUT | Editar informações de um funcionário |
| /api/v1/funcionario/:id| DELETE | Deletar um funcionário |

- **Buscar funcionário pelo username**

Para realizar a buscar por um usuário deve ser inserido o paramento _search_ e o valor (_username_) a ser pesquisado no enpoint api/v1/funcionario/

---

## Modelo de JSON

**Cadastrar empresa**
``` json
{
"nome": "nome da empresa",
"cnpj": "cnpj da empresa"
}
```

**Cadastrar funcionário**

``` json
{
"nome": "Nome do Funcionário",
"username": "funcionariousername",
    "empresas": [
        {
            "nome": "nome da empresa já cadastrada"
        }
    ]
}
```
## Exemplo de Modelo JSON


**Cadastrar empresa**

**endpoint:** /api/v1/empresa/

``` json
{
"nome": "Google",
"cnpj": "12345"
}
```
``` json
{
"nome": "Company Hero",
"cnpj": "54321"
}
```

**Cadastrar funcionário**

**endpoint:** /api/v1/funcionario/

_Cadastrando em uma única empresa_
``` json
{
"nome": "Mark Down",
"username": "md",
    "empresas": [
        {
            "nome": "Google"
        }
    ]
}
```

_Cadastrando em mais de uma empresa_

``` json
{
"nome": "Java Script",
"username": "js",
    "empresas": [
        {
            "nome": "Google"
        },
        {
            "nome": "Company Hero"
        }
    ]
}
```