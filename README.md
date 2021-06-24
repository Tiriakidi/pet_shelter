# pet_shelter 
Доступ в админ-панель: polina / qwerty

#ЗАПУСК ПРОЕКТА MACOS на локальном сервере

```
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
