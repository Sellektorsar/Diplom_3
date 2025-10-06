import allure
import pytest

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage


class TestMainFunctionality:
    """Тесты для основного функционала приложения"""

    @allure.title("Переход по клику на 'Конструктор'")
    @allure.description("Проверка перехода в конструктор с главной страницы")
    def test_constructor_navigation(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_constructor_button()
        
        assert main_page.is_main_page_displayed()

    @allure.title("Переход по клику на 'Лента заказов'")
    @allure.description("Проверка перехода в ленту заказов с главной страницы")
    def test_order_feed_navigation(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page.open_main_page()
        main_page.click_order_feed_button()
        
        assert order_feed_page.is_order_feed_page_displayed()

    @allure.title("Клик по ингредиенту открывает модальное окно с деталями")
    @allure.description("Проверка открытия модального окна с деталями ингредиента")
    def test_ingredient_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_first_ingredient()
        main_page.wait_ingredient_modal_displayed()
        
        assert main_page.is_ingredient_modal_displayed()

    @allure.title("Модальное окно ингредиента закрывается кликом по крестику")
    @allure.description("Проверка закрытия модального окна ингредиента")
    def test_ingredient_modal_close(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_first_ingredient()
        main_page.close_ingredient_modal()
        
        assert not main_page.is_ingredient_modal_displayed()

    @allure.title("При добавлении ингредиента в заказ увеличивается каунтер")
    @allure.description("Проверка увеличения счетчика ингредиента при добавлении в заказ")
    def test_ingredient_counter_increase(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        initial_counter = main_page.get_first_ingredient_counter()
        main_page.add_first_ingredient_to_order()
        final_counter = main_page.get_first_ingredient_counter()
        
        assert final_counter > initial_counter

    @allure.title("Залогиненный пользователь может оформить заказ")
    @allure.description("Проверка возможности оформления заказа авторизованным пользователем")
    def test_authorized_user_can_place_order(self, driver, test_user, test_ingredients):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.open_main_page()
        main_page.click_login_button()
        login_page.login_user(test_user["email"], test_user["password"])
        main_page.wait_for_order_button_visible()
        
        assert main_page.is_order_button_visible()
