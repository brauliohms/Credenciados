# Credenciados

_Sistema para cadastro dos credenciados do FUNSA-GSAU-YS_

## Instalação

- Instale o **python** versão 3.x, **venv** e o **pip** no seu sistema operacional
`sudo apt install python3-pip python3-venv` (Debian)
- Clone esse repositório: `git clone https://github.com/brauliohms/Credenciados.git`
- Vá até o repositório: `cd Credenciados`
- Crie um ambiente virtual: `python3 -m venv venv` (Debian)
`python -m venv venv` (Windows)

> Em ambientes Debian o binário do python é python3 e no Windows apenas python

- Ativar ambiente virtual: `source venv/bin/activate` (Debian)
`venv\Scripts\Activate` (Windows)

- Instalar as dependências de desenvolvimento: `pip install -r requirements-dev.txt`

> Se for deploy em um servidor, utilizar pip install -r requirements.txt

- Criar as tabelas do Banco de Dados: `python manage.py migrate`
- Criar o Super Usurário para área Admin: `python manage.py createsuperuser`
- Criar os arquivos estáticos no diretório static/: `python manage.py collectstatic`
- Importar a base de dados da tabela credenciados com todos os cadastrados atualmente:
`python manage.py loaddata scripts/credenciados.json`

## Utilização

### Dev ou Análise

- Ter finalizado todos os passos da **Instalação**
- Ativar o ambiente virtual caso não esteja ativado `source venv/bin/activate`
- Suba o servidor do django para Dev ou Análise: `python manage.py runserver`
- Acesse o sistema web em um navegador através do seguinte endereço:
`http://127.0.0.1:8000`

### Testes

Para realizar todos os testes:

- Ter finalizado todos os passos da **Instalação**
- Ativar o ambiente virtual caso não esteja ativado `source venv/bin/activate`
- Rodar o comando para executar os testes `python manage.py test`

## Docker / Deploy

### Instalação e Configuração

- Primeiro editar os arquivos ocultos com as variáveis de ambiente:
`.env-dev` para ambiente de desenvolvimento e testes.
`.env-prod` para o ambiente de produção (deploy) e deixar igual as configurações
do banco de dados postgresql no arquivo `.env-psql`.
- Instalar os pacotes para uso do docker `apt install docker.io docker-compose`
- Para usar o usuario regular do sistema com o docker adicionar o usuario ao
grupo docker `adduser usuarioregular docker` e reiniciar sistema ou se preferir,
utilizar o docker com o usuario `root` não é necessario adicionar usuario regular
no grupo docker.

### Rodar

#### Desenvolvimento

- Para criar as imagens e subir os containers com o ambiente de desenvolvimento:
`docker-compose -f docker-compose.dev.yml up -d --build`
- para acompanhar os logs em tempo real:
`docker-compose -f docker-compose.prod.yml logs -f`
- para fechar os containers:
`docker-compose -f docker-compose.prod.yml down`
- para iniciar em segundo plano:
`docker-compose -f docker-compose.prod.yml up -d`

#### Produção

- Para criar as imagens e subir os containers com o ambiente de desenvolvimento:
`docker-compose -f docker-compose.prod.yml up -d --build`
- Importar a base de dados da tabela credenciados com todos os cadastrados atualmente:
`docker exec -it django_credenciados bash`
`python manage.py loaddata scripts/credenciados.json`
- Para sair do terminal de dentro do container:
`exit` ou `CTRL + c`
