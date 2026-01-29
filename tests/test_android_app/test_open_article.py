import allure

from wiki_mobile.screens.onboarding_screen import OnboardingScreen
from wiki_mobile.screens.main_screen import MainScreen
from wiki_mobile.screens.search_screen import SearchScreen
from wiki_mobile.screens.article_screen import ArticleScreen


@allure.title("Wikipedia: открыть статью из результатов поиска")
@allure.tag("mobile", "wikipedia", "article")
def test_open_article_from_search():
    OnboardingScreen().pass_if_present()
    MainScreen().should_be_opened().open_search()

    SearchScreen().type_query("Python").results_should_be_visible().open_first_result()
    ArticleScreen().should_be_opened()
