class Helper:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url
