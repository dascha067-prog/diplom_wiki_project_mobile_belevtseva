import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be


class ArticleScreen:
    CANDIDATES = [
        (AppiumBy.ACCESSIBILITY_ID, "Navigate up"),
        (AppiumBy.ID, "org.wikipedia.alpha:id/toolbar"),
        (AppiumBy.ID, "org.wikipedia.alpha:id/view_page_title_text"),
        (AppiumBy.ID, "org.wikipedia.alpha:id/page_web_view"),
    ]

    @allure.step("Проверить, что открылась статья")
    def should_be_opened(self):
        for locator in self.CANDIDATES:
            if browser.element(locator).matching(be.visible):
                return self

        raise AssertionError(
            "Статья не открылась: ни один из ожидаемых элементов ArticleScreen не найден."
        )
