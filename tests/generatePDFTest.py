import unittest
import time
from selenium import webdriver


class generatePDFTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_generate_pdf(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/accounts/login/")
        time.sleep(3)
        # elem = driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div/p[2]/a[1]").click()
        # time.sleep(3)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        # Click Login button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/input[2]").click()
        print("Logged in")
        time.sleep(3)
        # Click View details under Customer
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a").click()
        time.sleep(5)
        # Click Generate PDF button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[1]/td[15]/a").click()
        time.sleep(3)
        print("PDF generated successfully")
        driver.get("http://127.0.0.1:8000")
        time.sleep(1)
        driver.get("http://127.0.0.1:8000")


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
