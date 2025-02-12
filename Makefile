git-pull: 
	echo "Pulling from git"
	git stash && git pull

start:
	echo "Starting the project"
	python3 -m venv venv
	. venv/bin/activate
	pip install -r requirements.txt
	python embarcatech-tarefa7-web/manage.py runserver

deploy: git-pull start

cd:
	ssh root@200.137.2.7 'cd /var/embarcatech && make deploy'
