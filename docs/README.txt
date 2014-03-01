honcho start --port 8000
python manage.py runserver --settings=gitpop2.dev_settings
python manage.py test --settings=gitpop2.dev_settings gitpop2
