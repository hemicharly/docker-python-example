# Imagem do python
FROM python:3.7-alpine

# Instalando as lib do projeto python
RUN pip3 install flask

# Cria pasta de logs
RUN mkdir -m 777 /logs

# Local aonde será salvo o projeto
WORKDIR /app

# Copiando os arquivos do projeto para dentro do docker
COPY ./app/src ./

# Iniciando a aplicação python
CMD ["python", "app.py"]

