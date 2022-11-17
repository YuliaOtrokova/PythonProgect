from .base_page import BasePage
from .locators import MainPagelocators


class MainPage(BasePage):

    def should_be_link_to_product_page(self):
        assert self.element_is_present(*MainPagelocators.LINK_TO_PRODUCT_PAGE)

    def go_to_product_page(self):
        self.browser.find_element(*MainPagelocators.LINK_TO_PRODUCT_PAGE).click()

    def go_to_login_page(self):
        self.browser.find_element(*MainPagelocators.LOGIN_BTN).click()
