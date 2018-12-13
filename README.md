[![Build Status](https://travis-ci.org/felipecolen/pyro-site.svg?branch=master)](https://travis-ci.org/felipecolen/pyro-site)
[![pipeline status](https://gitlab.com/PyNorte-RO/pyro-site/badges/master/pipeline.svg)](https://gitlab.com/PyNorte-RO/pyro-site/commits/master)
[![coverage report](https://gitlab.com/PyNorte-RO/pyro-site/badges/master/coverage.svg)](https://gitlab.com/PyNorte-RO/pyro-site/commits/master)
[![Requirements Status](https://requires.io/github/felipecolen/pyro-site/requirements.svg?branch=master)](https://requires.io/github/felipecolen/pyro-site/requirements/?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/2570ff99918ad5cd5d87/maintainability)](https://codeclimate.com/github/felipecolen/pyro-site/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/2570ff99918ad5cd5d87/test_coverage)](https://codeclimate.com/github/felipecolen/pyro-site/test_coverage)


# Site da PyRO
Site da comunidade Python Rondônia desenvolvido em Python com o microframework Flask


## Requisitos

* [Python 3.6.5](https://www.python.org/downloads/)
* [Flask 1.0](http://flask.pocoo.org/docs/1.0/)
* [Git](https://git-scm.com/)
* [Docker](https://www.docker.com/community-edition)


## Subindo o projeto

        pip install -r requirements.txt
        python app.py


## Subindo o projeto com docker

        pip install docker-compose
        docker-compose up

## Nginx
Caso o Nginx não esteja servindo os arquivos estáticos corretamente, execute o comando abaixo para verificar se o user www-data tem permissão

        sudo -u www-data stat /username/test/static
        
        
Caso não tenha, tente:

        gpasswd -a www-data username
        chmod g+x /username && chmod g+x /username/test && chmod g+x /username/test/static

Reinicie o Nginx

        nginx -s reload
        
        
Fonte: https://stackoverflow.com/questions/25774999/nginx-stat-failed-13-permission-denied