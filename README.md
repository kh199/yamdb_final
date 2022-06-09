![example workflow](https://github.com/kh199/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## Описание проекта

Проект **YaMDb** собирает **отзывы (Review)** пользователей на произведения **(Titles)**. Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список **категорий (Category)** может быть расширен администратором.
Сами произведения в **YaMDb** не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
В каждой категории есть **произведения**: книги, фильмы или музыка. 
Произведению может быть присвоен **жанр (Genre)** из списка предустановленных. Новые жанры может создавать только администратор.

К проекту по адресу `http://127.0.0.1/redoc/` подключена документация API YaMDb. В ней описаны возможные запросы к API и структура ожидаемых ответов. Для каждого запроса указаны уровни прав доступа: пользовательские роли, которым разрешён запрос.

## Установка

Клонировать репозиторий:
```
git clone https://github.com/kh199/yamdb_final
```
Создать и заполнить файл .env:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```
Запустить docker-compose:
```
docker-compose up -d
```
Выполнить миграции:
```
docker-compose exec web python manage.py migrate
```
Создать суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```
Подгрузить статику:
```
docker-compose exec web python manage.py collectstatic --no-input 
```
Заполнить базу тестовыми данными:
```
docker-compose exec web python manage.py loaddata fixtures.json
```
Создать суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```

## Авторы
+ **Евгений Альбрант** [albrant](https://github.com/albrant)
+ **Екатерина Каричева** [kh199](https://github.com/kh199)
+ **Анастасия Нестеренко** [AnastasiaNesterenko](https://github.com/AnastasiaNesterenko)
