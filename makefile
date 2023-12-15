all: mypy interpret 


mypy:
	mypy main.py rsa.py auxiliar.py

interpret:
	python3 main.py 