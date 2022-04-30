# Задание

## Юнит тестирование (локальный запуск тестов)

1. Для юнит тестирования кода используется unittest либо pytest модули
2. Продемонстрировать пример юнит тестирования с классом calculator (реализует просты математические операции)
    1. Использовать интерпритатор Python3.X, где X>6
    2. Установить с помощью команды pip зависимости pytest
   ```shell
   pip install pytest
   ```
    3. Запустить тесты с помщью команды
   ```shell
   py.test tests/unit_tests
   ```
    4. Убедиться, что тесты пройдены
    5. Также можно настроить Pycharm для запуска тестов через IDE:
       ![img](assets/images/PycharmPytestSettings.png)\
       Далее запускать через:
       ![img](assets/images/RunTests.png)
3. Продемонстрировать ошибки при тестировании кода
    1. В классе Calculator допустить ошибку в функции (например в функции add вместо + написать оператор -)
    2. Запустить тесты
    3. Убедиться, что один из тестов не пройден

## Функциональное тестирование (локальный запуск тестов)

1. Для функционального тестирования кода используется модуль selenium
   ```shell
   pip install selenium
   ```
2. Продемонстрировать пример функционального тестирования с мини приложением на flask, которое выдает результаты
   операций класса калькулятор
    1. Установить selenium (команда выше). Скачать необходимый драйвер (chrome или yandex) и вложить в папку с
       функциональными тестами. Если используете chrome, необходимо указать путь к драйверу в переменной chrome_driver (
       сейчас стоит к yandexdriver, если не задана переменная среды ChromeWebDriver)
       Если используете ОС Linux, то вместо exe необходимо скачать драйвер для Linux.
    2. Запустить веб-приложение. Оно должно запуститься на localhost:5000
   ```shell
   python app.py
   ``` 
    3. Запустить тесты
   ```shell
   py.test tests/functional_tests
   ```
    4. Убедиться, что тесты пройдены
3. Продемонстрировать ошибки при тестировании кода (неверный тип, неверная строка)
    1. В файле app.py в методе add убрать из ```@app.route("/add/<int:a>&<int:b>")``` тип **int** (python будет
       воспринимать a и b как строки)
       Должно получится ```@app.route("/add/<a>&<b>")```
    2. Запустить веб-приложение и тесты
    3. Убедиться, что один из тестов не прошел (при сложении получается конкатенация строк, а не арифметическая
       операция)

## Pipeline - continuous integration (CI) with Azure DevOps

