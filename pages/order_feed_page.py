import allure
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.locators import StellarBurgersLocators


class OrderFeedPage(BasePage):
    """Страница ленты заказов"""

    @allure.step("Открытие страницы ленты заказов")
    def open_order_feed_page(self):
        """Открытие страницы ленты заказов"""
        self.driver.get("https://stellarburgers.nomoreparties.site/feed")

    @allure.step("Клик по первому заказу")
    def click_first_order(self):
        self.wait.until(EC.presence_of_all_elements_located(StellarBurgersLocators.ORDER_FEED_ORDER))
        orders = self.driver.find_elements(*StellarBurgersLocators.ORDER_FEED_ORDER)
        orders[0].click()

    @allure.step("Проверка отображения страницы ленты заказов")
    def is_order_feed_page_displayed(self):
        """Проверка отображения страницы ленты заказов"""
        return self.is_element_visible(StellarBurgersLocators.ORDER_FEED_PAGE_TITLE)

    @allure.step("Ожидание открытия модального окна заказа")
    def wait_order_modal_displayed(self):
        self.wait.until(EC.url_contains("/feed/"))

    @allure.step("Проверка отображения страницы заказа")
    def is_order_modal_displayed(self):
        return "/feed/" in self.driver.current_url and len(self.driver.current_url.split("/feed/")) > 1

    @allure.step("Закрытие модального окна заказа")
    def close_order_modal(self):
        """Закрытие модального окна заказа"""
        self.click_element(StellarBurgersLocators.ORDER_MODAL_CLOSE_BUTTON)

    @allure.step("Получение номера заказа из модального окна")
    def get_order_number_from_modal(self):
        """Получение номера заказа из модального окна"""
        return self.get_text(StellarBurgersLocators.ORDER_MODAL_ORDER_NUMBER)

    @allure.step("Получение количества выполненных заказов за все время")
    def get_total_orders_all_time(self):
        total_text = self.get_text(StellarBurgersLocators.ORDER_FEED_TOTAL_ALL_TIME)
        return int(total_text.replace(' ', ''))

    @allure.step("Получение количества выполненных заказов за сегодня")
    def get_total_orders_today(self):
        total_text = self.get_text(StellarBurgersLocators.ORDER_FEED_TOTAL_TODAY)
        return int(total_text.replace(' ', ''))

