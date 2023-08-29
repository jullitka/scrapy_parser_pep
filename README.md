# Асинхронный парсер PEP

Асинхронный парсер собирающий данные PEP с сайта https://www.python.org/.

- Парсер собирает данные (номер, название, статус) со страниц PEP и записывает их в файл формата .csv.
- Парсер подсчитывает количество PEP каждого статуса и количество всех документов.
Записывает полученные данные в файл .csv
## Стек технологий:
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Scrapy](https://img.shields.io/badge/-Scrapy-464646?logo=Scrapy)](https://docs.scrapy.org/en/latest/)

## Запуск проекта
- Клонировать репозиторий и перейти в директорию проекта:
```
git clone https://github.com/jullitka/scrapy_parser_pep.git
cd scrapy_parser_pep
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
- Запустить парсер
```
scrapy crawl pep
```
## Авторы
[Юлия Пашкова](https://github.com/Jullitka)
