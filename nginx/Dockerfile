FROM debian:bookworm-slim

MAINTAINER Ten Souto <soutobhms@fab.mil.br>

# Essa variável de ambiente é usada para controlar se o Python deve
# gravar arquivos de bytecode (.pyc) no disco. 1 = Não, 0 = Sim
ENV PYTHONDONTWRITEBYTECODE 1

# Define que a saída do Python será exibida imediatamente no console ou em
# outros dispositivos de saída, sem ser armazenada em buffer.
# Em resumo, você verá os outputs do Python em tempo real.
ENV PYTHONUNBUFFERED 1

WORKDIR /etc/nginx

EXPOSE 80
# EXPOSE 443

# RUN executa comandos em um shell dentro do container para construir a imagem.
# O resultado da execução do comando é armazenado no sistema de arquivos da
# imagem como uma nova camada.
# Agrupar os comandos em um único RUN pode reduzir a quantidade de camadas da
# imagem e torná-la mais eficiente.
RUN apt-get update && apt-get upgrade -y && \
  apt-get install -y tzdata locales netcat-openbsd nginx-full vim && \
  ln -fs /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
  sed -i 's/# pt_BR.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen && \
  locale-gen && \
  update-locale LANG=pt_BR.UTF-8 && \
  mkdir -p /var/django && \
  chown -R www-data:www-data /var/django

COPY .bashrc /root
# A cópia tem ser feita após a instalação do nginx
# se copiar antes ira dar erro na instalação do pacote nginx-full
COPY nginx.conf .
COPY default sites-available

CMD ["nginx", "-g", "daemon off;"]
