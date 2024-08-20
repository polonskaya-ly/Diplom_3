from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self, base_url):
        return self.driver.get(base_url)

    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    def wait_for_element_presented(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_not_presented(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_for_element_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
