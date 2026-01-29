import allure

from wiki_mobile.screens.onboarding_screen import OnboardingScreen
from wiki_mobile.screens.main_screen import MainScreen
from wiki_mobile.screens.search_screen import SearchScreen


@allure.title("Wikipedia: поиск статьи и отображение результатов")
@allure.tag("mobile", "wikipedia", "search")
def test_search():
    OnboardingScreen().pass_if_present()
    MainScreen().should_be_opened().open_search()

    SearchScreen() \
        .type_query("Appium") \
        .results_should_be_visible() \
        .first_result_should_contain("Appium")
