from selenium.webdriver.common.by import By

class LocatorsOrderPage:
    NAME_FIELD = [By.XPATH, './/input[@placeholder="* Имя"]']
    SURNAME_FIELD = [By.XPATH, './/input[@placeholder="* Фамилия"]']
    ADDRESS_FIELD = [By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]']
    STATION_FIELD = [By.XPATH, './/input[@placeholder="* Станция метро"]']

    STATION_ROCOSSOVSKOGO = [By.XPATH, './/*[text()="Бульвар Рокоссовского"]']
    STATION_SOKOLNIKI = [By.XPATH, './/*[text()="Сокольники"]']

    PHONE_FIELD = [By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]']

    NEXT_BUTTON = [By.XPATH, './/button[text()="Далее"]']

    DATE_FIELD = [By.XPATH, './/input[@placeholder="* Когда привезти самокат"]']

    RENTAL_PERIOD_LIST = [By.CSS_SELECTOR, '.Dropdown-arrow']

    RENTAL_PERIOD_DAY = [By.XPATH, './/div[text()="сутки"]']
    RENTAL_PERIOD_TWO_DAYS = [By.XPATH, './/div[text()="двое суток"]']

    CHECKBOX_BLACK_COLOUR = [By.ID, 'black']
    CHECKBOX_GREY_COLOUR = [By.ID, 'grey']

    COMMENT_FIELD = [By.XPATH, './/input[@placeholder="Комментарий для курьера"]']
    ORDER_BUTTON = [By.XPATH, './/*[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]']

    HEADER_ORDER_IS_PLACED = [By.CSS_SELECTOR, '.Order_ModalHeader__3FDaJ']

    LOGO_SCOOTER = [By.XPATH, './/img[@alt="Scooter"]']
    LOGO_YANDEX = [By.XPATH, './/*[@href="//yandex.ru"]']
