Дипломный проект. Задание 3: веб-приложение

UI-автотесты  для проверки программы, которая помогает заказать бургер в Stellar Burgers.

Реализованы сценарии для проверки функционала "Восстановление пароля", "Личный кабинет", "Основной функционал", "Лента заказов".


Запуск тестов происходит в Chrome и Firefox

Стек

Pytest, Allure-pytest, Selenium, Requests


Структура проекта

pages - пакет, содержащий код PageObject

tests - пакет, содержащий тесты, разделенные по классам. Например, bun_test.py, burger_test.py и т.д.

client - пакет, содержащий код api ручек для подготовки тетсовых данных

Запуск автотестов 

$ pytest tests --alluredir=allure_results

Установка зависимостей

$ pip install -r requirements.txt

Cоздание Allure отчета

$ allure serve allure_results
