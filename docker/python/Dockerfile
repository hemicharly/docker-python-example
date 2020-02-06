# Imagem do python
FROM python:3.7-slim

# Instalando libs do sistema operacional para mysql
RUN apt-get update \
 && apt-get install -y python3-dev python3-mysqldb \
 && apt-get clean


# Cria pasta de logs
RUN mkdir -m 777 /logs

# Local aonde será salvo o projeto
WORKDIR /app

# Copiando as libs do projeto
COPY docker/python/requirements.txt requirements.txt

# Instalando as lib do projeto python
RUN pip3 install -r requirements.txt

# Iniciando a aplicação python
CMD ["gunicorn", "--bind", "0.0.0.0:8000","wsgi:app"]

