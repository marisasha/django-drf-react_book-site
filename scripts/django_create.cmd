cd ..
cd back

python -m venv venv
call venv/scripts/activate

pip install django-cors-headers
pip install django pillow
pip install --upgrade djangorestframework-simplejwt





python manage.py runserver

cmd