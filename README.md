# Scripts

As atividades (1 a 4) estão dentro da pasta scripts, e todas retornam as respostas com print no terminal.
- Na pasta raiz:
    - .venv\bin\activate
    - cd scripts
    - python main.py


# Backend

Para rodar o projeto é necessário dar os seguintes comandos no terminal.
- Na pasta raiz:
    - cd backend
    - venv\bin\activate
    - pip install -r requirements.txt
    - python manage.py runserver

Por padrão o projeto irá rodar na porta 8000.

- Endpoints:
    - http://127.0.0.1:8000/api/veiculos/ (GET)
    - http://127.0.0.1:8000/api/veiculos/?termo=Jeep/ (GET)
    - Json de requisição (POST, PUT)
        -  {
            "marca": "Ford",
            "nome": "Fiesta",
            "ano": 2012,
            "descricao": "Veículo compacto",
            "created": timezone.now(),
            "updated": timezone.now(),
            "vendido": False
        }
    - http://127.0.0.1:8000/api/veiculos/1 (DELETE)
    - http://127.0.0.1:8000/api/veiculos/nao_vendidos (GET)
    - http://127.0.0.1:8000/api/veiculos/por_decada (GET)
    - http://127.0.0.1:8000/api/veiculos/por_fabricante (GET)
    - http://127.0.0.1:8000/api/veiculos/ultima_semana (GET)

![image](https://github.com/user-attachments/assets/10f5bb2f-44dd-4cb4-98fd-e96fef189f2d)


# Frontend

Para rodar o projeto é necessário dar os seguintes comandos no terminal.
- Na pasta raiz:
    - cd frotend/app
    - ng serve

Por padrão o projeto irá rodar na porta 4200.

![image](https://github.com/user-attachments/assets/afd6f1d5-a740-4394-8fac-62db91fd3a15)

