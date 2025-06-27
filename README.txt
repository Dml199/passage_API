passage_API

Описание проекта:

passage_API — это серверное приложение, реализующее REST API для приема данных о горных перевалах от туристов. 
С помощью этого API мобильное приложение может отправлять информацию о перевале (координаты, фотографии, название, данные пользователя и др.) на сервер, где она сохраняется в базе данных.

Функционал:

Прием POST-запроса с данными о перевале в формате JSON.
Валидация и сохранение информации в базе данных.
Хранение фотографий и пользовательских данных.
Возврат статуса операции и идентификатора созданной записи.

Требования:

Python 3.8+
PostgreSQL


Быстрый старт:

1.Создайте файл проекта - example_project.

2. Клонируйте репозиторий bash
cd example_project
git clone https://github.com/Dml199/passage_API.git


3. Создайте файл .env в папке "App" проекта. Создайте там следующие переменные.
FSTR_DB_HOST=localhost
FSTR_DB_PORT=5432
FSTR_DB_LOGIN=your_db_user
FSTR_DB_PASS=your_db_password

Примечание:

FSTR_DB_HOST — адрес сервера базы данных (например, localhost или IP).
FSTR_DB_PORT — порт базы данных (обычно 5432 для PostgreSQL).
FSTR_DB_LOGIN — имя пользователя для подключения к базе данных.
FSTR_DB_PASS — пароль пользователя базы данных.

4. Запустите скрипт start.sh командой "source start.sh"

После успешного запуска проекта, для проверки работоспособности введите в консоли следующий запрос:

curl -X POST http://localhost:8000/submitData \
  -H "Content-Type: application/json" \
  -d '{
    "beauty_title": "пер. ",
    "title": "Пхия",
    "other_titles": "Триев",
    "connect": "",
    "add_time": "2021-09-22 13:18:13",
    "user": {
      "email": "qwerty@mail.ru",
      "fam": "Пупкин",
      "name": "Василий",
      "otc": "Иванович",
      "phone": "+7 555 55 55"
    },
    "coords": {
      "latitude": "45.3842",
      "longitude": "7.1525",
      "height": "1200"
    },
    "level": {
      "winter": "",
      "summer": "1А",
      "autumn": "1А",
      "spring": ""
    },
    "images": [
      {"data": "<картинка1>", "title": "Седловина"},
      {"data": "<картинка2>", "title": "Подъём"}
    ]
  }'
    

Формат ответа

Успех:
{ "status": 200, "message": null, "id": 42 }

Ошибка:
{ "status": 400, "message": "Bad Request: missing required fields", "id": null }

Примечание: 
Все комманды и скрипты были написаны для работы на операционной системе Linux (Debian Destribution) и могут не сработать на других операционных системах.

Контакты:
Если возникли вопросы или предложения, пишите на takszent@gmail.com
