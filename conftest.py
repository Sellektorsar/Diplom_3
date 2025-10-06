import pytest
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utils.api_client import APIClient
import allure


def pytest_addoption(parser):
    """Добавление опций командной строки для выбора браузера"""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Браузер для тестирования: chrome или firefox"
    )


@pytest.fixture(scope="session")
def api_client():
    """Фикстура для API клиента"""
    client = APIClient()
    yield client
    client.close()


@pytest.fixture
def driver(request):
    """Фикстура для WebDriver"""
    browser_name = request.config.getoption("--browser")

    if browser_name == "chrome":
        options = ChromeOptions()
        # Временно отключаем headless для анализа структуры сайта
        # options.add_argument("--headless")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-extensions")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        # options.add_argument("--headless")  # Headless режим
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Неподдерживаемый браузер: {browser_name}")

    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def test_user(api_client):
    """Фикстура для создания тестового пользователя"""
    # Генерация уникальных данных для пользователя
    unique_id = str(uuid.uuid4())[:8]
    email = f"test_{unique_id}@example.com"
    password = "test_password_123"
    name = f"TestUser_{unique_id}"

    # Создание пользователя
    response = api_client.create_user(email, password, name)

    if response.get("success"):
        user_data = response["user"]
        access_token = response["accessToken"]
        refresh_token = response["refreshToken"]

        yield {
            "email": email,
            "password": password,
            "name": name,
            "access_token": access_token,
            "refresh_token": refresh_token
        }

        # Очистка - удаление пользователя после теста
        try:
            api_client.delete_user(access_token)
        except Exception:
            pass  # Игнорируем ошибки при удалении
    else:
        pytest.skip(f"Не удалось создать пользователя: {response.get('message')}")


@pytest.fixture
def test_ingredients(api_client):
    """Фикстура для получения ингредиентов"""
    response = api_client.get_ingredients()

    if response.get("success"):
        ingredients = response["data"]
        return ingredients
    else:
        pytest.skip("Не удалось получить ингредиенты")


@pytest.fixture(autouse=True)
def attach_screenshot_on_failure(request, driver):
    """Автоматическое прикрепление скриншота при падении теста"""
    def fin():
        if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )
    request.addfinalizer(fin)


@pytest.fixture
def random_order_data(test_ingredients, api_client, test_user):
    """Фикстура для создания случайного заказа"""
    # Выбираем случайные ингредиенты для заказа
    ingredients = test_ingredients[:3]  # Берем первые 3 ингредиента
    ingredient_ids = [ing["_id"] for ing in ingredients]

    # Создаем заказ
    response = api_client.create_order(ingredient_ids, test_user["access_token"])

    if response.get("success"):
        order_data = {
            "ingredients": ingredient_ids,
            "order_number": response["order"]["number"],
            "order_id": response["order"]["_id"] if "_id" in response["order"] else None
        }
        return order_data
    else:
        pytest.skip(f"Не удалось создать заказ: {response.get('message')}")


def pytest_configure(config):
    """Настройка метаданных для Allure"""
    # Метаданные будут добавлены через allure decorators в тестах
    pass


def pytest_collection_modifyitems(config, items):
    """Добавление маркеров к тестам"""
    for item in items:
        # Добавляем маркер для браузера
        browser_marker = config.getoption("--browser")
        item.add_marker(pytest.mark.browser(browser_marker))

        # Добавляем маркер для UI тестов
        item.add_marker(pytest.mark.ui)