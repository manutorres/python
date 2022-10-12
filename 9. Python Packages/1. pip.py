# pip install requests
# pip install --upgrade pip
# pip list
# pip install requests==2.20.0
# pip install requests==2.20.* Ultima version compatible
# pip uninstall requests
# pip install requests~=2.20.0 Ultima version compatible

# pip install pipenv => Pipenv maneja venvs y paquetes
# pipenv install requests => Crea venv con el nuevo paquete
# pipenv --venv => Path del nuevo virtual environment

# pipenv install => Genera venv nueva a partir de las dependencias
# especificadas en Pipfile (actualizadas posiblemente)
# pipenv install --ignore-pipfile => Genera venv nueva a partir de
# las dependencias especificadas en Pipfile.lock (versiones exactas)

import requests

response = requests.get("http://google.com")
print(response)
