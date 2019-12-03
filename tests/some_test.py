import random
from time import sleep

from screens.main import Main


#@pytest.mark.usefixtures('driver_setup')
class TestSomething:
    def test_cashing(self, driver_setup):
        driver = driver_setup
        main = Main(driver)
        articles = main.get_articles()
        main.toggle_wifi()
        main.close_app()
        main.launch_app()
        offline = main.get_articles()
        for index, item in enumerate(articles):
            assert articles[index].title == offline[index].title
            assert articles[index].description == offline[index].description

    def test_filter(self, driver_setup):
        driver = driver_setup
        main = Main(driver)
        articles = main.get_articles()
        words = ' '.join(articles[0].title.split()[:3])
        main.filter(words)
        #main.wait_until_stale(articles[0].element)
        sleep(5)    #avoid with WebDriverWait
        filtered_articles = main.get_articles()
        assert articles[0].title == filtered_articles[0].title
        assert articles[0].description == filtered_articles[0].description
        assert articles[0].image == filtered_articles[0].image
