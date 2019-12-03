import pytest

from screens.main import Main


def assert_articles(article, refreshed):
    print('first: ' + article.description.text)
    print('second: ' + refreshed.description.text)
    assert article.title.text == refreshed.title.text
    assert article.description.text == refreshed.description.text
    assert article.image.screenshot_as_base64 == refreshed.image.screenshot_as_base64


TITLE_HEIGHT = 2


class TestSomething:
    @pytest.mark.cash
    @pytest.mark.positive
    def test_cashing(self, driver_setup):
        driver = driver_setup
        main = Main(driver)
        articles = main.get_articles()
        main.toggle_wifi()
        main.close_app()
        main.launch_app()
        offline = main.get_articles()
        for index, item in enumerate(articles):
            assert_articles(articles[index], offline[index])

    @pytest.mark.filter
    @pytest.mark.positive
    @pytest.mark.xfail(reason='Problems with WebDriverWait')
    def test_filter(self, driver_setup):
        driver = driver_setup
        main = Main(driver)
        articles = main.get_articles()
        words = ' '.join(articles[0].title.text.split()[:3])
        main.filter(words)
        main.wait_until_stale(articles[-1].element)
        filtered_articles = main.get_articles()
        assert len(filtered_articles) == 1
        assert_articles(articles[0], filtered_articles[0])

    @pytest.mark.positive
    @pytest.mark.article_size
    def test_article_size(self, driver_setup):
        driver = driver_setup
        main = Main(driver)
        articles = main.get_articles()
        for article in articles:
            assert article.title.size['height'] == TITLE_HEIGHT
            assert article.image.size['height'] == 2
            assert article.description.size['height'] == 2
