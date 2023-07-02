
# Проект асинхронный парсер PEP
## Технологии
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=gray)](https://www.python.org/) [![Scrapy](https://img.shields.io/badge/-Scrapy-464646?style=flat&logoColor=56C0C0&color=gray)](https://scrapy.org/) 

Полный список модулей, используемых в проекте, доступен в [requirements.txt](https://github.com/NECROshizo/scrapy_parser_pep/blob/main/requirements.txt)
## Линтеры
[![Flake8](https://img.shields.io/badge/-flake8-464646?style=flat&logo=flake8&logoColor=56C0C0&color=gray)](https://flake8.pycqa.org/)

## Описание проекта
Данный парсер выполняет следующие функции:
- Собирает в один фаил формата csv список всех PEP с номером, названием и статусом.
- Собирает в один фаил формата csv сводную таблицу количество всех статусов PEP.

## Установка и настройки
#### Клонирование репозитория:

```
git clone git@github.com:NECROshizo/scrapy_parser_pep.git
```

#### Создание виртуального окружения:

```
python -m venv venv
```

#### Запуск виртуального окружения:

```
source venv/Scripts/activate - команда для Windows
source venv/bin/activate - команда для Linux и macOS
```
#### Установка зависимостей:

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
## Использование парсера
#### Запуск парсера
```
scrapy crawl pep
```
**Результат сохранен в директории result**
```
Статус,Количество
Final,274
Accepted,51
Active,31
Rejected,12
Superseded,20
Withdrawn,56
April Fool!,1
Deferred,37
Draft,23
Total,615
```

## Автор
[**Оганин Пётр**](https://github.com/NECROshizo) 
2023 г.
