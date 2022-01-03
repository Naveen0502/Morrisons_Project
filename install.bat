py -3 -m venv .venv
CALL .venv\scripts\activate
pip install -r requirment.txt
coverage run --source=pytest -m py.test
coverage html
PAUSE