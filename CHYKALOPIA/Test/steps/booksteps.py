from behave import given, when, then
from config.config_reader import ConfigReader
import os
from CHYKALOPIA.Wrapper_Chyka.Browser import Browser
from CHYKALOPIA.Wrapper_Chyka.Header import Header
from CHYKALOPIA.Wrapper_Chyka.Home_Page import HomePage
from CHYKALOPIA.Wrapper_Chyka.Call_us_Page import CallUSPage
from CHYKALOPIA.Wrapper_Chyka.Calendar import Calendar
from CHYKALOPIA.Test.steps.chykasteps import user_opens_homepage
import time


URL = "https://chykalophia.com/"
file_path = os.path.join("/Users/iuliia603/PycharmProjects/pythonProject/CHYKALOPIA/Test/steps/config.ini")
configs = ConfigReader(file_path)


@given('user clicks the Get a call button')
def user_clicks_get_call_button(context):
    header = Header(context.browser)
    header.open_get_call_page()


@given("the booking page is open")
def booking_page_call_open(context):
    call_us_page = CallUSPage(context.browser)
    call_us_page.get_call_us_title()


@when('user clicks the Get start button')
def user_clicks_get_start_btn(context):
    call_us_page = CallUSPage(context.browser)
    call_us_page.click_get_started()
    time.sleep(12)


@then('the calendar is open')
def calendar_is_open(context):
#    browser = Browser
    calendar = Calendar(context.browser)
    calendar.switch_to_calendar_frame()
    time.sleep(6)
    assert calendar.get_calendar_title() == "Select a Date & Time"


@when('user selects data')
def user_selects_data(context):
    calendar = Calendar(context.browser)
    calendar.switch_to_calendar_frame()
    calendar.select_the_date('November 29')

# @when('user select time')
# def user_select_time(context):
#
# @when('user clicks the Next button')
# def user_clicks_next_btn(context):
#
# @then('the information about the call is displayed')
# def information_about_call_is_displayed(context):

