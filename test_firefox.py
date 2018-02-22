import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class TestFirefox(unittest.TestCase):
    dc = {}
    testName = 'Selenium Test on Firefox'
    driver = None

    def setUp(self):
        self.dc['testName'] = self.testName
        self.dc['browserName'] = 'firefox'
        # Specify the access key in order to run this test against the browser Grid
        self.dc['accessKey'] = ''
        self.driver = webdriver.Remote('https://cloud.seetest.io/wd/hub', self.dc)

    def test_firefox(self):
        self.driver.get("https://seetest.io")
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[text()='Manual']")))

        manual_nav_link = self.driver.find_element_by_xpath("//*[text()='Manual']")
        manual_nav_link.click()

        automation_nav_link = self.driver.find_element_by_xpath("//*[text()='Automation']")
        automation_nav_link.click()

        webinar_footer_link = self.driver.find_element_by_xpath("//*[text()='Webinars']")
        webinar_footer_link.click()

        webinars_h2_title_text = self.driver.find_element_by_xpath("//h2[1]").text

        print("The title of the first h2 is: " + webinars_h2_title_text)

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
