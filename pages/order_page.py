from pages.base_page import BasePage
from locators.locators_order_page import LocatorsOrderPage
from urls import Urls

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(Urls.ORDER_PAGE_URL)

    def choice_station(self, station_locator):
        self.click_on_element_with_wait(LocatorsOrderPage.STATION_FIELD)
        self.click_on_element_with_wait(station_locator)

        

    def making_an_order(self, name, surname, address, station, phone, date, period, colour, comment):
        self.find_element_with_wait(LocatorsOrderPage.NAME_FIELD).send_keys(name)
        self.find_element_with_wait(LocatorsOrderPage.SURNAME_FIELD).send_keys(surname)
        self.find_element_with_wait(LocatorsOrderPage.ADDRESS_FIELD).send_keys(address)
        self.choice_station(station)
        self.find_element_with_wait(LocatorsOrderPage.PHONE_FIELD).send_keys(phone)
        self.click_on_element_with_wait(LocatorsOrderPage.NEXT_BUTTON)
        self.find_element_with_wait(LocatorsOrderPage.DATE_FIELD).send_keys(date)
        self.click_on_element_with_wait(LocatorsOrderPage.RENTAL_PERIOD_LIST)
        self.click_on_element_with_wait(period)
        self.click_on_element_with_wait(colour)
        self.find_element_with_wait(LocatorsOrderPage.COMMENT_FIELD).send_keys(comment)
        self.click_on_element_with_wait(LocatorsOrderPage.ORDER_BUTTON)

    def click_on_scooter_logo(self):
        self.click_on_element_with_wait(LocatorsOrderPage.LOGO_SCOOTER)

    def click_on_yandex_logo(self):
        self.click_on_element_with_wait(LocatorsOrderPage.LOGO_YANDEX)