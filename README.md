
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
# status_summary_2023-07-01T00-03-46.csv
Ссылка на документацию Версия Статус
https://docs.python.org/3.13/ 3.13 in development
https://docs.python.org/3.12/ 3.12 pre-release
https://docs.python.org/3.11/ 3.11 stable
https://docs.python.org/3.10/ 3.10 security-fixes
https://docs.python.org/3.9/ 3.9 security-fixes
https://docs.python.org/3.8/ 3.8 security-fixes
https://docs.python.org/3.7/ 3.7 security-fixes
https://docs.python.org/3.6/ 3.6 EOL
https://docs.python.org/3.5/ 3.5 EOL
https://docs.python.org/2.7/ 2.7 EOL
https://www.python.org/doc/versions/ All versions
```
#### Команда c отформатированным выводом в консоль 
```
python src/main.py latest-versions -o pretty
```
**Полученный результат**
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
