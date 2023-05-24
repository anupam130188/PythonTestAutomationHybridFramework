import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self,driver):
        self.driver = driver

    def page_scroll(self):
            # pageLength = self.driver.execute_script(
            #     "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
            # match = False
            # while (match == False):
            #     lastCount = pageLength
            #     time.sleep(1)
            #     pageLength = self.driver.execute_script(
            #         "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
            #     if lastCount == pageLength:
            #         match = True

            SCROLL_PAUSE_TIME = 3

            # Get scroll height
            last_height = self.driver.execute_script("return document.body.scrollHeight")

            while True:
                # Scroll down to bottom
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                # Wait to load page
                time.sleep(SCROLL_PAUSE_TIME)

                # Calculate new scroll height and compare with last scroll height
                new_height = self.driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
            time.sleep(4)

    def wait_presence_of_all_elements_located(self,locator_type, locator):
        wait=WebDriverWait(self.driver,10)
        list_of_elements = all_stops = wait.until(EC.presence_of_all_elements_located((locator_type,locator)))
        return list_of_elements

    def wait_element_to_be_clickable(self,locator_type, locator):
        #all_stops = self.wait.until(EC.presence_of_all_elements_located(By.XPATH, "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop')]"))
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type,locator )))
        time.sleep(1)
        return element

    def click_element(self,locator_type, locator):
       wait = WebDriverWait(self.driver, 10)
       wait.until(EC.element_to_be_clickable((locator_type, locator))).click()

    def jsclick_element(self, locator_type, locator):
           wait = WebDriverWait(self.driver, 10)
           # element = self.click_element(By.XPATH, "//p[@class='font-lightgrey bold'][normalize-space()=1]")
           b = wait.until(EC.element_to_be_clickable((locator_type, locator)))
           self.driver.execute_script("arguments[0].click();", b)
           time.sleep(1)





