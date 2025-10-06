from pages.base_page import BasePage
from locators.locators import StellarBurgersLocators
import allure


class ForgotPasswordPage(BasePage):
    """Страница восстановления пароля"""

    @allure.step("Открытие страницы восстановления пароля")
    def open_forgot_password_page(self):
        """Открытие страницы восстановления пароля"""
        self.driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

    @allure.step("Ввод email для восстановления пароля")
    def enter_recovery_email(self, email):
        """Ввод email для восстановления пароля"""
        self.enter_text(StellarBurgersLocators.RECOVER_EMAIL_INPUT, email)

    @allure.step("Клик по кнопке 'Восстановить'")
    def click_recover_button(self):
        """Клик по кнопке 'Восстановить'"""
        self.click_element(StellarBurgersLocators.RECOVER_SUBMIT_BUTTON)

    @allure.step("Полное восстановление пароля")
    def recover_password(self, email):
        """Полное восстановление пароля"""
        self.enter_recovery_email(email)
        self.click_recover_button()

    @allure.step("Клик по ссылке 'Войти'")
    def click_login_link(self):
        """Клик по ссылке 'Войти'"""
        self.click_element(StellarBurgersLocators.RECOVER_LOGIN_LINK)

    @allure.step("Проверка отображения страницы восстановления пароля")
    def is_forgot_password_page_displayed(self):
        """Проверка отображения страницы восстановления пароля"""
        return self.is_element_visible(StellarBurgersLocators.RECOVER_SUBMIT_BUTTON)

    @allure.step("Проверка активности поля email")
    def is_email_field_active(self):
        """Проверка активности поля email"""
        return self.is_element_enabled(StellarBurgersLocators.RECOVER_EMAIL_INPUT)