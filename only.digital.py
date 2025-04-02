import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class FooterSearchTest(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_should_find_footer_element(self):
        self.driver.get("https://only.digital")
        footer = self.driver.find_element(By.XPATH, "//*[@class='text2 Footer_text___ATim']")
        delta_y = footer.location['y']
        ActionChains(self.driver).move_to_element(footer).perform()

        actual = footer.text
        expected = "Создаем digital-продукт на базе\nстратегии, креатива и технологий"
        self.assertEqual(expected, actual)

    def test_should_find_company_presentation(self):
        self.driver.get("https://only.digital")
        footer_elements = self.driver.find_elements(By.XPATH, "//*[@class='captions Documents_documentsDescription__ARJsa']")
        company_presentation = footer_elements[1]
        delta_y = company_presentation.location['y']
        ActionChains(self.driver).move_to_element(company_presentation).perform()

        actual = company_presentation.text
        expected = "презентация \nкомпании"
        self.assertEqual(expected, actual)
if __name__ == "__main__":
    unittest.main()