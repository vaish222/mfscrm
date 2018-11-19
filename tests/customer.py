import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class customer_test(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://foodserviceapp.herokuapp.com/accounts/login/")
        user = "instructor"
        pwd = "instructor1a"
        elem = self.driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = self.driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        # Click Login button
        elem = self.driver.find_element_by_xpath("/html/body/div/div/div/form/input[2]").click()
        print("Logged in")
        time.sleep(1)
        # Click View details under Customer
        elem = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a").click()
        time.sleep(1)

    def test_add_customer(self):
        driver = self.driver
        # Click Add Customer button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_cust_name")
        elem.send_keys("Vaishali Goel")

        elem = driver.find_element_by_id("id_organization")
        elem.send_keys("Capstone Inc.")

        elem = driver.find_element_by_id("id_role")
        elem.send_keys("Staff Assistant")

        elem = driver.find_element_by_id("id_bldgroom")
        elem.send_keys("PKI Room 260")

        elem = driver.find_element_by_id("id_account_number")
        elem.send_keys("100")

        elem = driver.find_element_by_id("id_address")
        elem.send_keys("12145 Stone dr.")

        elem = driver.find_element_by_id("id_city")
        elem.send_keys("Omaha")

        elem = driver.find_element_by_id("id_state")
        elem.send_keys("Nebraska")

        elem = driver.find_element_by_id("id_zipcode")
        elem.send_keys("67895")

        elem = driver.find_element_by_id("id_email")
        elem.send_keys("vg@unomaha.edu")

        elem = driver.find_element_by_id("id_phone_number")
        elem.send_keys("6784562345")

        # Click Save
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(1)
        print("Added Customer successfully")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)

    def test_delete_customer(self):
        driver = self.driver
        # Click Delete Customer button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[4]/td[13]/a").click()
        time.sleep(1)
        alert = driver.switch_to.alert
        alert.accept()
        print("alert accepted")
        time.sleep(1)
        print("Deleted Customer successfully")


    def test_edit_customer(self):
        driver = self.driver
        # Click Edit Customer button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[4]/td[12]/a").click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_organization")
        elem.clear()
        elem.send_keys("ABC Inc.")

        elem = driver.find_element_by_id("id_state")
        elem.clear()
        elem.send_keys("NE")

        elem = driver.find_element_by_id("id_zipcode")
        elem.clear()
        elem.send_keys("67896")

        elem = driver.find_element_by_id("id_phone_number")
        elem.clear()
        elem.send_keys("6784562378")

        # Click Update
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(1)
        print("Updated Customer successfully")


    def test_summary(self):
        driver = self.driver
        # Click Summary button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[1]/td[14]/a").click()
        time.sleep(1)
        print("Summary is shown successfully")

    @classmethod
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
