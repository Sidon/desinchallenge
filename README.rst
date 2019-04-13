#########################################
``Teste para desenvolvimento python``
#########################################


Descrição
***********

| O teste consiste em implementar um caso de uso.
| Trazer lista completa de Followers da conta https://www.instagram.com/evolutioncoffee/ via Scripting (Pode usar Webscraping, API, etc, etc)
| Desenvolver Django para CRUD e visualização dos dados
| Enviar instruções de instalação


:Date: **11/04/2019**
:Author: **Sidon Duarte**

TL;DR
*******
| A aplicação foi hospedada no `Heroku <http://www.heroku.com>`_.
| Para testá-la clique: https://desinchallenge.herokuapp.com/.
| Repositorio no github: https://github.com/Sidon/desinchallenge.

Ambiente de desenvolvimento:
****************************

    +-------------------+---------------------------+------------+
    | Resource          | Description               | Version    |
    +===================+===========================+============+
    | Computer          | Desktop 8 GB Memory       | I5 G5      |
    +-------------------+---------------------------+------------+
    | Operating System  | Ubuntu  LTS               | 18.04      |
    +-------------------+---------------------------+------------+
    | Editor/IDE        | Pycharm                   | 2019.1     |
    +-------------------+---------------------------+------------+
    | venv              | Conda (Miniconda)         | 4.3.14     |
    +-------------------+---------------------------+------------+
    | Devel Platform    + Django/Python             | 3.7        |
    +-------------------+---------------------------+------------+
    | CI                | CircleCI                  | 2017-08    |
    +-------------------+---------------------------+------------+
    | Coverage          | Codecov                   |            |
    +-------------------+---------------------------+------------+
    | Django            | Main framework            | 2.2        |
    +-------------------+---------------------------+------------+
    | DRF               | dajano-rest-fw            |  3.9       |
    +-------------------+---------------------------+------------+


Instalação local
****************

1 - Clone o repositório e navegue para o diretorio

.. code-block::

    $ git clone https://github.com/Sidon/desinchallenge.git
    $ cd desinchallenge


3 - Crie um ambiente virtual com seu gerenciador de venv, exempo com miniconda:

.. code-block::

    $ conda create -n desinchallenge python = 3.7


4 - Instale os pacotes necessários

.. code-block::

    # Mude para o ambiente criado
    $ source activate desinchallenge
    $ pip install -r requirements.txt


Recriação do Banco de dados (Opcional)
**************************************

1 - Apague o banco

.. code-block::

    # Exemplo no linux
    $ rm -rf challenge.sqlite3

2 - Limpe as migrations

.. code-block::

    $ python manage.py clmigrations

3 - Crie as migrations (Recriando o banco)

.. code-block::

    $ python manage.py makemigrations
    $ python manage.py migrate

4 - Crie um superuser com o nome admin

.. code-block::

    $ python manage.py createsuperuser

5 - Popule o banco com os dados iniciais (cerca de 40 a 50 minutos)

.. code-block::

    $ python manage.py initialdata


Execução local (modo dev)
*************************

    Para execução local execute o `runserver` informando o numero da porta, o default é `8000`

.. code-block::

    $ manage.py runserver 8000



4 - Execute os testes do sistema :

.. code-block::

    $ python manage.py test

5 -  Crie o banco de dados com os dados iniciais

.. code-block::

    $ python manage.py initialdata


6 -  Execute a aplicação:

.. code-block::

    $ python manage.py runserver

7 -  Acesse a pagina principal

.. code-block::

    http://127.0.0.1:8000/


Acessando a API via Curl
*************************

API Root:
============

.. code-block::


    $ curl https://desinchallenge.herokuapp.com/api/
    {"followers":"https://desinchallenge.herokuapp.com/api/followers/"}


Listar todos os followers
=========================


.. code-block::

    curl -H 'Accept: application/json; indent=4' -u admin:master.21 desinchallenge.herokuapp.com/api/followers/

[
    {
        "id_instagram": 32842718,
        "full_name": "Augusto Gonçalves",
        "user_name": "augusto_1977",
        "profile_url": "https://www.instagram.com/augusto_1977",
        "links": {
            "self": "http://desinchallenge.herokuapp.com/api/followers/1/"
        }
    },
    {
        "id_instagram": 1417072262,
        "full_name": "Roberta Mellara",
        "user_name": "melararoberta",
        "profile_url": "https://www.instagram.com/melararoberta",
        "links": {
            "self": "http://desinchallenge.herokuapp.com/api/followers/2/"
        }
    },


    ...


Listar somente as 2 primeiras followers
=======================================

.. code-block::

        curl -H 'Accept:application/json;indent=4' -u admin:master.21  desinchallenge.herokuapp.com/api/followers/?limit=2





Listar baseado no critério: come-soon
========================================================

