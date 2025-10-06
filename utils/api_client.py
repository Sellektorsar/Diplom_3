import requests
import allure
from typing import Dict, Any


class APIClient:
    """Клиент для работы с API Stellar Burgers"""

    BASE_URL = "https://stellarburgers.nomoreparties.site/api"

    def __init__(self):
        self.session = requests.Session()

    @allure.step("Создание пользователя")
    def create_user(self, email: str, password: str, name: str) -> Dict[str, Any]:
        """Создание нового пользователя"""
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        response = self.session.post(f"{self.BASE_URL}/auth/register", json=payload)
        return response.json()

    @allure.step("Авторизация пользователя")
    def login_user(self, email: str, password: str) -> Dict[str, Any]:
        """Авторизация пользователя"""
        payload = {
            "email": email,
            "password": password
        }
        response = self.session.post(f"{self.BASE_URL}/auth/login", json=payload)
        return response.json()

    @allure.step("Удаление пользователя")
    def delete_user(self, access_token: str) -> Dict[str, Any]:
        """Удаление пользователя"""
        headers = {"Authorization": access_token}
        response = self.session.delete(f"{self.BASE_URL}/auth/user", headers=headers)
        return response.json()

    @allure.step("Восстановление пароля")
    def reset_password(self, email: str) -> Dict[str, Any]:
        """Запрос на восстановление пароля"""
        payload = {"email": email}
        response = self.session.post(f"{self.BASE_URL}/password-reset", json=payload)
        return response.json()

    @allure.step("Сброс пароля")
    def confirm_reset_password(self, password: str, token: str) -> Dict[str, Any]:
        """Подтверждение сброса пароля"""
        payload = {
            "password": password,
            "token": token
        }
        response = self.session.post(f"{self.BASE_URL}/password-reset/reset", json=payload)
        return response.json()

    @allure.step("Получение ингредиентов")
    def get_ingredients(self) -> Dict[str, Any]:
        """Получение списка ингредиентов"""
        response = self.session.get(f"{self.BASE_URL}/ingredients")
        return response.json()

    @allure.step("Создание заказа")
    def create_order(self, ingredients: list, access_token: str = None) -> Dict[str, Any]:
        """Создание заказа"""
        payload = {"ingredients": ingredients}
        headers = {}
        if access_token:
            headers["Authorization"] = access_token

        response = self.session.post(f"{self.BASE_URL}/orders", json=payload, headers=headers)
        return response.json()

    @allure.step("Получение заказов пользователя")
    def get_user_orders(self, access_token: str) -> Dict[str, Any]:
        """Получение заказов пользователя"""
        headers = {"Authorization": access_token}
        response = self.session.get(f"{self.BASE_URL}/orders", headers=headers)
        return response.json()

    @allure.step("Получение всех заказов")
    def get_all_orders(self) -> Dict[str, Any]:
        """Получение всех заказов"""
        response = self.session.get(f"{self.BASE_URL}/orders/all")
        return response.json()

    @allure.step("Обновление токена")
    def refresh_token(self, refresh_token: str) -> Dict[str, Any]:
        """Обновление токена доступа"""
        payload = {"token": refresh_token}
        response = self.session.post(f"{self.BASE_URL}/auth/token", json=payload)
        return response.json()

    @allure.step("Выход из системы")
    def logout_user(self, refresh_token: str) -> Dict[str, Any]:
        """Выход пользователя из системы"""
        payload = {"token": refresh_token}
        response = self.session.post(f"{self.BASE_URL}/auth/logout", json=payload)
        return response.json()

    @allure.step("Получение данных пользователя")
    def get_user_info(self, access_token: str) -> Dict[str, Any]:
        """Получение информации о пользователе"""
        headers = {"Authorization": access_token}
        response = self.session.get(f"{self.BASE_URL}/auth/user", headers=headers)
        return response.json()

    @allure.step("Обновление данных пользователя")
    def update_user_info(self, access_token: str, **kwargs) -> Dict[str, Any]:
        """Обновление информации о пользователе"""
        headers = {"Authorization": access_token}
        payload = {k: v for k, v in kwargs.items() if v is not None}
        response = self.session.patch(f"{self.BASE_URL}/auth/user", json=payload, headers=headers)
        return response.json()

    def close(self):
        """Закрытие сессии"""
        self.session.close()