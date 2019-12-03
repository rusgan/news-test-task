from screens.base_screen import BaseScreen


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

    def get_articles(self):
        elements = self.get_elements(self.article_locator)
        articles = []
        for element in elements:
            article = Article()
            article.title = element.find_element_by_id(self.title_id)
            article.image = element.find_element_by_id(self.image_id).screenshot_as_base64
            article.description = element.find_element_by_id(self.description_id).text
            article.element = element
            articles.append(article)
        return articles


class Article:
    element = None
    title = None
    image = None
    description = None


