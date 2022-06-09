# Teste - Ced/codec 
## Autora:  Marcielle de Paula Jorge
  
<br>

Esse repositório é sobre um  sistema de adminitração de uma Livraria usando o Framework Django e para o front-end Bootstrap e o Banco de dados Postgree
com esse sistema é possivel listar, adicionar livros, editar ou deletar um livro existente.

## As seguintes ferramentas foram usadas na construção do projeto:
- Django - Python Web Framework: https://www.djangoproject.com/ 
- PostgreeSQL - https://www.pgadmin.org/
- Docker - https://www.docker.com/
- Bootstrap - CSS & JS Library: https://getbootstrap.com/
- SweetAlert 2 - https://sweetalert2.github.io/

<br>

Arquitetura:  
Docker servers:

Server: Django with Django Rest Framework and Djoser
Frontend: Bootstrap
DB: PostgreSQL

Funcionalidades:
Adicionar Livros, editar seus atributos/Caracteristicas, listar por categoria e deletar livros existentes


Prerequisites
Python  
Python Pip
Docker,

Pre-requisitos:
 Instalar docker: https://docs.docker.com/desktop/windows/install/


Comandos para executar este projeto
Construir a imagem do docker e iniciar o contêiner

    docker-compose up -d --build  

O proprio docker vai se encarregar de carregar o python ja instalando as dependencias do projeto que estao no arquivo `requirements.txt`  
após iniciado é preciso executar os seguintes comandos para criar as tabelas no bando de dados:
    
    docker-compose exec web python manage.py migrate

Após executar o ultimo comando você pode cadastrar acessar o sistema e cadastrar novos items, para isso use:

>http://localhost:8000/  

ou você pode acessar o admin e cadastrar, execute o seguinte comando para criar um novo super usuário
    
    docker-compose exec web python manage.py createsuperuser

e em seguida acesse, para acessar o modulo de Admin.
>http://localhost:8000/admin/  

para fechar o docker e encerrar a execução do containêrs

    docker-compose down  


