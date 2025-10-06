from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import allure


class BasePage:
    """Базовый класс для всех Page Object классов"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

    @allure.step("Клик по элементу")
    def click_element(self, locator):
        """Клик по элементу с ожиданием"""
        try:
            modal = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'Modal_modal_opened')]")
            if modal:
                close_btn = self.driver.find_elements(By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
                if close_btn:
                    close_btn[0].click()
                    WebDriverWait(self.driver, 5).until(
                        EC.invisibility_of_element_located((By.XPATH, "//div[contains(@class, 'Modal_modal_opened')]"))
                    )
        except (TimeoutException, NoSuchElementException):
            pass
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Ввод текста в поле")
    def enter_text(self, locator, text):
        """Ввод текста в поле с ожиданием"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Получение текста элемента")
    def get_text(self, locator):
        """Получение текста элемента"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    @allure.step("Проверка видимости элемента")
    def is_element_visible(self, locator):
        """Проверка видимости элемента"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Проверка наличия элемента")
    def is_element_present(self, locator):
        """Проверка наличия элемента на странице"""
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Ожидание исчезновения элемента")
    def wait_for_element_to_disappear(self, locator):
        """Ожидание исчезновения элемента"""
        self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Наведение курсора на элемент")
    def hover_element(self, locator):
        """Наведение курсора на элемент"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.actions.move_to_element(element).perform()

    @allure.step("Получение атрибута элемента")
    def get_attribute(self, locator, attribute):
        """Получение атрибута элемента"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.get_attribute(attribute)

    @allure.step("Проверка активности элемента")
    def is_element_enabled(self, locator):
        """Проверка активности элемента"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.is_enabled()

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        """Получение текущего URL"""
        return self.driver.current_url

    @allure.step("Обновление страницы")
    def refresh_page(self):
        """Обновление страницы"""
        self.driver.refresh()

    @allure.step("Прокрутка к элементу")
    def scroll_to_element(self, locator):
        """Прокрутка к элементу"""
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.actions.move_to_element(element).perform()

    @allure.step("Ожидание появления модального окна")
    def wait_for_modal_to_appear(self, modal_locator):
        """Ожидание появления модального окна"""
        self.wait.until(EC.visibility_of_element_located(modal_locator))

    @allure.step("Клик за пределами модального окна")
    def click_outside_modal(self):
        """Клик за пределами модального окна для закрытия"""
        modal_overlay = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".Modal_modal_overlay__x2ZCr")))
        modal_overlay.click()

    @allure.step("Drag and drop элемента")
    def drag_and_drop(self, source_locator, target_locator):
        """Перетаскивание элемента"""
        source_element = self.wait.until(EC.element_to_be_clickable(source_locator))
        target_element = self.wait.until(EC.element_to_be_clickable(target_locator))
        self.actions.drag_and_drop(source_element, target_element).perform()

    @allure.step("Получение списка элементов")
    def get_elements_list(self, locator):
        """Получение списка элементов"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Ожидание текста в элементе")
    def wait_for_text_in_element(self, locator, text):
        """Ожидание появления текста в элементе"""
        self.wait.until(EC.text_to_be_present_in_element(locator, text))