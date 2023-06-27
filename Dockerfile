FROM debian:bookworm-slim

MAINTAINER Braulio Henrique Marques Souto <braulio@disroot.org>

# Essa variável de ambiente é usada para controlar se o Python deve
# gravar arquivos de bytecode (.pyc) no disco. 1 = Não, 0 = Sim
ENV PYTHONDONTWRITEBYTECODE 1

# Define que a saída do Python será exibida imediatamente no console ou em
# outros dispositivos de saída, sem ser armazenada em buffer.
# Em resumo, você verá os outputs do Python em tempo real.
ENV PYTHONUNBUFFERED 1

# Entra na pasta /var/django no container
WORKDIR /var/django

# Copia a pasta "Credenciados" para dentro do container.
COPY . ./

#ENV PATH="$VIRTUAL_ENV/bin:$PATH"

#RUN pip install -r requirements.txt --break-system-packages

# A porta 8000 estará disponível para conexões externas ao container
# É a porta que vamos usar para o Django.
EXPOSE 8000

# RUN executa comandos em um shell dentro do container para construir a imagem.
# O resultado da execução do comando é armazenado no sistema de arquivos da
# imagem como uma nova camada.
# Agrupar os comandos em um único RUN pode reduzir a quantidade de camadas da
# imagem e torná-la mais eficiente.
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y netcat-openbsd python3-pip python3-venv vim && \
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
    chmod -R +x scripts

# Adiciona a pasta scripts e venv/bin
# no $PATH do container.
ENV PATH="/var/django/scripts:/venv/bin:$PATH"

# Muda o usuário para django
USER django

# Executa o arquivo scripts/commands.sh
#CMD ["commands.sh"]
#CMD ["/var/django/venv/bin/gunicorn", "--bind", ":8000", "--workers", "3", "core.wsgi:application"]