1. Восстановить код до состояния, когда все тесты проходят успешно
2. Сделать git push изменений в свой репозиторий на GitHub
3. Настроить интеграцию с Azure DevOps
    1. Зайти на [сайт](https://dev.azure.com) Azure DevOps. Зайти под студенческим аккаунтом.
    2. Создать проект со своим именем (можно оставить дефолтные настройки). Проект сделать публичным.
       ![img.png](azureDevOpsNewProj.png)
    3. Добавить аккаунт преподавателя в свой проект
       ![img.png](invite.png)\   
       ![img_1.png](img_1.png)
    4. Если публичный проект создать по умолчанию не получается, необходимо зайти в настройки организиации и подключить эту функцию
    ![img_38.png](img_38.png)
       поставить следующие настройки
       ![img_39.png](img_39.png)
   5. также убедится, что во вкладке parralel job доступен бесплатный пакет
    ![img_40.png](img_40.png)
      Если не доступен (не как на скриншоте), необходимо либо запросить пакет по [ссылке](https://aka.ms/azpipelines-parallelism-request). Укажите, что приватные репозитории используете. В течение 2-3 дней дадут ответ.
      Если не получится получить такой доступ, то преподаватель добавит вас в свою организацию. Количество мест ограничено, поэтому буду добавлять по 5 человек.
3. Создать CI pipeline
    1. Перейти во вкладку Pipelines
       ![img.png](img.png)
    2. Нажать кнопку create Pipeline
    3. Выбрать GitHub как источник кода (при этом нужно залогинится в свой аккаунт)
       ![img_2.png](img_2.png)
    4. Выбрать репозитори PipelinePractice
       ![img_3.png](img_3.png)
    5. В yaml файл (манифест) вставить следующий код:
    ```yaml
    # Python package
    # Create and test a Python package on multiple Python versions.
    # Add steps that analyze code, save the dist with the build record, publish to a PyPI-compatible index, and more:
    # https://docs.microsoft.com/azure/devops/pipelines/languages/python
    
    trigger: # в данном блоке определяется, при каком событии запускать пайплайн
    - master # запускаем, как только пришел новый коммит в ветку master
    
    pool: # здесь определяем образ докера, в котором запускается приложение и версию интерпритатора
      vmImage: ubuntu-latest # выбираем ubuntu
    strategy: # здесь выбираем стек программирования
      matrix: # matrix позволяет запускать параллельные конвейеры, если требуются разные версии
    #    Python36: # пока отключаем запуск на 3.6
    #      python.version: '3.6'
        Python37: # запускаем на 3.7
          python.version: '3.7'
    
    steps: # здесь указываются шаги конвейера
    - task: UsePythonVersion@0 # используем версию питона
      inputs:
        versionSpec: '$(python.version)'
      displayName: 'Use Python $(python.version)'
    
    - script: | # запускаем апдейт питона, устанавливаем зависимости (в нашем случае flask)
        python -m pip install --upgrade pip
        pip install -r requirements.txt
      displayName: 'Install dependencies' # здесь отображается название текущей задачи
    
    - script: | # запускаем юнит тесты (без функциональных)
        pip install pytest 
        pytest tests/unit_tests && pip install pycmd && py.cleanup tests/
      displayName: 'pytest'
    
    - task: ArchiveFiles@2 # архивируем наш проект чтобы опубликовать артефакт. Артефакт это по сути то, что отдает клиенту (например архив с программой)
      displayName: 'Archive application'
      inputs:
        rootFolderOrFile: '$(System.DefaultWorkingDirectory)/'
        includeRootFolder: false
        archiveFile: '$(Build.ArtifactStagingDirectory)/$(Build.BuildId).zip'
    
    - task: PublishBuildArtifacts@1 # публикуем артефакт как результат нашего пайплайна
      displayName: 'Publish Artifact: drop'
    
   ```
    6. Нажимаем Run. Переходим в пайплайн. Убеждаемся, что все stages выполнены
       ![img_4.png](img_4.png)
    7. Должен быть опубликован артефакт
       ![img_5.png](img_5.png)
       Название артефакта - версия
       ![img_6.png](img_6.png)

    8. В readme добавить status badge
       ![img_7.png](img_7.png)

## Pipeline - continuous deployment (CD) with Azure DevOps

1. Восстановить код до состояния, когда все тесты проходят успешно
2. Запросить у преподавателя создание ресурсной группы в Azure
3. Создать Web App в Azure
    1. Войти в Azure с помощью своего университетского аккаунта
    2. Убедиться, что вам доступны ресурсы
    3. Создать новый ресурс
       ![img_8.png](img_8.png)
    4. Выбрать create web app
       ![img_9.png](img_9.png)
    5. Выбрать следующие характеристики
       ![img_10.png](img_10.png)
       ![img_11.png](img_11.png)
    6. Создать Web App
4. Настроить CD pipeline
    1. В Azure DevOps создать Release
       ![img_12.png](img_12.png)
    2. В артефакты добавить результат pipeline из CI конвейра
       ![img_13.png](img_13.png)
       ![img_14.png](img_14.png)
    3. Выставить тригер на запуск после CI пайплайна
       ![img_15.png](img_15.png)
    4. Добавить Stage. Выбрать python app. Stage назвать deploy
       ![img_16.png](img_16.png)
    5. Удалить все stages. Добавить Azure App Service Deploy
       ![img_21.png](img_21.png)
    6. Сконфигурировать настройки сервиса в Azure
       ![img_22.png](img_22.png)
    ```shell
    gunicorn --bind=0.0.0.0 --timeout 600 app:app # команда вызова python app.py через шлюз gunicorn
    ```
   про gunicorn подробнее [здесь](https://docs.microsoft.com/en-us/azure/app-service/configure-language-python) - в
   поиске ищите gunicorn
    7. Убедиться, что агент запускается на Windows
       ![img_23.png](img_23.png)
    8. Нажать Create release
       ![img_24.png](img_24.png)
       ![img_25.png](img_25.png)
    9. Перейти на вкладку Release и нажать deploy
       ![img_26.png](img_26.png)
    10. Убедится, что все таски завершены
        ![img_27.png](img_27.png)
        11. Перейти на сайт по url, который задавали в Web App, должно отобразится hello-word
4. В CD pipeline настроить функциональное тестирование
    1. В Azure DevOps отредактировать Release. Добавить новый Stage. Назвать его test
       ![img_29.png](img_29.png)
    2. Назначить его после stage с deploy
       ![img_28.png](img_28.png)
       ![img_30.png](img_30.png)
    3. Добавить следующие шаги:
       ![img_31.png](img_31.png)
       4.Сконфигурировать следующим образом Разархивируем приложение (артефакт)
       ![img_32.png](img_32.png)

   ![img_33.png](img_33.png)
   Что происходит в коде?
    ```shell
      pip install selenium pytest# устанавливаем selenium и pytest
      echo $(ChromeWebDriver) # убеждаемся, что установлен ChromeWebDriver. Он есть только в версиях agent Windows
      pytest Agent.HomeDirectory/tests/functional_tests --url <url вашего сайта>  --junitxml=TestResults/test-results.xml # запускаем тесты. экспортируем отчет
    ```
   Не забываем в pytest вставить --url вашего сайта!
   Публикуем тесты в Azure DevOps
   ![img_34.png](img_34.png)
    5. Создать Release. Проверить, что тесты выполнились
       ![img_35.png](img_35.png)
    6. В вкладке Test Plans должны отобразится результаты
       ![img_36.png](img_36.png)
       ![img_37.png](img_37.png)

[Статья пример](https://www.azuredevopslabs.com/labs/vstsextend/python/)