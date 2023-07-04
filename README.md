# Асинхронный парсер PEP

Асинхронный парсер собирающий данные PEP с сайта https://www.python.org/.

#### Номер, название, статус 
Парсер собирает данные со страниц PEP и записывает их в файл формата .csv.

#### Статус - количество
Парсер подсчитывает количество PEP каждого статуса и сумму всех статусов.
Записывает полученные данные в файл .csv

## Запуск проекта
Клонировать репозиторий:
```
- git clone git@github.com:jullitka/scrapy_parser_pep.git
```
- Создать и активировать виртуальное окружение:
```
python3 -m venv env
source venv/Scripts/activate
```
- Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
## Запуск парсера
```
scrapy crawl pep
```
