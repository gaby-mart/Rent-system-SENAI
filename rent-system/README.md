# Anotações das Aulas de Back-End


### Comandos para iniciar o projeto:
- `django-admin startproject "nome_do_projeto" .` -> Cria o projeto DJANGO
- `django-admin startapp "nome_da_aplicacao"` -> Cria a aplicação Rest Framework


### Comandos de migração:
- `py manage.py makemigrations` -> Cria a migração
- `py manage.py migrate` -> Atualiza o banco para a migração atual


### Entendendo auth_user
Os principais campos são:
- `is_superuser` -> Diz o usuário é o root (usuário com acesso total à aplicação) ou não
- `is_staff` -> Diz se o usuário é administrador ou não
- `is_active` -> Diz se o usuário está ativo ou não

### Comandos
- `py manage.py createsuperuser` -> Cria o usuário root da aplicação
- `py manage.py runserver` -> Inicializa o servidor

### JWT
- `https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html` -> Documentação Oficial Jwt Django
- `pip install djangorestframework-simplejwt` -> Instala o JWT
- `pip install djangorestframework-simplejwt[crypto]` -> Instalação das dependencias de criptografia
