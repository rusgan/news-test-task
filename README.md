News test task
====================
# Tools
1. [Appium](http://appium.io/) requires Node.js
    ```shell
    npm install -g appium
    ```
2. Для проверки конфигурации [appium-doctor](https://github.com/appium/appium-doctor)
    ```shell
    npm install appium-doctor -g
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