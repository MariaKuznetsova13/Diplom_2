# Diplom_2
## Тесты на API "Stellar Burgers"

## Структура проекта
- allure_results - папка с отчетом о тестировании
- tests - папка с тестами
- conftest.py - фикстуры
- requirements.txt - файл с необходимыми библиотеками
- data.py - файл с данными для тестов
- helpers.py - файл с методами для тестов

## Запуск тестов
- Установка зависимостей - pip install -r requirements.txt
- Запуск тестов без отчета - pytest -v
- Запуск тестов с отчетом - pytest --alluredir=allure_results