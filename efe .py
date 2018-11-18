from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest,time, re

class Efe(unittest.TestCase):
     def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
     def test_efe(self):
        driver = self.driver
        driver.get(self.base_url + "/search?q=%3A+http%3A%2F%2Fautomationpractice.com%2F+&ie=utf-8&oe=utf-8&client=firefox-b-ab")
        driver.find_element_by_css_selector("h3.LC20lb").click()
        driver.find_element_by_css_selector("a.login").click()
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("agaken4unow@gmail.com")
        driver.find_element_by_id("passwd").clear()
        driver.find_element_by_id("passwd").send_keys("master4u@")
        driver.find_element_by_id("SubmitLogin").click()
        # Warning: assertTextPresent may require manual changes
        self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"^[\s\S]*$")
        self.assertEqual("Efe Agadagba", driver.find_element_by_xpath(".//*[@id='header']//span[text()='Efe Agadagba']").text)
        driver.find_element_by_css_selector("a[title=\"View my shopping cart\"]").click()
        # Warning: assertTextPresent may require manual changes
        self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"^[\s\S]*$")
        self.assertEqual("WOMEN", driver.find_element_by_link_text("WOMEN").text)
        driver.find_element_by_link_text("Women").click()
        driver.find_element_by_css_selector("label[name=\"layered_id_attribute_group_24\"] > a").click()
        self.assertEqual("Product successfully added to your shopping cart", driver.find_element_by_css_selector("h2").text)
        driver.close()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        self.is_element_present(By.CSS_SELECTOR, "a[title=\"View my shopping cart\"]")
        self.assertEqual("Your shopping cart contains: 1 Product", driver.find_element_by_css_selector("span.heading-counter").text)
        driver.find_element_by_id("summary_products_quantity").click()
        driver.find_element_by_css_selector("li.sfHover > a.sf-with-ul").click()
         # Warning: assertTextPresent may require manual changes
        self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"^[\s\S]*[@id='center_column'\]/div\[1\]/div/div/span[\s\S]*$")
        Select(driver.find_element_by_id("selectProductSort")).select_by_visible_text("Price: Lowest first")
        driver.find_element_by_css_selector("option[value=\"price:asc\"]").click()
        Select(driver.find_element_by_id("selectProductSort")).select_by_visible_text("Price: Highest first")
        driver.find_element_by_css_selector("option[value=\"price:desc\"]").click()
         # Warning: assertTextPresent may require manual changes
        self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"^[\s\S]*\.//[\s\S]*\[@id='center_column'\]/div\[3\]/div\[2\]/div\[2\][\s\S]*$")


def is_element_present(self, how, what):
    try:
        self.driver.find_element(by=how, value=what)
    except NoSuchElementException as e:
        return False
    return True


def is_alert_present(self):
    try:
        self.driver.switch_to_alert()
    except NoAlertPresentException as e:
        return False
    return True


def close_alert_and_get_its_text(self):
    try:
        alert = self.driver.switch_to_alert()
        alert_text = alert.text
        if self.accept_next_alert:
            alert.accept()
        else:
            alert.dismiss()
        return alert_text
    finally:
        self.accept_next_alert = True


def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
