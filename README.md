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

1. Rodar o projeto
```
  make up
```
2. A API está rodando na porta 5000
  - Para testar, envie uma requisição para http://localhost:5000/

### Rodar na máquina

1. Rodar o projeto
```
  make up-machine
```
2. A API está rodando na porta 5000
  - Para testar, envie uma requisição para http://localhost:5000/
