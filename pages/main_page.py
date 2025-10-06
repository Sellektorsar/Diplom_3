import allure
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.locators import StellarBurgersLocators


class MainPage(BasePage):
    """Главная страница Stellar Burgers"""

    @allure.step("Открытие главной страницы")
    def open_main_page(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    @allure.step("Клик по кнопке 'Конструктор'")
    def click_constructor_button(self):
        self.click_element(StellarBurgersLocators.MAIN_PAGE_CONSTRUCTOR_LINK)

    @allure.step("Клик по кнопке 'Лента заказов'")
    def click_order_feed_button(self):
        self.click_element(StellarBurgersLocators.MAIN_PAGE_ORDER_FEED_LINK)

    @allure.step("Клик по кнопке 'Личный кабинет'")
    def click_profile_button(self):
        self.click_element(StellarBurgersLocators.MAIN_PAGE_PROFILE_LINK)

    @allure.step("Клик по кнопке 'Войти в аккаунт'")
    def click_login_button(self):
        self.click_element(StellarBurgersLocators.LOGIN_BUTTON)

    @allure.step("Проверка отображения главной страницы")
    def is_main_page_displayed(self):
        return self.is_element_visible(StellarBurgersLocators.MAIN_PAGE_CONSTRUCTOR_LINK)

    @allure.step("Добавление первого ингредиента в заказ")
    def add_first_ingredient_to_order(self):
        self.wait.until(EC.presence_of_element_located(StellarBurgersLocators.CONSTRUCTOR_DROP_ZONE))
        ingredients = self.get_elements_list(StellarBurgersLocators.CONSTRUCTOR_INGREDIENT)
        drop_zone = self.driver.find_element(*StellarBurgersLocators.CONSTRUCTOR_DROP_ZONE)
        self.actions.drag_and_drop(ingredients[0], drop_zone).perform()

    @allure.step("Получение счетчика первого ингредиента")
    def get_first_ingredient_counter(self):
        self.wait.until(EC.presence_of_element_located(StellarBurgersLocators.CONSTRUCTOR_INGREDIENT_COUNTER))
        counters = self.get_elements_list(StellarBurgersLocators.CONSTRUCTOR_INGREDIENT_COUNTER)
        counter_text = counters[0].text
        return int(counter_text) if counter_text.isdigit() else 0

    @allure.step("Клик по первому ингредиенту")
    def click_first_ingredient(self):
        ingredients = self.get_elements_list(StellarBurgersLocators.CONSTRUCTOR_INGREDIENT)
        ingredients[0].click()

    @allure.step("Ожидание открытия модального окна ингредиента")
    def wait_ingredient_modal_displayed(self):
        self.wait.until(EC.visibility_of_element_located(StellarBurgersLocators.INGREDIENT_MODAL))

    @allure.step("Проверка отображения модального окна ингредиента")
    def is_ingredient_modal_displayed(self):
        return self.is_element_visible(StellarBurgersLocators.INGREDIENT_MODAL)

    @allure.step("Закрытие модального окна ингредиента")
    def close_ingredient_modal(self):
        self.click_element(StellarBurgersLocators.INGREDIENT_MODAL_CLOSE_BUTTON)
        self.wait.until(EC.invisibility_of_element_located(StellarBurgersLocators.INGREDIENT_MODAL))

    @allure.step("Клик по кнопке 'Оформить заказ'")
    def click_place_order_button(self):
        self.click_element(StellarBurgersLocators.CONSTRUCTOR_ORDER_BUTTON)

    @allure.step("Ожидание кнопки 'Оформить заказ'")
    def wait_for_order_button_visible(self):
        self.wait.until(EC.visibility_of_element_located(StellarBurgersLocators.CONSTRUCTOR_ORDER_BUTTON))

    @allure.step("Проверка видимости кнопки 'Оформить заказ'")
    def is_order_button_visible(self):
        return self.is_element_visible(StellarBurgersLocators.CONSTRUCTOR_ORDER_BUTTON)
