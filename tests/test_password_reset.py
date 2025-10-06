import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from locators.locators import StellarBurgersLocators


class TestPasswordReset:
    """Тесты для функциональности восстановления пароля"""

    @allure.title("Переход на страницу восстановления пароля по кнопке 'Восстановить пароль'")
    @allure.description("Проверка перехода на страницу восстановления пароля с главной страницы")
    def test_forgot_password_link_navigation(self, driver):
        """Тест перехода на страницу восстановления пароля"""
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)

        # Шаги
        main_page.open_main_page()
        main_page.click_login_button()
        login_page.click_recover_password_link()

        # Проверка
        assert forgot_password_page.is_forgot_password_page_displayed(), "Страница восстановления пароля не отображается"

    @allure.title("Ввод почты и клик по кнопке 'Восстановить'")
    @allure.description("Проверка ввода email и клика по кнопке восстановления")
    def test_enter_email_and_recover(self, driver, test_user):
        """Тест ввода email и клика по кнопке 'Восстановить'"""
        forgot_password_page = ForgotPasswordPage(driver)

        # Шаги
        forgot_password_page.open_forgot_password_page()
        forgot_password_page.enter_recovery_email(test_user["email"])
        forgot_password_page.click_recover_button()

        # Проверка - после успешного восстановления должна открыться страница reset-password
        reset_password_page = ResetPasswordPage(driver)
        assert reset_password_page.is_reset_password_page_displayed(), "Страница сброса пароля не отображается"

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным")
    @allure.description("Проверка функциональности кнопки показать/скрыть пароль")
    def test_show_hide_password_functionality(self, driver, test_user):
        """Тест функциональности кнопки показать/скрыть пароль"""
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)

        # Шаги - сначала переходим на страницу восстановления
        forgot_password_page.open_forgot_password_page()
        forgot_password_page.enter_recovery_email(test_user["email"])
        forgot_password_page.click_recover_button()
        
        WebDriverWait(driver, 10).until(EC.url_contains("/reset-password"))

        # Проверяем что попали на страницу reset-password
        assert reset_password_page.is_reset_password_page_displayed(), "Страница сброса пароля должна отобразиться"

        # Проверяем наличие кнопки показа пароля
        assert reset_password_page.is_element_visible(StellarBurgersLocators.RESET_SHOW_PASSWORD_BUTTON), "Кнопка показа пароля должна быть доступна"