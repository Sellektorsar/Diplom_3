from pages.base_page import BasePage
from locators.locators import StellarBurgersLocators
import allure


class ResetPasswordPage(BasePage):
    """Страница восстановления пароля"""

    @allure.step("Открытие страницы восстановления пароля")
    def open_reset_password_page(self):
        """Открытие страницы восстановления пароля"""
        self.driver.get("https://stellarburgers.nomoreparties.site/reset-password")

    @allure.step("Ввод нового пароля")
    def enter_new_password(self, password):
        """Ввод нового пароля"""
        self.enter_text(StellarBurgersLocators.RESET_PASSWORD_INPUT, password)

    @allure.step("Ввод токена восстановления")
    def enter_reset_token(self, token):
        """Ввод токена восстановления"""
        self.enter_text(StellarBurgersLocators.RESET_TOKEN_INPUT, token)

    @allure.step("Клик по кнопке 'Сохранить'")
    def click_save_button(self):
        """Клик по кнопке 'Сохранить'"""
        self.click_element(StellarBurgersLocators.RESET_SAVE_BUTTON)

    @allure.step("Полное восстановление пароля")
    def reset_password(self, password, token):
        """Полное восстановление пароля"""
        self.enter_new_password(password)
        self.enter_reset_token(token)
        self.click_save_button()

    @allure.step("Клик по кнопке показать/скрыть пароль")
    def click_show_password_button(self):
        """Клик по кнопке показать/скрыть пароль"""
        self.click_element(StellarBurgersLocators.RESET_SHOW_PASSWORD_BUTTON)

    @allure.step("Проверка отображения страницы восстановления пароля")
    def is_reset_password_page_displayed(self):
        """Проверка отображения страницы восстановления пароля"""
        return self.is_element_visible(StellarBurgersLocators.RESET_SAVE_BUTTON)

    @allure.step("Проверка активности поля пароля")
    def is_password_field_active(self):
        from selenium.common.exceptions import NoSuchElementException
        try:
            password_input = self.driver.find_element(*StellarBurgersLocators.RESET_PASSWORD_INPUT)
            return password_input.get_attribute("type") == "text"
        except NoSuchElementException:
            return False

    @allure.step("Проверка скрытости поля пароля")
    def is_password_field_hidden(self):
        from selenium.common.exceptions import NoSuchElementException
        try:
            password_input = self.driver.find_element(*StellarBurgersLocators.RESET_PASSWORD_INPUT)
            return password_input.get_attribute("type") == "password"
        except NoSuchElementException:
            return True