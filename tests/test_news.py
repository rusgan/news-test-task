import string
from time import sleep

import pytest

from screens.main import Main
from utils import helpers


def assert_articles(article, refreshed):
    assert article.title_text == refreshed.title_text
    assert article.description_text == refreshed.description_text
    assert article.image_screenshot == refreshed.image_screenshot


# TODO add function to get sizes for screens
# TITLE_HEIGHT
# IMAGE_HEIGHT
# DESCRIPTION_HEIGHT
TIMEOUT = 3


class TestNews:
    @pytest.mark.cache
    @pytest.mark.positive
    def test_caching(self):
        main = Main(pytest.driver)
        articles = main.get_all_articles()
        main.toggle_wifi()
        main.start_main_activity()
        offline = main.get_all_articles()
        for index, item in enumerate(articles):
            assert_articles(articles[index], offline[index])

    @pytest.mark.filter
    @pytest.mark.positive
    @pytest.mark.xfail(reason='Work like search instead of filtering. Also need inject mocks or db to control backend '
                              'part')
    def test_filter(self):
        main = Main(pytest.driver)
        articles = main.get_current_articles()
        words = ' '.join(articles[0].title_text.split()[:3])
        main.filter(words)
        # TODO figure out how to wait till stale elements in multiple filter results
        sleep(TIMEOUT)
        # main.wait_until_stale(articles[-1].article_element)
        filtered_articles = main.get_current_articles()
        assert_articles(articles[0], filtered_articles[0])

    @pytest.mark.positive
    @pytest.mark.filter_input
    @pytest.mark.parametrize("input", [string.printable, helpers.printable])
    def test_filter_input(self, input):
        main = Main(pytest.driver)
        main.filter(input)
        search_field = main.get_search_text()
        assert search_field == input

    @pytest.mark.negative
    @pytest.mark.negative_input
    @pytest.mark.parametrize("input", [' ', ' \n'])
    def test_filter_input_negative(self, input):
        main = Main(pytest.driver)
        articles = main.get_current_articles()
        main.filter(input)
        sleep(TIMEOUT)
        after_filter = main.get_current_articles()
        for index, item in enumerate(articles):
            assert_articles(articles[index], after_filter[index])

    @pytest.mark.positive
    @pytest.mark.article_size
    @pytest.mark.skip(reason="Need to add scale for sizes. And check requirements.")
    def test_article_size(self):
        main = Main(pytest.driver)
        articles_elements = main.get_current_articles()
        for article in articles_elements:
            assert article.title_element.size['height'] == TITLE_HEIGHT
            assert article.image_element.size['height'] == IMAGE_HEIGHT
            assert article.description.size['height'] == DESCRIPTION_HEIGHT

    @pytest.mark.positive
    @pytest.mark.article_content
    @pytest.mark.skip(reason="Need to control backend or db to get content. Or add request to get articles"
                             "https://newsapi.org/v2/top-headlines?country=ru")
    def test_article_content(self):
        pass