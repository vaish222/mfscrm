import unittest
import time
from selenium import webdriver


class editServiceTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_edit_service(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://foodserviceapp.herokuapp.com/accounts/login/")
        time.sleep(1)
        # elem = driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div/p[2]/a[1]").click()
        # time.sleep(3)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        # Click Login button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/input[2]").click()
        print("Logged in")
        time.sleep(1)
        # Click View details under Service
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[2]/div/div/p[2]/a").click()
        time.sleep(1)
        # Click Edit Service button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[6]/td[8]/a").click()
        time.sleep(2)
        # elem = driver.find_element_by_id("id_cust_name")
        # elem.send_keys("Barbara York")
        # time.sleep(1)
        # elem = driver.find_element_by_id("id_product")
        # elem.send_keys("Box Lunch - Turkey on Wheat")
        # time.sleep(1)
        # elem = driver.find_element_by_id("id_p_description")
        # elem.send_keys("Box Lunch - Turkey on Wheat bread. Apple or Orange and Chips Cookie")
        # time.sleep(1)
        elem = driver.find_element_by_id("id_location")
        elem.clear()
        elem.send_keys("PKI Room 271")

        # elem = driver.find_element_by_id("id_pickup_time")
        # elem.send_keys("2018-11-09 17:31:26")
        # time.sleep(1)
        elem = driver.find_element_by_id("id_service_charge")
        elem.clear()
        elem.send_keys("270")

        # Click Update
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(2)
        print("Updated Service successfully")
        # driver.get("http://127.0.0.1:8000")
        # time.sleep(1)
        # driver.get("http://127.0.0.1:8000")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
