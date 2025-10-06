from pages.base_page import BasePage
from locators.locators import StellarBurgersLocators
import allure


class RegisterPage(BasePage):
    """Страница регистрации пользователя"""

    @allure.step("Открытие страницы регистрации")
    def open_register_page(self):
        """Открытие страницы регистрации"""
        self.driver.get("https://stellarburgers.nomoreparties.site/register")

    @allure.step("Ввод имени в поле регистрации")
    def enter_register_name(self, name):
        """Ввод имени в поле регистрации"""
        self.enter_text(StellarBurgersLocators.REGISTER_NAME_INPUT, name)

    @allure.step("Ввод email в поле регистрации")
    def enter_register_email(self, email):
        """Ввод email в поле регистрации"""
        self.enter_text(StellarBurgersLocators.REGISTER_EMAIL_INPUT, email)

    @allure.step("Ввод пароля в поле регистрации")
    def enter_register_password(self, password):
        """Ввод пароля в поле регистрации"""
        self.enter_text(StellarBurgersLocators.REGISTER_PASSWORD_INPUT, password)

    @allure.step("Клик по кнопке 'Зарегистрироваться'")
    def click_register_submit(self):
        """Клик по кнопке 'Зарегистрироваться'"""
        self.click_element(StellarBurgersLocators.REGISTER_SUBMIT_BUTTON)

    @allure.step("Полная регистрация пользователя")
    def register_user(self, name, email, password):
        """Полная регистрация пользователя"""
        self.enter_register_name(name)
        self.enter_register_email(email)
        self.enter_register_password(password)
        self.click_register_submit()

    @allure.step("Клик по ссылке 'Войти'")
    def click_login_link(self):
        """Клик по ссылке 'Войти'"""
        self.click_element(StellarBurgersLocators.REGISTER_LOGIN_LINK)

    @allure.step("Проверка отображения страницы регистрации")
    def is_register_page_displayed(self):
        """Проверка отображения страницы регистрации"""
        return self.is_element_visible(StellarBurgersLocators.REGISTER_SUBMIT_BUTTON)

    @allure.step("Проверка сообщения об ошибке")
    def is_error_message_displayed(self):
        """Проверка отображения сообщения об ошибке"""
        return self.is_element_visible(StellarBurgersLocators.ERROR_MESSAGE)

    @allure.step("Получение текста ошибки")
    def get_error_message_text(self):
        """Получение текста сообщения об ошибке"""
        return self.get_text(StellarBurgersLocators.ERROR_MESSAGE)

    @allure.step("Проверка валидности пароля")
    def is_password_invalid_message_displayed(self):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.common.exceptions import TimeoutException
        try:
            error_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(StellarBurgersLocators.ERROR_MESSAGE)
            )
            return "Некорректный пароль" in error_element.text
        except TimeoutException:
            return False