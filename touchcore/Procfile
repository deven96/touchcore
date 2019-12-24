release: python manage.py migrate
web: gunicorn touchcore.wsgi --log-file - --log-level debug
