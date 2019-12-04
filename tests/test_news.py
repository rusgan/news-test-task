import pytest

from screens.main import Main


def assert_articles(article, refreshed):
    assert article.title == refreshed.title
    assert article.description == refreshed.description
    assert article.image == refreshed.image


TITLE_HEIGHT = 99
IMAGE_HEIGHT = 275
DESCRIPTION_HEIGHT = 77


class TestNews:
    @pytest.mark.cache
    @pytest.mark.positive
    def test_caching(self):
        main = Main(pytest.driver)
        articles = main.get_articles()
        main.toggle_wifi()
        main.start_main_activity()
        offline = main.get_articles()
        for index, item in enumerate(articles):
            assert_articles(articles[index], offline[index])

    @pytest.mark.filter
    @pytest.mark.positive
    @pytest.mark.xfail(reason='Work like search instead of filtering. Also need inject mocks or db to control backend '
                              'part')
    def test_filter(self):
        main = Main(pytest.driver)
        articles = main.get_articles()
        words = ' '.join(articles[0].title.split()[:3])
        main.filter(words)
        main.wait_until_stale(articles[-1].element)
        filtered_articles = main.get_articles()
        assert len(filtered_articles) == 1
        assert_articles(articles[0], filtered_articles[0])

    @pytest.mark.positive
    @pytest.mark.article_size
    def test_article_size(self):
        main = Main(pytest.driver)
        articles_elements = main.get_article_elements()
        for article in articles_elements:
            assert article.title.size['height'] == TITLE_HEIGHT
            assert article.image.size['height'] == IMAGE_HEIGHT
            assert article.description.size['height'] == DESCRIPTION_HEIGHT
