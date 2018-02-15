default: web

web:
	./ve python -m scripts.web

install:
	./ve pip install -r requirements.txt

