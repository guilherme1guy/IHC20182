## Preparando o ambiente

#### Preparativos
- Confira se possui o python3.6
- Confira se possui o pip3.6

#### Instalando a máquina virtual

> $ pip3.6 install virtualenv

#### Configurando e iniciando a máquina virtual
> $ virtualenv -p python3.6 --no-site-packages venv

#### Ativando a máquina virtual
> $ source venv/bin/activate

#### Instalando dependências necessárias na máquina
> (venv)$ sudo apt-get install python3.6-dev libmysqlclient-dev

> (venv)$ python3.6 -m pip	 install --upgrade pip

> (venv)$ pip install --upgrade -r requirements.txt

Agora sua máquina está pronta para a manipulação do projeto

#### Desativando a máquina virtual

> (venv)$ deactivate
