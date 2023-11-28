from CHYKALOPIA.Wrapper_Chyka.UIElement import UIElement as Element
from selenium.webdriver.common.by import By
from CHYKALOPIA.Wrapper_Chyka.Browser import Browser
import time

class Calendar:
    def __init__(self, browser):
        self.browser = Browser
        self.calendar_title = Element(browser, By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/h2')
        self.time_3_45 = Element(browser, By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/button')
        self.time_3_30 = Element(browser, By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/button')
        self.next_btn = Element(browser, By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/button[2]')
        self.iframe = Element(browser, By.XPATH, '//*[@id="get-started"]/div/div/iframe')

    def switch_to_calendar_frame(self):
        self.driver.get_driver(self).switch_to.frame(self.iframe.get_element())
        time.sleep(10)

    def switch_back_from_calendar_frame(self):
        self.browser.get_driver().switch_to.default_content()

    def get_calendar_title(self):
        return self.calendar_title.get_text()

    def select_the_date(self, date_to_select):
        self.date = Element(self.browser, By.XPATH, '//button[contains(@aria-label, "{}")]'.format(date_to_select))
        self.date.click()

    def select_time_3_45(self):
        self.time_3_45.click()

    def select_time_3_30(self):
        self.time_3_30.click()

    def click_next_btn(self):
        self.next_btn.click()

