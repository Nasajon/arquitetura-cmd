empacotar:
	python empacotar.py

pyinstaller:
	pyinstaller --hidden-import pg8000 --onefile --console --name "arquitetura-cmd" ./__main__.py