from behave import given, when, then
from CHYKALOPIA.Wrapper_Chyka.Browser import Browser
from CHYKALOPIA.Wrapper_Chyka.Header import Header
from CHYKALOPIA.Wrapper_Chyka.Home_Page import HomePage
from CHYKALOPIA.Wrapper_Chyka.CapabilityPage import CapabilityPage
from CHYKALOPIA.Wrapper_Chyka.Brand_Strategy_page import BrandStrategyPage
from CHYKALOPIA.Wrapper_Chyka.Work_Page import WorkPage
from CHYKALOPIA.Wrapper_Chyka.Call_us_Page import CallUSPage
from config.config_reader import ConfigReader
import os

URL = "https://chykalophia.com/"
file_path = os.path.join("/Users/iuliia603/PycharmProjects/pythonProject/CHYKALOPIA/Test/steps/config.ini")
configs = ConfigReader(file_path)


@given("user opens the Homepage")
def user_opens_homepage(context):
    browser = Browser(URL, configs.get_browser(), configs.get_wait_time())
    context.browser = browser
    context.homepage = HomePage(context.browser)
    context.homepage.get_homepage_title()


@when("user clicks the Capabilities button")
def user_clicks_capabilities_button(context):
    homepage = HomePage(context.browser)
    homepage.open_capabilities_page()


@then("Capabilities page is open")
def capabilities_page_is_open(context):
    context.capabilities_page = CapabilityPage(context.browser)
    context.capabilities_page.get_capability_title()


@when("user clicks the Capabilities dropdown")
def user_clicks_capabilities_dropdown(context):
    header = Header(context.browser)
    header.show_all_capabilities()


@when("user clicks Brand Strategy & Development")
def user_clicks_brand_strategy(context):
    header = Header(context.browser)
    header.select_brand_strategy_section()


@then("Brand Strategy & Development page is open")
def brand_strategy_page_is_open(context):
    brand_strategy_page = BrandStrategyPage(context.browser)
    brand_strategy_page.get_brand_strategy_title()


@when("user clicks the Work button")
def user_clicks_work_button(context):
    homepage = HomePage(context.browser)
    homepage.open_work_page()


@then("Work page is open")
def work_page_is_open(context):
    work_page = WorkPage(context.browser)
    work_page.get_work_title()


@when("user clicks the Get on a call button")
def user_clicks_get_call_button(context):
    header = Header(context.browser)
    header.open_get_call_page()


@then("the page for booking a call is open")
def page_for_booking_call_open(context):
    call_us_page = CallUSPage(context.browser)
    call_us_page.get_call_us_title()


@when("user clicks the logo")
def user_clicks_logo(context):
    header = Header(context.browser)
    header.click_logo()


@then("Home page is open")
def homepage_is_open(context):
    homepage = HomePage(context.browser)
    homepage.get_homepage_title()





