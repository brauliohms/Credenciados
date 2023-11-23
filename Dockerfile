FROM debian:bookworm-slim

MAINTAINER Ten Souto <soutobhms@fab.mil.br>

# Essa variável de ambiente é usada para controlar se o Python deve
# gravar arquivos de bytecode (.pyc) no disco. 1 = Não, 0 = Sim
ENV PYTHONDONTWRITEBYTECODE 1

# Define que a saída do Python será exibida imediatamente no console ou em
# outros dispositivos de saída, sem ser armazenada em buffer.
# Em resumo, você verá os outputs do Python em tempo real.
ENV PYTHONUNBUFFERED 1

# Defina a variável de ambiente DEBIAN_FRONTEND como noninteractive
# para evitar interações do usuário
ENV DEBIAN_FRONTEND="noninteractive"

# Entra na pasta /var/django no container
WORKDIR /var/django

COPY ./config/.bashrc /root
COPY ./django_credenciados/requirements.txt .
COPY ./django_credenciados/requirements-dev.txt .
COPY ./scripts /scripts

# Copia a pasta "Credenciados" para dentro do container.
# Descomente apenas se NÃO usar docker-compose ou
# se usar docker run com -v e indicar caminho completo/idok:/var/django
# e comentar os COPY acima
# COPY . ./

# A porta 8000 estará disponível para conexões externas ao container
# É a porta que vamos usar para o Django.
EXPOSE 8000

# RUN executa comandos em um shell dentro do container para construir a imagem.
# O resultado da execução do comando é armazenado no sistema de arquivos da
# imagem como uma nova camada.
# Agrupar os comandos em um único RUN pode reduzir a quantidade de camadas da
# imagem e torná-la mais eficiente.
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y tzdata locales netcat-openbsd python3-pip python3-venv vim && \
    ln -fs /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
    sed -i 's/# pt_BR.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen && \
    update-locale LANG=pt_BR.UTF-8 && \
    python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r requirements.txt && \
    adduser --disabled-password --no-create-home django && \
    mkdir -p /var/django/static && \
    mkdir -p /var/django/media && \
    chown -R django:django /venv && \
    chown -R django:django . && \
    chmod -R 755 /var/django/static && \
    chmod -R 755 /var/django/media && \
    chmod -R 751 /scripts

# Adiciona a pasta /scripts e /venv/bin
# no $PATH do container.
ENV PATH="/scripts:/venv/bin:$PATH"
