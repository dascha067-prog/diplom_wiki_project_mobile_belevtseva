import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be, have


class SearchScreen:
    SEARCH_INPUT = (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")
    RESULT_TITLES = (AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")

    @allure.step("Ввести поисковый запрос: {query}")
    def type_query(self, query: str):
        browser.element(self.SEARCH_INPUT).should(be.visible).type(query)
        return self

    @allure.step("Проверить, что результаты поиска отображаются")
    def results_should_be_visible(self):
        browser.all(self.RESULT_TITLES).should(have.size_greater_than(0))
        return self

    @allure.step("Открыть первый результат поиска")
    def open_first_result(self):
        browser.all(self.RESULT_TITLES).first.should(be.visible).click()
        return self

    @allure.step("Проверить, что первый результат содержит текст: {text}")
    def first_result_should_contain(self, text: str):
        browser.all(self.RESULT_TITLES).first.should(have.text(text))
        return self
