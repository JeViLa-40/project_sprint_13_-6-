from pages.main_page import MainPage
from locators.locators_main_page import LocatorsMainPage
from urls import Urls
import pytest
import allure

question_how_much = [LocatorsMainPage.QUESTION_HOW_MUCH, LocatorsMainPage.ANSWER_HOW_MUCH, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.']
question_several_scooters = [LocatorsMainPage.QUESTION_SEVERAL_SCOOTERS, LocatorsMainPage.ANSWER_SEVERAL_SCOOTERS, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']
question_rental_time = [LocatorsMainPage.QUESTION_RENTAL_TIME, LocatorsMainPage.ANSWER_RENTAL_TIME, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.']
question_order_for_today = [LocatorsMainPage.QUESTION_ORDER_FOR_TODAY, LocatorsMainPage.ANSWER_ORDER_FOR_TODAY, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.']
question_order_extention_or_early_return = [LocatorsMainPage.QUESTION_ORDER_EXTENSION_OR_EARLY_RETURN, LocatorsMainPage.ANSWER_ORDER_EXTENSION_OR_EARLY_RETURN, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.']
question_charger = [LocatorsMainPage.QUESTION_CHARGER, LocatorsMainPage.ANSWER_CHARGER, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.']
question_cancel_order = [LocatorsMainPage.QUESTION_CANCEL_ORDER, LocatorsMainPage.ANSWER_CANCEL_ORDER, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']
question_moscow_district = [LocatorsMainPage.QUESTION_MOSCOW_DISTRICT, LocatorsMainPage.ANSWER_MOSCOW_DISTRICT, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']


class TestMainPage:

    @allure.title('Проверка вопросов и ответов на главной странице')
    @pytest.mark.parametrize('question, answer, expected_text',
                             [question_how_much, question_several_scooters, question_rental_time, question_order_for_today, question_order_extention_or_early_return, question_charger, question_cancel_order, question_moscow_district])
    def test_click_on_question(self, driver, question, answer, expected_text):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_on_cookie_app_button()
        main_page.click_on_question(question)
        actually_text = main_page.find_element_with_wait(answer).text
        assert actually_text == expected_text, "Ответ не совпадает с ожидаемым"

    @allure.title('Проверка кнопки Заказать на главной странице')
    def test_order_button_page(self, driver) -> None:
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_on_cookie_app_button()
        main_page.click_on_order_batton_page()
        assert driver.current_url == Urls.ORDER_PAGE_URL

    @allure.title('Проверка кнопки Заказать в заголовке главной страницы')
    def test_order_button_header(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_on_cookie_app_button()
        main_page.click_on_order_batton_header()
        assert driver.current_url == Urls.ORDER_PAGE_URL