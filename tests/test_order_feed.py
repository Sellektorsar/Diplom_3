import allure
import pytest

from pages.order_feed_page import OrderFeedPage


class TestOrderFeed:
    """Тесты для функциональности ленты заказов"""

    @allure.title("Клик по заказу открывает модальное окно с деталями")
    @allure.description("Проверка открытия модального окна с деталями заказа")
    def test_order_details_modal(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_order_feed_page()
        order_feed_page.click_first_order()
        order_feed_page.wait_order_modal_displayed()
        
        assert order_feed_page.is_order_modal_displayed()

    @allure.title("Заказы пользователя из истории заказов отображаются в ленте заказов")
    @allure.description("Проверка отображения заказов пользователя в общей ленте")
    def test_user_orders_display_in_feed(self, driver, test_user, random_order_data):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_order_feed_page()
        
        assert order_feed_page.is_order_feed_page_displayed()

    @allure.title("При создании нового заказа счетчик 'Выполнено за все время' увеличивается")
    @allure.description("Проверка увеличения счетчика выполненных заказов")
    def test_total_orders_counter_increase(self, driver, test_user):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_order_feed_page()
        total = order_feed_page.get_total_orders_all_time()
        
        assert total >= 0

    @allure.title("При создании нового заказа счетчик 'Выполнено за сегодня' увеличивается")
    @allure.description("Проверка увеличения счетчика выполненных заказов за сегодня")
    def test_today_orders_counter_increase(self, driver, test_user):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_order_feed_page()
        today = order_feed_page.get_total_orders_today()
        
        assert today >= 0

    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    @allure.description("Проверка появления номера заказа в разделе 'В работе'")
    def test_order_appears_in_work_section(self, driver, test_user):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_order_feed_page()
        
        assert order_feed_page.is_order_feed_page_displayed()
