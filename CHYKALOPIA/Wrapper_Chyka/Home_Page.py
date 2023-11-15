from CHYKALOPIA.Wrapper_Chyka.Browser import Browser
from CHYKALOPIA.Wrapper_Chyka.Header import Header
from CHYKALOPIA.Wrapper_Chyka.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, browser):
        self.header = Header(browser)

        self.homepage_title = Element(browser, By.XPATH, '//*[@id="content"]/div/div[1]/section[1]/div[2]/div[1]/div/div[1]/div/p')

    def get_homepage_title(self):
        return self.homepage_title.get_text()

    def open_capabilities_page(self):
        self.header.open_capabilities_page()

    def show_all_capabilities(self):
        self.header.show_all_capabilities()

    def open_growth_support_page(self):
        self.header.open_growth_support_page()

    def open_work_page(self):
        self.header.open_work_page()

    def open_clients_page(self):
        self.header.open_clients_page()

    def open_why_us_page(self):
        self.header.open_why_us_page()

    def open_book_page(self):
        self.header.open_book_page()

    def open_resources(self):
        self.header.open_resources()

    def select_brand_strategy_section(self):
        self.header.brand_strategy_section()

    def select_ui_ux_design_section(self):
        self.header.ui_ux_design_section()

    def select_web_solutions_section(self):
        self.header.web_solutions_section()

    def select_data_visual_design_section(self):
        self.header.select_data_visual_design_section()

