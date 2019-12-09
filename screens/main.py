from selenium.common.exceptions import NoSuchElementException

from screens.base_screen import BaseScreen

PACKAGE = 'my.deler.newstestapplication'
MAIN_ACTIVITY = PACKAGE + '.screens.MainActivity'
PAGE_SIZE = 20


class Main(BaseScreen):
    filter_locator = ('id', 'my.deler.newstestapplication:id/searchEdit')
    article_locator = ('id', 'my.deler.newstestapplication:id/cardView')
    title_id = 'my.deler.newstestapplication:id/titleText'
    image_id = 'my.deler.newstestapplication:id/iconImage'
    description_id = 'my.deler.newstestapplication:id/descriptionText'

    def get_search_text(self):
        return self.get_text(self.filter_locator)

    def filter(self, value):
        return self.send_keys(self.filter_locator, value)

    def get_current_articles(self):
        return self._sort_articles(self.get_elements(self.article_locator))

    def get_all_articles(self):
        articles = []
        while True:
            self._sort_articles(self.get_elements(self.article_locator), articles)
            self.scroll_down()
            refreshed = self._sort_articles(self.get_elements(self.article_locator))
            if refreshed[-1].description_text == articles[-1].description_text or len(articles) > PAGE_SIZE:
                return articles

    def start_main_activity(self):
        self.driver.start_activity(PACKAGE, MAIN_ACTIVITY)

    def get_article_by_text(self, text):
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance('
                                                        '0)).getChildByText(new UiSelector().className('
                                                        '"android.widget.TextView"), "%s")' % text)

    # TODO optimize or remake to UiScrollable
    def _sort_articles(self, article_elements, articles=None):
        if articles is None:
            articles = []
        for element in article_elements:
            article = Article()
            try:
                article.title_element = element.find_element_by_id(self.title_id)
                article.title_text = article.title_element.text
                article.image_element = element.find_element_by_id(self.image_id)
                article.image_element = article.image_element.screenshot_as_base64
                article.description_element = element.find_element_by_id(self.description_id)
                article.description_text = article.description_element.text
                article.article_element = element
            except NoSuchElementException:
                article = None
            if article is not None and self._filter(article, articles):
                articles.append(article)
        return articles

    def _filter(self, article, articles):
        for art in articles:
            if art.description_text == article.description_text:
                return False
        return True


class Article:
    article_element = None
    title_element = None
    title_text = None
    image_element = None
    image_screenshot = None
    description_element = None
    description_text = None
