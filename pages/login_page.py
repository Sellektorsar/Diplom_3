from pages.base_page import BasePage
from locators.locators import StellarBurgersLocators
import allure


class LoginPage(BasePage):
    """Страница входа в систему"""

    @allure.step("Открытие страницы входа")
    def open_login_page(self):
        """Открытие страницы входа"""
        self.driver.get("https://stellarburgers.nomoreparties.site/login")

    @allure.step("Ввод email в поле для входа")
    def enter_login_email(self, email):
        """Ввод email в поле для входа"""
        self.enter_text(StellarBurgersLocators.LOGIN_EMAIL_INPUT, email)

    @allure.step("Ввод пароля в поле для входа")
    def enter_login_password(self, password):
        """Ввод пароля в поле для входа"""
        self.enter_text(StellarBurgersLocators.LOGIN_PASSWORD_INPUT, password)

    @allure.step("Клик по кнопке 'Войти'")
    def click_login_submit(self):
        """Клик по кнопке 'Войти'"""
        self.click_element(StellarBurgersLocators.LOGIN_SUBMIT_BUTTON)

    @allure.step("Полная авторизация пользователя")
    def login_user(self, email, password):
        """Полная авторизация пользователя"""
        self.enter_login_email(email)
        self.enter_login_password(password)
        self.click_login_submit()

    @allure.step("Клик по ссылке 'Зарегистрироваться'")
    def click_register_link(self):
        """Клик по ссылке 'Зарегистрироваться'"""
        self.click_element(StellarBurgersLocators.REGISTER_BUTTON)

    @allure.step("Клик по ссылке 'Восстановить пароль'")
    def click_recover_password_link(self):
        """Клик по ссылке 'Восстановить пароль'"""
        self.click_element(StellarBurgersLocators.RECOVER_PASSWORD_LINK)

    @allure.step("Проверка отображения страницы входа")
    def is_login_page_displayed(self):
        """Проверка отображения страницы входа"""
        return self.is_element_visible(StellarBurgersLocators.LOGIN_SUBMIT_BUTTON)

    @allure.step("Проверка сообщения об ошибке")
    def is_error_message_displayed(self):
        """Проверка отображения сообщения об ошибке"""
        return self.is_element_visible(StellarBurgersLocators.ERROR_MESSAGE)

    @allure.step("Получение текста ошибки")
    def get_error_message_text(self):
        """Получение текста сообщения об ошибке"""
        return self.get_text(StellarBurgersLocators.ERROR_MESSAGE)