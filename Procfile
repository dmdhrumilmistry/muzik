web: gunicorn muzik.wsgi
worker: sh -c "python manage.py migrate; python manage.py collectstatic;"