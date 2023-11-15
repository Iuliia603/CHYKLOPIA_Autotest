from CHYKALOPIA.Wrapper_Chyka.Header import Header
from CHYKALOPIA.Wrapper_Chyka.Home_Page import HomePage
from CHYKALOPIA.Wrapper_Chyka.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class CallUSPage:
    def __init__(self, browser):
        self.header = Header(browser)
        self.homepage = HomePage(browser)

        self.call_us_title = Element(browser, By.XPATH, '//*[@id="content"]/div/div[1]/section[1]/div[2]/div[1]/div/section/div[2]/div[1]/div/div[1]/div/h1')

    def get_call_us_title(self):
        return self.call_us_title.get_text()