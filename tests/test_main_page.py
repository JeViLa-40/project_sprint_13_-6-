from pages.main_page import MainPage
from locators.locators_main_page import LocatorsMainPage
from urls import Urls

class TestMainPage:
    def test_question_how_much(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_on_cookie_app_button()
        main_page.click_on_question_how_much()
        answer = main_page.find_element_with_wait(LocatorsMainPage.ANSWER_HOW_MUCH)
        assert answer.text == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.', "Ответ не совпадает с ожидаемым"

    def test_question_several_scooters(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_on_cookie_app_button()
        main_page.click_on_question_several_scooters()
        answer = main_page.find_element_with_wait(LocatorsMainPage.ANSWER_SEVERAL_SCOOTERS)
        assert answer.text == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    def test_question_rental_time(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_on_cookie_app_button()
        main_page.click_on_question_rental_time()
        answer = main_page.find_element_with_wait(LocatorsMainPage.ANSWER_RENTAL_TIME)
        assert answer.text == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    def test_question_order_for_today(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_on_cookie_app_button()
        main_page.click_on_question_order_for_today()
        answer = main_page.find_element_with_wait(LocatorsMainPage.ANSWER_ORDER_FOR_TODAY)
        assert answer.text == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    def test_question_order_extention_or_early_return(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_on_cookie_app_button()
        main_page.click_on_question_order_extension_or_early_return()
        answer = main_page.find_element_with_wait(LocatorsMainPage.ANSWER_ORDER_EXTENSION_OR_EARLY_RETURN)
        assert answer.text == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    def test_question_charger(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_on_cookie_app_button()
        main_page.click_on_question_charger()
        answer = main_page.find_element_with_wait(LocatorsMainPage.ANSWER_CHARGER)
        assert answer.text == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    def test_question_cancel_order(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_on_cookie_app_button()
        main_page.click_on_question_cancel_order()
        answer = main_page.find_element_with_wait(LocatorsMainPage.ANSWER_CANCEL_ORDER)
        assert answer.text == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    def test_question_moscow_district(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_on_cookie_app_button()
        main_page.click_on_question_moscow_district()
        answer = main_page.find_element_with_wait(LocatorsMainPage.ANSWER_MOSCOW_DISTRICT)
        assert answer.text == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    def test_order_button_page(self, driver) -> None:
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_on_cookie_app_button()
        main_page.click_on_order_batton_page()
        assert driver.current_url == Urls.ORDER_PAGE_URL

    def test_order_button_header(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_on_cookie_app_button()
        main_page.click_on_order_batton_header()
        assert driver.current_url == Urls.ORDER_PAGE_URL