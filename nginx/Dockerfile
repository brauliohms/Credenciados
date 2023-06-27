FROM nginx:1.25-bookworm

MAINTAINER Braulio Henrique Marques Souto <braulio@disroot.org>

COPY django.conf /etc/nginx/conf.d

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y vim && \
    mkdir -p /var/django && \
    chown -R www-data:www-data /var/django && \
    rm -rf /etc/nginx/conf.d/default.conf

EXPOSE 80 443
