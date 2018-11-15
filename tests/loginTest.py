import unittest
import time
from selenium import webdriver


class loginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://foodserviceapp.herokuapp.com/")
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
        # time.sleep(3)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        # Click Login button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/input[2]").click()
        print("Logged in")
        time.sleep(1)
        #print("Logged in successfully")
        # driver.get("http://127.0.0.1:8000")
        # time.sleep(1)
        # driver.get("http://127.0.0.1:8000")


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
