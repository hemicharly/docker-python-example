# Imagem do python
FROM python:3.7-alpine

# Cria pasta de logs
RUN mkdir -m 777 /logs

# Local aonde será salvo o projeto
WORKDIR /app

# Copiando as libs do projeto
COPY docker/python/requirements.txt requirements.txt

# Instalando as lib do projeto python
RUN pip3 install -r requirements.txt

# Iniciando a aplicação python
CMD ["python", "app.py"]

