# Credenciados

_Sistema para cadastro dos credenciados do FUNSA-GSAU-YS_

## Instalação

- Instale o **python** versão 3.x, e o **Virtualenv**
- Clone esse repositório: `git clone https://github.com/brauliohms/Credenciados.git`
- Vá até o repositório: `cd Credenciados`
- Crie um ambiente virtual: `python3 -m venv venv` (Debian)
`python -m venv venv` (Windows)

> Em ambientes Debian o binário do python é python3 e no Windows apenas python

- Ativar ambiente virtual: `source venv/bin/activate` (Debian)
`venv\Scripts\Activate` (Windows)

- Instalar as dependências: `pip install -r requirements-dev.txt`

> Se for deploy em um servidor, utilizar pip install -r requirements.txt

- Ajustar o Banco de Dados: `python manage.py makemigrations`
- Criar as tabelas do Banco de Dados: `python manage.py migrate`
- Criar o Super Usurário para área Admin: `python manage.py createsuperuser`
- Criar os arquivos estáticos no diretório static/: `python manage.py collectstatic`

## Utilização

### Dev ou Análise

- Suba o servidor do django para Dev ou Análise: `python manage.py runserver`
- Acesse o sistema web em um navegador através do seguinte endereço:
`http://127.0.0.1:8000`
