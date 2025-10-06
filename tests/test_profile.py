import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.order_feed_page import OrderFeedPage
from locators.locators import StellarBurgersLocators


class TestProfile:
    """Тесты для функциональности личного кабинета"""

    @allure.title("Переход по клику на 'Личный кабинет'")
    @allure.description("Проверка перехода в личный кабинет с главной страницы")
    def test_profile_navigation(self, driver, test_user):
        """Тест перехода в личный кабинет"""
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        main_page.open_main_page()
        main_page.click_login_button()
        login_page.login_user(test_user["email"], test_user["password"])
        
        WebDriverWait(driver, 10).until(EC.url_contains("stellar"))
        WebDriverWait(driver, 10).until_not(EC.url_contains("login"))
        main_page.click_profile_button()

        assert profile_page.is_profile_page_displayed(), "Страница профиля не отображается"

    @allure.title("Переход в раздел 'История заказов'")
    @allure.description("Проверка перехода в историю заказов из профиля")
    def test_order_history_navigation(self, driver, test_user):
        """Тест перехода в историю заказов"""
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        main_page.open_main_page()
        main_page.click_login_button()
        login_page.login_user(test_user["email"], test_user["password"])
        
        WebDriverWait(driver, 10).until(EC.url_contains("stellar"))
        WebDriverWait(driver, 10).until_not(EC.url_contains("login"))
        main_page.click_profile_button()
        
        WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))
        profile_page.click_order_history_link()

        assert profile_page.is_order_history_page_displayed(), "Страница истории заказов не отображается"

    @allure.title("Выход из аккаунта")
    @allure.description("Проверка выхода из аккаунта через личный кабинет")
    def test_logout_from_account(self, driver, test_user):
        """Тест выхода из аккаунта"""
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        main_page.open_main_page()
        main_page.click_login_button()
        login_page.login_user(test_user["email"], test_user["password"])
        
        WebDriverWait(driver, 10).until(EC.url_contains("stellar"))
        WebDriverWait(driver, 10).until_not(EC.url_contains("login"))
        main_page.click_profile_button()
        
        WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))
        profile_page.click_logout_button()

        assert login_page.is_login_page_displayed(), "Страница входа не отображается после выхода"
