from behave import given, when, then
from config.config_reader import ConfigReader
import os
from CHYKALOPIA.Wrapper_Chyka.Browser import Browser
from CHYKALOPIA.Wrapper_Chyka.Design_page import UIUXPage
import time
from selenium.webdriver.support.color import Color


URL = "https://chykalophia.com/uiux/"
file_path = os.path.join("/Users/iuliia603/PycharmProjects/pythonProject/CHYKALOPIA/Test/steps/config.ini")
configs = ConfigReader(file_path)


@given("user opens UI/UX page")
def user_opens_UI_UX_page(context):
    browser = Browser(URL, configs.get_browser(), configs.get_wait_time())
    context.browser = browser
    context.design_page = UIUXPage(context.browser)
    context.design_page.get_ui_ux_title()


@given('user scrolls to Frequently Asked Questions')
def user_scrolls_questions(context):
    context.design_page = UIUXPage(context.browser)
    context.design_page.scroll_to_questions_title()


@when('user clicks on the question Why should I care about UX for my website?')
def user_clicks_que_why_care_about_UX_for_website(context):
    context.design_page = UIUXPage(context.browser)
    context.design_page.click_ux_for_website_que()
    time.sleep(10)


@then('answer about care is visible')
def answer_care_is_visible(context):
    context.design_page = UIUXPage(context.browser)
    context.design_page.get_ux_for_website_text()


@then('the first question color is black')
def question_color_is_black(context):
     context.design_page = UIUXPage(context.browser)
     ux_for_website_que = context.design_page.ux_for_website_que
     ux_for_website_que.wait_until_visible()

     background_color = ux_for_website_que.value_of_css_property("color")
     converted_background_color = Color.from_string(background_color)
     assert converted_background_color.rgb == 'rgb(0, 0, 0)'


@then('answer about care is not visible')
def answer_care_is_not_visible(context):
    context.design_page = UIUXPage(context.browser)
    context.design_page.get_ux_for_website_text()

    assert not context.design_page.get_ux_for_website_text()


@then('the first question color is gray')
def question_color_is_gray(context):
    context.design_page = UIUXPage(context.browser)
    ux_for_website_que_2 = context.design_page.ux_for_website_que
    ux_for_website_que_2.wait_until_visible()

    background_color_2 = ux_for_website_que_2.value_of_css_property("color")
    converted_background_color_2 = Color.from_string(background_color_2)
    assert converted_background_color_2.rgb == 'rgb(183, 183, 183)'


@when('user clicks on the question What should I prepare for my UX project?')
def user_clicks_question_prepare_ux_project(context):
    context.design_page = UIUXPage(context.browser)
    context.design_page.click_prepare_ux_que()
    time.sleep(10)


@then('answer about prepare is visible')
def answer_prepare_is_visible(context):
    context.design_page = UIUXPage(context.browser)
    context.design_page.get_prepare_ux_text()


@then('the second question color is black')
def question_color_is_black(context):
     context.design_page = UIUXPage(context.browser)
     prepare_ux_que = context.design_page.prepare_ux_que
     prepare_ux_que.wait_until_visible()

     background_color_3 = prepare_ux_que.value_of_css_property("color")
     converted_background_color_3 = Color.from_string(background_color_3)
     assert converted_background_color_3.rgb == 'rgb(0, 0, 0)'


@then('the second question color is gray')
def question_color_is_gray(context):
    context.design_page = UIUXPage(context.browser)
    prepare_ux_que_2 = context.design_page.prepare_ux_que
    prepare_ux_que_2.wait_until_visible()

    background_color_4 = prepare_ux_que_2.value_of_css_property("color")
    converted_background_color_4 = Color.from_string(background_color_4)
    assert converted_background_color_4.rgb == 'rgb(183, 183, 183)'


@when('user clicks on the question Do I need UX strategy?')
def user_clicks_question_need_strategy(context):
    context.design_page = UIUXPage(context.browser)
    context.design_page.click_need_ux_strategy_que()
    time.sleep(10)


@then('answer about need UX strategy is visible')
def answer_need_strategy_is_visible(context):
    context.design_page = UIUXPage(context.browser)
    context.design_page.get_need_ux_strategy_text()


@then('the third question color is black')
def question_color_is_black(context):
     context.design_page = UIUXPage(context.browser)
     need_ux_strategy_que = context.design_page.need_ux_strategy_que
     need_ux_strategy_que.wait_until_visible()

     background_color_5 = need_ux_strategy_que.value_of_css_property("color")
     converted_background_color_5 = Color.from_string(background_color_5)
     assert converted_background_color_5.rgb == 'rgb(0, 0, 0)'


@then('the third question color is gray')
def question_color_is_gray(context):
    context.design_page = UIUXPage(context.browser)
    need_ux_strategy_que_2 = context.design_page.need_ux_strategy_que
    need_ux_strategy_que_2.wait_until_visible()

    background_color_6 = need_ux_strategy_que_2.value_of_css_property("color")
    converted_background_color_6 = Color.from_string(background_color_6)
    assert converted_background_color_6.rgb == 'rgb(183, 183, 183)'


@when('user clicks on the question What’s the investment price range?')
def user_clicks_question_investment_price_range(context):
    context.design_page = UIUXPage(context.browser)
    context.design_page.click_investment_price_range_que()
    time.sleep(6)


@then('answer about investment price range is visible')
def answer_investment_price_range_is_visible(context):
    context.design_page = UIUXPage(context.browser)
    context.design_page.get_investment_price_range_text()


@then('the fourth question color is black')
def question_color_is_black(context):
     context.design_page = UIUXPage(context.browser)
     investment_price_range_que = context.design_page.investment_price_range_que
     investment_price_range_que.wait_until_visible()

     background_color_7 = investment_price_range_que.value_of_css_property("color")
     converted_background_color_7 = Color.from_string(background_color_7)
     assert converted_background_color_7.rgb == 'rgb(0, 0, 0)'


@then('the fourth question color is gray')
def question_color_is_gray(context):
    context.design_page = UIUXPage(context.browser)
    investment_price_range_que_2 = context.design_page.investment_price_range_que
    investment_price_range_que_2.wait_until_visible()

    background_color_8 = investment_price_range_que_2.value_of_css_property("color")
    converted_background_color_8 = Color.from_string(background_color_8)
    assert converted_background_color_8.rgb == 'rgb(183, 183, 183)'


@when('user clicks on the question How long will a UX project take?')
def user_clicks_question_how_long(context):
    context.design_page = UIUXPage(context.browser)
    context.design_page.click_how_long_ux_que()
    time.sleep(6)


@then('answer about How long is visible')
def answer_how_long_is_visible(context):
    context.design_page = UIUXPage(context.browser)
    context.design_page.get_how_long_ux_text()


@then('the fifth question color is black')
def question_color_is_black(context):
     context.design_page = UIUXPage(context.browser)
     how_long_ux_que = context.design_page.how_long_ux_que
     how_long_ux_que.wait_until_visible()

     background_color_9 = how_long_ux_que.value_of_css_property("color")
     converted_background_color_9 = Color.from_string(background_color_9)
     assert converted_background_color_9.rgb == 'rgb(0, 0, 0)'


@then('the fifth question color is gray')
def question_color_is_gray(context):
    how_long_ux_que_2 = context.design_page.how_long_ux_que
    how_long_ux_que_2.wait_until_visible()

    background_color_10 = how_long_ux_que_2.value_of_css_property("color")
    converted_background_color_10 = Color.from_string(background_color_10)
    assert converted_background_color_10.rgb == 'rgb(183, 183, 183)'