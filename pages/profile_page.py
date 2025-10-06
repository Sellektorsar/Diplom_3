from pages.base_page import BasePage
from locators.locators import StellarBurgersLocators
import allure


class ProfilePage(BasePage):
    """Страница профиля пользователя"""

    @allure.step("Открытие страницы профиля")
    def open_profile_page(self):
        """Открытие страницы профиля"""
        self.driver.get("https://stellarburgers.nomoreparties.site/account/profile")

    @allure.step("Ввод имени в поле профиля")
    def enter_profile_name(self, name):
        """Ввод имени в поле профиля"""
        self.enter_text(StellarBurgersLocators.PROFILE_NAME_INPUT, name)

    @allure.step("Ввод email в поле профиля")
    def enter_profile_email(self, email):
        """Ввод email в поле профиля"""
        self.enter_text(StellarBurgersLocators.PROFILE_EMAIL_INPUT, email)

    @allure.step("Ввод пароля в поле профиля")
    def enter_profile_password(self, password):
        """Ввод пароля в поле профиля"""
        self.enter_text(StellarBurgersLocators.PROFILE_PASSWORD_INPUT, password)

    @allure.step("Клик по кнопке 'Сохранить'")
    def click_save_button(self):
        """Клик по кнопке 'Сохранить'"""
        self.click_element(StellarBurgersLocators.PROFILE_SAVE_BUTTON)

    @allure.step("Клик по кнопке 'Отмена'")
    def click_cancel_button(self):
        """Клик по кнопке 'Отмена'"""
        self.click_element(StellarBurgersLocators.PROFILE_CANCEL_BUTTON)

    @allure.step("Клик по кнопке 'Выход'")
    def click_logout_button(self):
        """Клик по кнопке 'Выход'"""
        self.click_element(StellarBurgersLocators.PROFILE_LOGOUT_BUTTON)

    @allure.step("Клик по ссылке 'История заказов'")
    def click_order_history_link(self):
        """Клик по ссылке 'История заказов'"""
        self.click_element(StellarBurgersLocators.PROFILE_HISTORY_LINK)

    @allure.step("Полное обновление профиля")
    def update_profile(self, name=None, email=None, password=None):
        """Полное обновление профиля"""
        if name:
            self.enter_profile_name(name)
        if email:
            self.enter_profile_email(email)
        if password:
            self.enter_profile_password(password)
        self.click_save_button()

    @allure.step("Проверка отображения страницы профиля")
    def is_profile_page_displayed(self):
        """Проверка отображения страницы профиля"""
        return self.is_element_visible(StellarBurgersLocators.PROFILE_PAGE_TITLE)

    @allure.step("Проверка отображения страницы истории заказов")
    def is_order_history_page_displayed(self):
        """Проверка отображения страницы истории заказов"""
        return self.is_element_visible(StellarBurgersLocators.ORDER_HISTORY_PAGE_TITLE)

    @allure.step("Получение имени пользователя")
    def get_profile_name(self):
        """Получение имени пользователя"""
        return self.get_attribute(StellarBurgersLocators.PROFILE_NAME_INPUT, "value")

    @allure.step("Получение email пользователя")
    def get_profile_email(self):
        """Получение email пользователя"""
        return self.get_attribute(StellarBurgersLocators.PROFILE_EMAIL_INPUT, "value")

    @allure.step("Проверка активности поля имени")
    def is_name_field_active(self):
        """Проверка активности поля имени"""
        return self.is_element_enabled(StellarBurgersLocators.PROFILE_NAME_INPUT)

    @allure.step("Проверка активности поля email")
    def is_email_field_active(self):
        """Проверка активности поля email"""
        return self.is_element_enabled(StellarBurgersLocators.PROFILE_EMAIL_INPUT)

    @allure.step("Проверка активности поля пароля")
    def is_password_field_active(self):
        """Проверка активности поля пароля"""
        return self.is_element_enabled(StellarBurgersLocators.PROFILE_PASSWORD_INPUT)