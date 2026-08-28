from pages.base_page import BasePage
from locators.locators_main_page import LocatorsMainPage
from urls import Urls
import allure

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем главную страницу')
    def open_page(self):
        self.driver.get(Urls.MAIN_PAGE_URL)

    @allure.step('Кликаем по кнопке согласия с куками')
    def click_on_cookie_app_button(self):
        self.click_on_element_with_wait(LocatorsMainPage.COOKIE_APP_BUTTON)

    @allure.step('Кликаем на кнопку Заказать на странице')
    def click_on_order_batton_page(self):
        self.click_on_element_with_wait(LocatorsMainPage.ORDER_BUTTON_PAGE)

    @allure.step('Кликаем на кнопку Заказать в заголовке')
    def click_on_order_batton_header(self):
        self.click_on_element_with_wait(LocatorsMainPage.ORDER_BUTTON_HEADER)

    @allure.step('Кликаем по вопросу на главной странице')
    def click_on_question(self, question):
        self.click_on_element_with_wait(question)
