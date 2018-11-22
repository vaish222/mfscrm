import unittest
from mfscrm.tests.addCustomerTest import addCustomerTest
from mfscrm.tests.editCustomerTest import editCustomerTest
from mfscrm.tests.deleteCustomerTest import deleteCustomerTest
from mfscrm.tests.deleteProductTest import deleteProductTest
from mfscrm.tests.deleteServiceTest import deleteServiceTest
from mfscrm.tests.editProductTest import editProductTest
from mfscrm.tests.editServiceTest import editServiceTest
from mfscrm.tests.addProductTest import addProductTest
from mfscrm.tests.addServiceTest import addServiceTest
from mfscrm.tests.summaryTest import summaryTest
from mfscrm.tests.readAndAddCustomers import readAndAddCustomerTest
from mfscrm.tests.customer import customer_test
from mfscrm.tests.loginAndLogoutTest import login_logoutTest


def suite_login_logout():
    suite = unittest.TestSuite()
    suite.addTest(login_logoutTest('test_login_logout'))
    return suite


def suite_customer():

    suite = unittest.TestSuite()
    suite.addTest(addCustomerTest('test_add_customer'))
    suite.addTest(editCustomerTest('test_edit_customer'))
    suite.addTest(deleteCustomerTest('test_delete_customer'))
    suite.addTest(summaryTest('test_summary'))
    return suite

def suite_service():
    suite = unittest.TestSuite()
    suite.addTest(addServiceTest('test_add_service'))
    suite.addTest(editServiceTest('test_edit_service'))
    suite.addTest(deleteServiceTest('test_delete_service'))
    return suite

def suite_product():
    suite = unittest.TestSuite()
    suite.addTest(addProductTest('test_add_product'))
    suite.addTest(editProductTest('test_edit_product'))
    suite.addTest(deleteProductTest('test_delete_product'))
    return suite

def suite_read_excel():
    suite = unittest.TestSuite()
    suite.addTest(readAndAddCustomerTest('test_read_add_customer'))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite_login_logout())
    runner.run(suite_customer())
    runner.run(suite_service())
    runner.run(suite_product())
    runner.run(suite_read_excel()) #to read data from excel file and upload

