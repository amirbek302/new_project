# Живой журнал — Django Social Network

Учебный проект на Django: мини-социальная сеть, в которой пользователи могут публиковать посты и ставить лайки.

## Возможности

- Регистрация, вход и выход из аккаунта
- Личный кабинет пользователя
- Создание и удаление публикаций
- Общая лента Interesting
- Просмотр профилей других пользователей
- Лайки и отмена лайков
- Переключение языков и тем оформления

## Технологии

- Python
- Django
- PostgreSQL
- HTML, CSS, JavaScript
- Git

## Установка и запуск

**1. Клонировать репозиторий**

```bash
git clone <https://github.com/amirbek302/new_project.git>
cd new_project
```

**2. Создать виртуальное окружение**

```bash
python -m venv .venv
```

Активировать в Windows:

```bash
.venv\Scripts\activate
```

**3. Установить зависимости**

```bash
pip install -r requirements.txt
```

**4. Создать базу данных PostgreSQL**

Создать базу данных с именем `social_network`.

**5. Настроить переменные окружения**

Создать файл `django_project/.env`:

```env
DB_NAME=social_network
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=127.0.0.1
DB_PORT=5432
```

При необходимости добавить другие переменные, используемые в `settings.py`.

**6. Перейти в папку Django-проекта**

```bash
cd django_project
```

**7. Применить миграции**

```bash
python manage.py makemigrations

python manage.py migrate
```

**8. Создание перевода и его применение**

```bash
django-admin makemessages -l ru
django-admin makemessages -l uz
#Если уже есть LC_MESSAGES
#                  django.po то необязательно

python manage.py compilemessages  
```

**9. Запустить сервер**

```bash
python manage.py runserver
```

Открыть сайт:

http://127.0.0.1:8000/

## Автор

Амирбек

## Назначение

Практическая работа по Django — создание аналога «Живого журнала».
#### Читай Ниже
#### Если прочитали и не поставили звезду в проект то вы gay