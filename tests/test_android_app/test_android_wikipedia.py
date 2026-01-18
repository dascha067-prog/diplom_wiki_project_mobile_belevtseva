import allure
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


@allure.title("Wikipedia: поиск статьи и отображение результатов")
@allure.tag("mobile", "wikipedia", "search")
def test_search():
    with step("Открыть поиск"):
        browser.element(
            (AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")
        ).click()

    with step("Ввести поисковый запрос"):
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")
        ).type("Appium")

    with step("Проверить, что результаты поиска отображаются"):
        results = browser.all(
            (AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")
        )

        results.should(have.size_greater_than(0))

    with step("Проверить, что первый результат содержит искомый текст"):
        results.first.should(have.text("Appium"))
