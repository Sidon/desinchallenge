#########################################
``Teste para desenvolvimento python``
#########################################


Descrição
**********

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


3 - Crie um ambiente virtual com seu gerenciador de venv, exemplo com miniconda:

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

1 - Execute o `runserver` informando o numero da porta, o default é `8000`

.. code-block::

    $ manage.py runserver 8000

2 -  Acesse a pagina principal

.. code-block::

    http://127.0.0.1:8000/



#########################
Acessando a API via Curl
#########################


API Root:
*********

.. code-block::


    $ curl https://desinchallenge.herokuapp.com/api/
    {"followers":"https://desinchallenge.herokuapp.com/api/followers/"}


Listar todos os registros
=========================


.. code-block::

    $ curl -H 'Accept: application/json; indent=4' -u admin:master.21 desinchallenge.herokuapp.com/api/followers/

    [
        {
            "id_instagram": 32842718,
            "full_name": "Augusto Gonçalves",
            "user_name": "augusto_1977",
            "profile_url": "https://www.instagram.com/augusto_1977",
            "is_private": "Private",
            "links": {
                "self": "http://desinchallenge.herokuapp.com/api/followers/1/"
            }
        },
        {
            "id_instagram": 1417072262,
            "full_name": "Roberta Mellara",
            "user_name": "melararoberta",
            "profile_url": "https://www.instagram.com/melararoberta",
            "is_private": null,
            "links": {
                "self": "http://desinchallenge.herokuapp.com/api/followers/2/"
            }
        },
        ...
    ]


Listar somente os 2 primeiras registros
=======================================

.. code-block::

    $ curl -H 'Accept:application/json;indent=4' -u admin:master.21  desinchallenge.herokuapp.com/api/followers/?limit=2
    [
        {
            "id_instagram": 32842718,
            "full_name": "Augusto Gonçalves",
            "user_name": "augusto_1977",
            "profile_url": "https://www.instagram.com/augusto_1977",
            "is_private": "Private",
            "links": {
                "self": "http://desinchallenge.herokuapp.com/api/followers/1/"
            }
        },
        {
            "id_instagram": 1417072262,
            "full_name": "Roberta Mellara",
            "user_name": "melararoberta",
            "profile_url": "https://www.instagram.com/melararoberta",
            "is_private": null,
            "links": {
                "self": "http://desinchallenge.herokuapp.com/api/followers/2/"
            }
        }
    ]


Listar os registros cujo flag de privacidade seja Private
=========================================================

    $ curl -H 'Accept:application/json;indent=4' -u admin:master.21  desinchallenge.herokuapp.com/api/followers/?isprivate

.. code-block::

    [
        {
            "id_instagram": 32842718,
            "full_name": "Augusto Gonçalves",
            "user_name": "augusto_1977",
            "profile_url": "https://www.instagram.com/augusto_1977",
            "is_private": "Private",
            "links": {
                "self": "http://localhost:8000/api/followers/1/"
            }
        },
        {
            "id_instagram": 1401570783,
            "full_name": "Brenah",
            "user_name": "breninhavasconcelos",
            "profile_url": "https://www.instagram.com/breninhavasconcelos",
            "is_private": "Private",
            "links": {
                "self": "http://localhost:8000/api/followers/4/"
            }
        },

        ....
     ]


Busca pelo `id` no instagram
============================

.. code-block::

    $ curl -H 'Accept:application/json;indent=4' -u admin:master.21  localhost:8000/api/followers/?idinstagram=1524004563
    [
        {
            "id_instagram": 1524004563,
            "full_name": "Sidon Duarte",
            "user_name": "sidonduarte",
            "profile_url": "https://www.instagram.com/sidonduarte",
            "is_private": null,
            "links": {
                "self": "http://localhost:8000/api/followers/40/"
            }
        }
    ]


Busca pelo Username no instagram
=================================

.. code-block::

    $ curl -H 'Accept:application/json;indent=4' -u admin:master.21  localhost:8000/api/followers/?username=sidonduarte
    [
        {
            "id_instagram": 1524004563,
            "full_name": "Sidon Duarte",
            "user_name": "sidonduarte",
            "profile_url": "https://www.instagram.com/sidonduarte",
            "is_private": null,
            "links": {
                "self": "http://localhost:8000/api/followers/40/"
            }
        }
    ]



Busca por uma parte do Full Name
================================

.. code-block::

    $ curl -H 'Accept:application/json;indent=4' -u admin:master.21  localhost:8000/api/followers/?fullname=sidon
    [
        {
            "id_instagram": 1524004563,
            "full_name": "Sidon Duarte",
            "user_name": "sidonduarte",
            "profile_url": "https://www.instagram.com/sidonduarte",
            "is_private": null,
            "links": {
                "self": "http://localhost:8000/api/followers/40/"
            }
        },
        {
            "id_instagram": 3259086590,
            "full_name": "Savio Possidonio",
            "user_name": "saviopossidonio",
            "profile_url": "https://www.instagram.com/saviopossidonio",
            "is_private": null,
            "links": {
                "self": "http://localhost:8000/api/followers/9773/"
            }
        }
    ]



