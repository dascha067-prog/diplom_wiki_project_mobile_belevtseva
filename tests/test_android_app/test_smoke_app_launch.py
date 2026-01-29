import allure

from wiki_mobile.screens.onboarding_screen import OnboardingScreen
from wiki_mobile.screens.main_screen import MainScreen


@allure.title("Wikipedia: приложение запускается и открывается главный экран")
@allure.tag("mobile", "wikipedia", "smoke")
def test_wikipedia_app_launch_smoke():
    OnboardingScreen().pass_if_present()
    MainScreen().should_be_opened()
