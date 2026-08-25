from selenium.webdriver.common.by import By

class LocatorsMainPage:
    COOKIE_APP_BUTTON = [By.CSS_SELECTOR, '.App_CookieButton__3cvqF']

    QUESTION_HOW_MUCH = [By.CLASS_NAME, 'accordion__button']
    ANSWER_HOW_MUCH = [By.XPATH, './/*[@id="accordion__panel-0"]/p']
    QUESTION_SEVERAL_SCOOTERS = [By.ID, 'accordion__heading-1']
    ANSWER_SEVERAL_SCOOTERS = [By.XPATH, './/*[@id="accordion__panel-1"]/p']
    QUESTION_RENTAL_TIME = [By.ID, 'accordion__heading-2']
    ANSWER_RENTAL_TIME = [By.XPATH, './/*[@id="accordion__panel-2"]/p']
    QUESTION_ORDER_FOR_TODAY = [By.ID, 'accordion__heading-3']
    ANSWER_ORDER_FOR_TODAY = [By.XPATH, './/*[@id="accordion__panel-3"]/p']
    QUESTION_ORDER_EXTENSION_OR_EARLY_RETURN = [By.ID, 'accordion__heading-4']
    ANSWER_ORDER_EXTENSION_OR_EARLY_RETURN = [By.XPATH, './/*[@id="accordion__panel-4"]/p']
    QUESTION_CHARGER = [By.ID, 'accordion__heading-5']
    ANSWER_CHARGER = [By.XPATH, './/*[@id="accordion__panel-5"]/p']
    QUESTION_CANCEL_ORDER = [By.ID, 'accordion__heading-6']
    ANSWER_CANCEL_ORDER = [By.XPATH, './/*[@id="accordion__panel-6"]/p']
    QUESTION_MOSCOW_DISTRICT = [By.ID, 'accordion__heading-7']
    ANSWER_MOSCOW_DISTRICT = [By.XPATH, './/*[@id="accordion__panel-7"]/p']

    ORDER_BUTTON_PAGE = [By.XPATH, '//*[@class="Home_FinishButton__1_cWm"]/button']
    ORDER_BUTTON_HEADER = [By.XPATH, './/div[@class = "Header_Nav__AGCXC"]/button[text()="Заказать"]']
