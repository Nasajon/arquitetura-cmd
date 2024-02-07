empacotar:
	python3 empacotar.py

pyinstaller:
	pyinstaller --hidden-import pg8000 --onefile --console --name "arquitetura-cmd" ./__main__.py