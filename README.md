# Atividade CRUD – Django

Projeto desenvolvido para a Atividade Avaliativa, contendo um CRUD completo de funcionários.

## Tecnologias utilizadas
- Python 3
- Django
- MySQL
- Docker / Docker Compose

## Funcionalidades
- Cadastro de funcionário
- Listagem de funcionários
- Persistência em banco MySQL
- Interface web com Django Templates

## Como executar o projeto

```bash
docker-compose up -d
python manage.py migrate
python manage.py runserver
