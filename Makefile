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
<<<<<<< HEAD
	ssh root@200.137.2.7 'cd /var/embarcatech && make deploy'
=======
	ssh root@200.137.2.7 'cd /var/embarcatech && make deploy'
>>>>>>> cb513cc062069123b1356b6ad342df1328cde51c
