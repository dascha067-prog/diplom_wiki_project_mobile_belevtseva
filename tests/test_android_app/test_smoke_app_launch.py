import allure
from selene import browser, be


@allure.title("Wikipedia: приложение запускается (onboarding или главный экран)")
@allure.tag("mobile", "wikipedia", "smoke")
def test_wikipedia_app_launch_smoke():
    with allure.step("Определить, какой экран открыт: onboarding или главный"):

        skip_btn = browser.element(("id", "org.wikipedia.alpha:id/fragment_onboarding_skip_button"))
        continue_btn = browser.element(("id", "org.wikipedia.alpha:id/fragment_onboarding_forward_button"))
        done_btn = browser.element(("id", "org.wikipedia.alpha:id/fragment_onboarding_done_button"))
        onboarding_title = browser.element(("id", "org.wikipedia.alpha:id/primaryTextView"))

        search_container = browser.element(("id", "org.wikipedia.alpha:id/search_container"))

    with allure.step("Проверить, что видим главный экран или onboarding"):
        if search_container.matching(be.visible):
            with allure.step("Показан главный экран: отображается поле поиска"):
                search_container.should(be.visible)

        elif skip_btn.matching(be.visible):
            with allure.step("Показан onboarding: отображается кнопка Skip"):
                skip_btn.should(be.visible)

        elif continue_btn.matching(be.visible):
            with allure.step("Показан onboarding: отображается кнопка Continue"):
                continue_btn.should(be.visible)

        elif done_btn.matching(be.visible):
            with allure.step("Показан onboarding: отображается кнопка Done"):
                done_btn.should(be.visible)

        else:
            with allure.step("Запасная проверка: отображается заголовок onboarding"):
                onboarding_title.should(be.visible)
