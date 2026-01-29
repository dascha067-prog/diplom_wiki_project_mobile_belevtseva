import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be


class OnboardingScreen:
    SKIP = (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")
    CONTINUE = (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")
    DONE = (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_done_button")
    TITLE = (AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")

    @allure.step("Пройти онбординг (если он показан)")
    def pass_if_present(self):
        if browser.element(self.SKIP).matching(be.visible):
            browser.element(self.SKIP).click()
            return self
        if browser.element(self.CONTINUE).matching(be.visible):
            for _ in range(5):
                if browser.element(self.DONE).matching(be.visible):
                    browser.element(self.DONE).click()
                    return self
                if browser.element(self.CONTINUE).matching(be.visible):
                    browser.element(self.CONTINUE).click()
                else:
                    break
            return self
        if browser.element(self.DONE).matching(be.visible):
            browser.element(self.DONE).click()
            return self
        return self
