from CHYKALOPIA.Wrapper_Chyka.UIElement import UIElement as Element
from selenium.webdriver.common.by import By
from CHYKALOPIA.Wrapper_Chyka.Actions import Actions


class Header:
    def __init__(self, browser):
        self.actions = Actions(browser)

        self.logo = Element(browser, By.XPATH, "/html/body/div[1]/section[1]/div[2]/div[1]/div/div/div/a/img")
        self.get_call_btn = Element(browser, By.XPATH, "/html/body/div[1]/section[1]/div[2]/div[2]/div/div[1]/div/div/a")
        self.capabilities_btn = Element(browser, By.XPATH, '//*[@id="jet-menu-item-16364"]/a/div/div')
        self.brand_strategy_section = Element(browser, By.ID, "branding")
        self.ui_ux_design_section = Element(browser, By.ID, "uiux")
        self.web_solutions_section = Element(browser, By.ID, "webside")
        self.data_visual_design_section = Element(browser, By.ID, "datavisual")
        self.growth_support_btn = Element(browser, By.NAME, "Growth Support")
        self.work_btn = Element(browser, By.XPATH, '//*[@id="jet-menu-item-18172"]/a/div/div')
        self.clients_bnt = Element(browser, By.NAME, "Clients")
        self.why_us_btn = Element(browser, By.NAME, "Why US?")
        self.book_btn = Element(browser, By.NAME, "Book")
        self.resources_btn = Element(browser, By.NAME, "Resources")

    def verify_logo_is_visible(self):
        return self.logo.wait_until_visible()

    def click_logo(self):
        self.verify_logo_is_visible()
        self.logo.click()

    def open_get_call_page(self):
        self.get_call_btn.click()

    def open_capabilities_page(self):
        self.capabilities_btn.click()

    def show_all_capabilities(self):
        self.actions.move_to_element(self.capabilities_btn)

    def open_growth_support_page(self):
        self.growth_support_btn.click()

    def open_work_page(self):
        self.work_btn.click()

    def open_clients_page(self):
        self.clients_bnt.click()

    def open_why_us_page(self):
        self.why_us_btn.click()

    def open_book_page(self):
        self.book_btn.click()

    def open_resources(self):
        self.resources_btn.click()

    def select_brand_strategy_section(self):
#        self.show_all_capabilities()
        self.brand_strategy_section.click()

    def select_ui_ux_design_section(self):
        self.show_all_capabilities()
        self.ui_ux_design_section.click()

    def select_web_solutions_section(self):
        self.show_all_capabilities()
        self.web_solutions_section.click()

    def select_data_visual_design_section(self):
        self.show_all_capabilities()
        self.data_visual_design_section.click()

