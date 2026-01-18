import allure
from selene import browser


@allure.title("Wikipedia: открыть статью из результатов поиска")
@allure.tag("mobile", "wikipedia")
def test_open_article_from_search():
    with allure.step("Открыть поиск"):
        browser.element('//*[@text="Search Wikipedia"]').click()

    with allure.step("Ввести запрос поиска"):
        browser.element('//*[@resource-id="org.wikipedia.alpha:id/search_src_text"]').type("Python")

    with allure.step("Открыть первый результат поиска"):
        browser.element('//*[@resource-id="org.wikipedia.alpha:id/page_list_item_container"]').click()
