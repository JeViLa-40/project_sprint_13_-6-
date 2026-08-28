from pages.order_page import OrderPage
import pytest
from locators.locators_order_page import LocatorsOrderPage
from urls import Urls
import allure


data_set1 = ['Антон', 'Самойлов', 'ул. Королева, д.1', LocatorsOrderPage.STATION_ROCOSSOVSKOGO, '89998005555', '30.08.2026', LocatorsOrderPage.RENTAL_PERIOD_DAY, LocatorsOrderPage.CHECKBOX_BLACK_COLOUR, 'Жду у подъезда']
data_set2 = ['Юлия', 'Милова', 'пр. Победы, 8', LocatorsOrderPage.STATION_SOKOLNIKI, '+7999343567', '31.08.2026', LocatorsOrderPage.RENTAL_PERIOD_TWO_DAYS, LocatorsOrderPage.CHECKBOX_GREY_COLOUR, 'В 11.00']

class TestOrderPage:

    @allure.title('Проверка создания заказа')
    @pytest.mark.parametrize('data_set', [data_set1, data_set2])
    def test_making_an_order(self, driver, data_set):
        order_page = OrderPage(driver)
        order_page.open_page()
        order_page.making_an_order(*data_set)
        header = order_page.find_element_with_wait(LocatorsOrderPage.HEADER_ORDER_IS_PLACED)
        assert header.is_displayed()

    @allure.title('Проверка клика по логотипу Скутер')
    def test_click_on_scooter_logo(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page()
        order_page.click_on_scooter_logo()

        order_page.wait_for_url_contains(Urls.MAIN_PAGE_URL)
        assert driver.current_url == Urls.MAIN_PAGE_URL

    @allure.title('Проверка клика по логотипу Яндекс')
    def test_click_on_yandex_logo(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page()
        order_page.click_on_yandex_logo()
#изменить, тут проблема таймаут
        driver.switch_to.window(driver.window_handles[-1])
        order_page.wait_for_url_contains(Urls.DZEN_URL)
        assert Urls.DZEN_URL in driver.current_url
