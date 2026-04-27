# YouGile Auto Tests

## Описание
Автоматизация UI и API тестов YouGile

## Стек
- Selenium
- Pytest
- Requests
- Allure

## Запуск

UI:
pytest -m ui

API:
pytest -m api

Все:
pytest

## Allure отчет
pytest --alluredir=allure-results
allure serve allure-results

## Ссылка на ручное тестирование
https://legkih-qa-skypro.yonote.ru/share/b33ba8e9-85dd-4417-92f6-fa8bbf88b647

## Особенности
- Динамическое получение user_id
- Генерация уникальных данных
- Использование фикстур
- Разделение UI/API

## Запуск

pytest -m api
pytest -m ui
pytest