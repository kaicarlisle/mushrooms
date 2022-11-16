PYTHON=python3
ENV=venv
PY=$(ENV)/bin/python3


venv:
	$(PYTHON) -m venv $(ENV)
	$(PY) -m pip install -r requirements.txt

black: venv
	$(PY) -m black . --exclude="$(ENV)"
