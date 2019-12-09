News test task
====================

# Tools
Для автоматизации был выбран фреймворк Appium, но я бы рекомедовал для автоматизации использвать нативные инструменты.
Но если если по каким-то причинам, такой возмодности нет, то предложил бы выбрать изменить стек на java, поскольку Python библотека
для работы с Appium не столь удобна.

1. [Appium](http://appium.io/) requires Node.js

    Установка

    ```shell
    npm install -g appium
    ```

    Запуск
    ```shell
    appium
    ```

2. Для проверки конфигурации [appium-doctor](https://github.com/appium/appium-doctor)

    Установка

    ```shell
    npm install appium-doctor -g
    ```

    Проверка компонент

    ```shell
    appium-doctor --android
    ```
# Libraries
Необходимые библиотеки находятся в requirements.txt

    ```shell
    pip install -r requirements.txt
    ```
# Usage
 Настройки драйвера и capabilities вынесена в фикстуру driver_setup
```python
@pytest.fixture(scope="session", autouse=True)
def driver_setup(request):
    capabilities = {
        'platformName': 'Android',
        'deviceName': 'pixel3',
        'app': PATH('app/news.apk'),
        'avd': 'pixel3'
    }
    url = 'http://localhost:4723/wd/hub'
    driver = webdriver.Remote(url, capabilities)
```
Запуск по маркеру
    ```shell
    pytest -m "%marker_name%"
    ```
# Cases
Чек-листы находятся в файле /documents/checklists

Кейсы автоматизации отбирались по критериям:
1. Покрыть требования
2. Возможность автоматизации
3. Влияние на скоращение рутинных прроверок