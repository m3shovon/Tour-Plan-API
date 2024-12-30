# Tour Plan API

<!-- Virtual env on windows -->

$ python -m venv venv
$ source venv/Scripts/activate


<!-- Upgrade requirements.txt packages to latest -->

pip install pip-upgrader
pip-upgrade

<!-- Install requirements.txt -->

pip install -r requirements.txt

<!-- Run project -->

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

<!-- Create supersuer -->

python manage.py createsuperuser

<!-- Cpanel setup -->

video tutorial - https://www.youtube.com/watch?v=dJWVL15Jpws
mysql setup - https://pythonfusion.com/deploy-django-on-shared-hosting/

<!-- sudo apt-get update

sudo apt-get -y install python3-pip

sudo apt install libpq-dev python3-dev

pip3 install psycopg2 -->


<!-- To Solve Migration Errors

python manage.py migrate --fake [app] zero
python manage.py migrate --fake
python manage.py makemigrations [app] --empty 

If SSL:
python manage.py runsslserver

POSTGRES:
sudo su - postgres
psql -U postgres -c "GRANT ALL PRIVILEGES ON SCHEMA public TO USER_NAME;"


-->

