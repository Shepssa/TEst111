# sasha-ecommerce
Cool description

## To download libs use
Inside project root run this command in bash
```
python -m venv venv
venv\Scripts\activate on windows
source venv/bin/activate on Mac/Linux
pip install -r requirements.txt
```

## Init project
To initialize project
```
python manage.py migrate
python manage.py createsuperuser
```

## To collect static for deploy
```
python manage.py collectstatic
```

## To run project
xxxx means the port of the app
by the default port equals 8000
and the app run on http://localhost:8000/
```
python manage.py runserver xxxx
```
