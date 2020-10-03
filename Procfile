release: python manage.py makemigrations empresa --no-input
release: python manage.py migrate empresa --no-input
release: python manage.py makemigrations funcionario --no-input
release: python manage.py funcionario --no-input
release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input
web: gunicorn core.wsgi --log-file -