from CHYKALOPIA.Wrapper_Chyka.UIElement import UIElement as Element
from selenium.webdriver.common.by import By
import time


class Calendar:
    def __init__(self, browser):
        self.browser = browser
        self.calendar_title = Element(browser, By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/h2')
        self.time_3_45 = Element(browser, By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/button')
        self.time_3_30 = Element(browser, By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/button')
        self.next_btn = Element(browser, By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[1]/button[2]')
        self.iframe = Element(browser, By.TAG_NAME, 'iframe')
        self.time_11 = Element(browser, By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[1]/button')
        self.information_about_call = Element(browser, By.XPATH, '//*[@id="root"]/div/div/div/div[1]/div/div/div[1]/div[2]/div/div/div/div/div[3]/div/div[3]')

    def switch_to_calendar_frame(self):
        time.sleep(10)
        self.browser.get_driver().switch_to.frame(self.iframe.get_element())

    def switch_back_from_calendar_frame(self):
        self.browser.get_driver().switch_to.default_content()

    def get_calendar_title(self):
        return self.calendar_title.get_text()

    def select_the_date(self, date_to_select):
        self.date_12 = Element(self.browser, By.XPATH, '//button[contains(@aria-label, "{}")]'.format(date_to_select))
        self.date_12.click()

    def select_time_3_45(self):
        self.time_3_45.click()

    def select_time_3_30(self):
        self.time_3_30.click()

    def select_time_11(self):
        self.time_11.click()

    def click_next_btn(self):
        self.next_btn.click()

    def get_information_about_call(self):
        return self.information_about_call.get_text()

