from pages.base_page import BasePage
from locators.locators_main_page import LocatorsMainPage
from urls import Urls

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(Urls.MAIN_PAGE_URL)

    def click_on_cookie_app_button(self):
        self.click_on_element_with_wait(LocatorsMainPage.COOKIE_APP_BUTTON)

    def click_on_order_batton_page(self):
        self.click_on_element_with_wait(LocatorsMainPage.ORDER_BUTTON_PAGE)

    def click_on_order_batton_header(self):
        self.click_on_element_with_wait(LocatorsMainPage.ORDER_BUTTON_HEADER)

    def click_on_question_how_much(self):
        self.click_on_element_with_wait(LocatorsMainPage.QUESTION_HOW_MUCH)

    def click_on_question_several_scooters(self):
        self.click_on_element_with_wait(LocatorsMainPage.QUESTION_SEVERAL_SCOOTERS)

    def click_on_question_rental_time(self):
        self.click_on_element_with_wait(LocatorsMainPage.QUESTION_RENTAL_TIME)

    def click_on_question_order_for_today(self):
        self.click_on_element_with_wait(LocatorsMainPage.QUESTION_ORDER_FOR_TODAY)

    def click_on_question_order_extension_or_early_return(self):
        self.click_on_element_with_wait(LocatorsMainPage.QUESTION_ORDER_EXTENSION_OR_EARLY_RETURN)

    def click_on_question_charger(self):
        self.click_on_element_with_wait(LocatorsMainPage.QUESTION_CHARGER)

    def click_on_question_cancel_order(self):
        self.click_on_element_with_wait(LocatorsMainPage.QUESTION_CANCEL_ORDER)

    def click_on_question_moscow_district(self):
        self.click_on_element_with_wait(LocatorsMainPage.QUESTION_MOSCOW_DISTRICT)
