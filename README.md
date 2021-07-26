# Bank Security Control Panel

Система слежения за посетителями банка.


## Настройка
В папке project должен быть создаг файл `.env`, в нем нужно создать и заполнить по образцу
```
ENGINE = django.db.backends.postgresql_psycopg2
HOST = pypo.org
PORT = 5124
NAME = checklist
USER = slime
PASSWORD = osipov123
SECRET_KEY = REPLACE_ME
ALLOWED_HOSTS = 127.0.0.1

DEBUG = True
```
Строка `DEBUG` опциональная.

## Запуск

Для запуска блога у вас уже должен быть установлен Python 3.

Установите зависимости:

```sh
$ pip install -r requirements.txt
```

Запустите сервер

```sh
$ python manage.py runserver 0.0.0.0:8000
```
