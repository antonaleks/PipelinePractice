# PipelinePractice
Пример [статус бейджа](https://docs.microsoft.com/en-us/azure/devops/pipelines/create-first-pipeline?view=azure-devops&tabs=java%2Ctfs-2018-2%2Cbrowser) с пайплайна:

[![Build Status](https://dev.azure.com/alekseevap/calculatorWebApi/_apis/build/status/antonaleks.calculatorWebApi?branchName=master)](https://dev.azure.com/alekseevap/calculatorWebApi/_apis/build/status/antonaleks.calculatorWebApi?branchName=master)

# Структура проекта
├── **guide**- *модуль с мануалом по заданию.*\
├── **entity**- *модуль сущностей.*\
│  ├── **calculator.py** - *класс Calculator, реализующий простые математические операции*\
├── **tests**- *модуль тестов.*\
│  ├── **functional_tests** - *модуль функциональных тестов*\
│  │  ├── **test_index.py** - *функциональные тесты с использованием фреймворка Selenium*\
│  │  ├── **yandexdriver.exe** - *драйвер для Selenium. Скачивается локально, в зависимости от браузера.* 
*Если используете yandexbrowser, драйвер можно скачать по [ссылке](https://github.com/yandex/YandexDriver/releases)* \
│  │  ├── **chromedriver.exe** - *драйвер для Selenium. Скачивается локально, в зависимости от браузера.* 
*Если используете chrome, драйвер можно скачать по [ссылке](https://chromedriver.chromium.org/downloads)* \
│  ├── **unit_tests** - *модуль юнит тестов*\
│  │  ├── **__init__.py** - *инициализация системного пути до модулей. Используется при запуске CI пайплайна (чтобы не ругался на путь к calculator.py).*\
│  │  ├── **test_calculator.py** - *юнит тесты класса Calculator*\
├── **azure-pipelines.yml**- *манифест запуска CI конвейера в репозитории Azure DevOps. Создается автоматически, заполняется на платформе Azure DevOps.*\
├── **requirements.txt**- *зависимости python.*\

# Задание
1. Локально запустить юнит и функциональные тесты
2. В репозитории организовать конвейер CI с запуском Юнит тестов, упаковкой приложения в архив. В readme указать лейбл с успешным прохождением пайплайна (по-желанию).
3. Организовать CD конвейр с разворачиванием приложения в Azure Web App, протестировать приложение фуникцональными тестами (автоматически при развертке)