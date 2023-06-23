# backend-events-time

## Requisitos
- [Docker] (https://www.docker.com/)
- [Python] (https://www.python.org/)
- [Makefile] (https://sourceforge.net/projects/gnuwin32/files/latest/download)
- [Dbeaver] (https://dbeaver.io/) ou outro gerenciador de banco

## Tecnologias
- [Orator] (https://orator-orm.com/docs/0.9)
- [Flask] (https://flask.palletsprojects.com/en/2.3.x/)

## Setup

### Rodar com docker

1. Rodar o projeto com:
```
  make up-silent db-migrate
```
Se quiser ver os logs, rodar o comando:
```
  make up
```
2. A API está rodando na porta 5000
  - Para testar, envie uma requisição para http://localhost:5000/

### Rodar os testes
```
  make test
```

## Rodar com Insomnia
[![Run in Insomnia}](https://insomnia.rest/images/run.svg)](https://insomnia.rest/run/?label=Events%20Time%20API&uri=https%3A%2F%2Fraw.githubusercontent.com%2Fvictorkoji%2Fbackend-events-time%2Fmain%2Finsomnia_api.json%3Ftoken%3DGHSAT0AAAAAACD4GJIJDDBPLTDB7LZG3K2IZERBT4Q)
