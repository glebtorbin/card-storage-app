## Описание проекта:
В проекте реализована база для хранения банковских и каких-либо других карт 

### Через API-сервис можно сделать следующие запросы:
* Получение публикаций методом GET /api/v1/card-list/. Также реализован поиск по всем полям

* Получение информации о конкретной карте со всеми транзакциями по ней: GET /api/v1/card/{card_id}/detail/

* Активация карты: GET /api/v1/card/{card_id}/activate/

* Удаление карты: GET /api/v1/card/{card_id}/delete/

* Обновление статуса карт: GET /api/v1/update-status/

* Генератор карт, поля: 
- series: серия карты
- number: кол-во генерируемых карт
- term: срок действия карты
GET /api/v1/card/generate/{series}/{number}/{term}

## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/glebtorbin/card-storage-app.git
```
```
cd card-storage-app
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```
```
source venv/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
```
cd app
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```
