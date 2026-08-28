from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ищем нужный элемент')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Кликаем на нужный элемент')
    def click_on_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Ожидаем нужный URL')
    def wait_for_url_contains(self, url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url))
