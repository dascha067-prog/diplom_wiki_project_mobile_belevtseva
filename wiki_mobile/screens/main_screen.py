import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be


class MainScreen:
    SEARCH_CONTAINER = (AppiumBy.ID, "org.wikipedia.alpha:id/search_container")
    SEARCH_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")

    @allure.step("Проверить, что открыт главный экран")
    def should_be_opened(self):
        browser.element(self.SEARCH_CONTAINER).should(be.visible)
        return self

    @allure.step("Открыть поиск")
    def open_search(self):
        browser.element(self.SEARCH_BUTTON).should(be.visible).click()
        return self
