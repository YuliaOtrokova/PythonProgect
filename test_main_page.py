import pytest
import time
from pages.main_page import MainPage
from pythonProject.pages.login_page import LoginPage

link = 'https://selenium1py.pythonanywhere.com/ru/'

# class TestMainPage():

    # def setup(self):
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #     не надо если есть фикстуры
    # @pytest.mark.open_page
    # @pytest.mark.smoke
@pytest.mark.smoke
def test_quest_can_go_to_catalogue(browser):
    # browser.get(link)
    page = MainPage(browser, link)
    page.open_page()
    page.should_be_link_to_product_page()
    page.go_to_product_page()
    time.sleep(5)

    # @pytest.mark.view_products #@pytest.mark.xfail
# def test_2(browser):
#     browser.get(link)
#     time.sleep(5)

    # def teardown(self):
    #     self.driver.quit()
#     не нужно при фикстурах
@pytest.mark.regression
def test_quest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open_page()
    page.go_to_login_page()
    time.sleep(2)
    page = LoginPage(browser, link)
    page.should_be_login_page()

def test_user_сan_autorize(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    page = LoginPage(browser, link)
    page.open_page()
    page.register_user(email=str(time.time()) + '@mail.org', password='QAZ123edc!')
    page.should_be_autorized_user()