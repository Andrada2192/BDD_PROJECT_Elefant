from selenium import webdriver


class Browser:

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)


    def close(self):
        self.driver.quit()