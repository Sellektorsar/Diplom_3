from selenium.webdriver.common.by import By


class StellarBurgersLocators:
    """Класс с локаторами для всех элементов сайта Stellar Burgers"""

    # Главная страница - обновленные локаторы на основе реальной структуры
    MAIN_PAGE_CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
    MAIN_PAGE_ORDER_FEED_LINK = (By.XPATH, "//p[text()='Лента Заказов']")
    MAIN_PAGE_PROFILE_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")

    # Кнопки входа и регистрации
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    REGISTER_BUTTON = (By.XPATH, "//a[text()='Зарегистрироваться']")
    RECOVER_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")

    # Форма входа - локаторы для модальных окон и динамического контента
    LOGIN_EMAIL_INPUT = (By.XPATH, "(//input[@type='text'])[1]")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")

    # Форма регистрации
    REGISTER_NAME_INPUT = (By.XPATH, "(//input[@type='text'])[1]")
    REGISTER_EMAIL_INPUT = (By.XPATH, "(//input[@type='text'])[2]")
    REGISTER_PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    REGISTER_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    REGISTER_LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")

    # Восстановление пароля
    RECOVER_EMAIL_INPUT = (By.XPATH, "(//input[@type='text'])[1]")
    RECOVER_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    RECOVER_LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")

    # Страница восстановления пароля
    RESET_PASSWORD_INPUT = (By.XPATH, "(//input[@type='password'])[1]")
    RESET_TOKEN_INPUT = (By.XPATH, "(//input[@type='text'])[1]")
    RESET_SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")
    RESET_SHOW_PASSWORD_BUTTON = (By.CSS_SELECTOR, ".input__icon")

    # Личный кабинет
    PROFILE_NAME_INPUT = (By.XPATH, "(//input[@type='text'])[1]")
    PROFILE_EMAIL_INPUT = (By.XPATH, "(//input[@type='text'])[2]")
    PROFILE_PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    PROFILE_SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")
    PROFILE_CANCEL_BUTTON = (By.XPATH, "//button[text()='Отмена']")
    PROFILE_LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    PROFILE_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")

    # Конструктор бургера - обновленные локаторы
    CONSTRUCTOR_BUN_TAB = (By.XPATH, "//span[text()='Булки']")
    CONSTRUCTOR_SAUCE_TAB = (By.XPATH, "//span[text()='Соусы']")
    CONSTRUCTOR_FILLING_TAB = (By.XPATH, "//span[text()='Начинки']")
    CONSTRUCTOR_INGREDIENT = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]")
    CONSTRUCTOR_INGREDIENT_COUNTER = (By.XPATH, "//p[contains(@class, 'counter_counter__num')]")
    CONSTRUCTOR_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")

    # Модальное окно ингредиента
    INGREDIENT_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal')]")
    INGREDIENT_MODAL_CLOSE_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal')]//button[contains(@class, 'Modal_modal__close')]")
    INGREDIENT_MODAL_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")

    # Лента заказов - локаторы для динамического контента
    ORDER_FEED_CONTAINER = (By.XPATH, "//main")
    ORDER_FEED_ORDER = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]")
    ORDER_FEED_ORDER_NUMBER = (By.XPATH, "//p[contains(@class, 'text_type_digits')]")
    ORDER_FEED_DONE_ORDERS = (By.XPATH, "//div[contains(@class, 'OrderFeed_orderListReady')]//li")
    ORDER_FEED_TOTAL_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    ORDER_FEED_TOTAL_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")

    # Модальное окно заказа
    ORDER_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal')]")
    ORDER_MODAL_CLOSE_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal')]//button[contains(@class, 'Modal_modal__close')]")
    ORDER_MODAL_ORDER_NUMBER = (By.XPATH, "//section[contains(@class, 'Modal_modal')]//h2")

    # Рабочая область заказа
    ORDER_WORKSPACE = (By.CSS_SELECTOR, ".BurgerConstructor_basket__container")
    ORDER_IN_WORK = (By.XPATH, "//div[contains(@class, 'OrderFeed_orderListReady')]//li")

    # Заголовки страниц
    PROFILE_PAGE_TITLE = (By.XPATH, "//a[contains(@class, 'Account_link') and contains(@class, 'Account_link_active')]")
    ORDER_FEED_PAGE_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    ORDER_HISTORY_PAGE_TITLE = (By.XPATH, "//a[contains(@class, 'Account_link') and contains(@class, 'Account_link_active')]")

    # Сообщения об ошибках
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".input__error")
    REQUIRED_FIELD_ERROR = (By.XPATH, "//p[text()='Обязательное поле']")

    # Дополнительные локаторы для динамического контента
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
    CONSTRUCTOR_DROP_ZONE = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list')]")
    ORDER_TOTAL_PRICE = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket__totalContainer')]//p")