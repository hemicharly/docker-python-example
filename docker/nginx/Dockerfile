FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf

WORKDIR /application

RUN mkdir -p /etc/nginx/sites-enabled

COPY docker/nginx/nginx.conf /etc/nginx/nginx.conf

CMD ["nginx", "-g", "daemon off;"]
