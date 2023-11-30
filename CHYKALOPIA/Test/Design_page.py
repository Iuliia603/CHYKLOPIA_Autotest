from CHYKALOPIA.Wrapper_Chyka.Header import Header
from CHYKALOPIA.Wrapper_Chyka.Home_Page import HomePage
from CHYKALOPIA.Wrapper_Chyka.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class UIUXPage:
    def __init__(self, browser):
        self.browser = browser
        self.header = Header(browser)
        self.homepage = HomePage(browser)

        self.ui_ux_title = Element(browser, By.XPATH,'//*[@id="content"]/div/div[1]/section[1]/div[2]/div[1]/div/div[2]/div/h2')
        self.questions_title = Element(browser, By.XPATH, '//*[@id="content"]/div/div[1]/section[13]/div[2]/div[1]/div/div/div/h4')

        self.ux_for_website_que = Element(browser, By.XPATH, '//*[@id="elementor-tab-title-1411"]/a')
        self.prepare_ux_que = Element(browser, By.XPATH, '//*[@id="elementor-tab-title-1412"]/a')
        self.need_ux_strategy_que = Element(browser, By.XPATH, '//*[@id="content"]/div/div[1]/section[13]/div[2]/div[2]/div/div/div/div/div[3]')
        self.investment_price_range_que = Element(browser, By.XPATH, '//*[@id="content"]/div/div[1]/section[13]/div[2]/div[2]/div/div/div/div/div[4]')
        self.how_long_ux_que = Element(browser, By.XPATH, '//*[@id="content"]/div/div[1]/section[13]/div[2]/div[2]/div/div/div/div/div[5]')

        self.ux_for_website_text = Element(browser, By.XPATH, '//*[@id="elementor-tab-content-1411"]')
        self.prepare_ux_text = Element(browser, By.XPATH, '//*[@id="elementor-tab-content-1412"]')
        self.need_ux_strategy_text = Element(browser, By.XPATH,'//*[@id="elementor-tab-content-1413"]')
        self.investment_price_range_text = Element(browser, By.XPATH,'//*[@id="elementor-tab-content-1414"]')
        self.how_long_ux_text = Element(browser, By.XPATH, '//*[@id="elementor-tab-content-1415"]')
        self.get_a_call_title = Element(browser, By.XPATH, '//*[@id="content"]/div/div[1]/section[12]/div[2]/div[1]/div/div/div/div/a[1]')

    def get_ui_ux_title(self):
        return self.ui_ux_title.get_text()

    def get_questions_title(self):
        return self.questions_title.get_text()

    def scroll_to_questions_title(self):
        questions_title_element = self.get_a_call_title.get_element()
        self.browser.execute_script("arguments[0].scrollIntoView();", questions_title_element)

    def click_ux_for_website_que(self):
        self.ux_for_website_que.click()

    def click_prepare_ux_que(self):
        self.prepare_ux_que.click()

    def click_need_ux_strategy_que(self):
        self.need_ux_strategy_que.click()

    def click_investment_price_range_que(self):
        self.investment_price_range_que.click()

    def click_how_long_ux_que(self):
        self.how_long_ux_que.click()

    def get_ux_for_website_text(self):
        return self.ux_for_website_que.get_text()

    def get_prepare_ux_text(self):
        return self.prepare_ux_text.get_text()

    def get_need_ux_strategy_text(self):
        return self.need_ux_strategy_text.get_text()

    def get_investment_price_range_text(self):
        return self.investment_price_range_text.get_text()

    def get_how_long_ux_text(self):
        return self.how_long_ux_text.get_text()

    # def is_answer_visible(self, question_element):
    #     answer_element = question_element.get_element()
    #     return answer_element.is_displayed()








