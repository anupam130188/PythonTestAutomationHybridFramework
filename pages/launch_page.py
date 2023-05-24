import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.search_page import SearchFlightResults
from utilities.Utilities import Utils

class LaunchPage(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        #self.wait = wait

    CLICK_POPUP="//span[@class='logSprite icClose']"
    DEPART_FROM_FIELD="(//p[contains(text(),'Enter city or airport')])[1]"
    DEPART_FROM="//span[contains(text(),'From')]/parent::div//input"
    GOING_TO="//span[contains(text(),'To')]//..//input[@type='text']"

    log =Utils.customlogger()
    def getDepartFieldFrom(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.DEPART_FROM_FIELD)

    def getGoingTo(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.GOING_TO)

    def getDepartFrom(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.DEPART_FROM)

    def departfromibibo(self,departfrom):
        self.jsclick_element(By.XPATH,self.CLICK_POPUP)
        self.getDepartFieldFrom().click()
        self.getDepartFrom().send_keys(departfrom)
        self.getDepartFrom().send_keys(Keys.ENTER)

    def goingtoibibo(self,goingto):
        self.getGoingTo().click()
        self.getGoingTo().send_keys(goingto)
        self.getGoingTo().send_keys(Keys.ENTER)


    def selectdateibibo(self, selectdate):
        self.wait_element_to_be_clickable(By.XPATH, "//div[@class='DayPicker']").click()
        all_dates = self.wait_element_to_be_clickable(By.XPATH, "//div[contains(text(),'May 2023')]/ancestor::div[@class='DayPicker-Month']//div[@class='DayPicker-Day']") \
            .find_elements(By.XPATH, "//div[contains(text(),'May 2023')]/ancestor::div[@class='DayPicker-Month']//div[@class='DayPicker-Day']")
        self.log.info(str(all_dates))
        for date in all_dates:
            self.log.info(date)
            if date.get_attribute("aria-label") == selectdate:
                date.click()
                break
        self.wait_element_to_be_clickable(By.XPATH, "//span[@class ='fswTrvl__done']").click()
        time.sleep(1)
        self.wait_element_to_be_clickable(By.XPATH, "//a[contains(text(),'Done')]").click()
        time.sleep(1)

    def searchflightsibibo(self):
            self.click_element(By.XPATH, "//span[contains(text(),'SEARCH FLIGHTS')]")
            time.sleep(1)
    def searchFlights(self,goingfrom,goingto,date):
        self.departfromibibo(goingfrom)
        self.goingtoibibo(goingto)
        self.selectdateibibo(date)
        self.searchflightsibibo()
        search_flight_results= SearchFlightResults(self.driver)
        return search_flight_results


    # def departfrom(self,departfrom):
    #     #depart_from = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']")))
    #     time.sleep(2)
    #     depart_from = self.wait_element_to_be_clickable(By.XPATH, "//input[@id='BE_flight_origin_city']")
    #     depart_from.click()
    #     time.sleep(2)
    #     #depart_from.send_keys(departfrom)
    #     depart_from.send_keys(Keys.ENTER)
    #     time.sleep(2)
    #
    # def goingto(self,goingto):
    #     going_to = self.wait_element_to_be_clickable(By.XPATH, "//input[@id='BE_flight_arrival_city']")
    #     going_to.click()
    #     time.sleep(2)
    #     going_to.send_keys(goingto)
    #     time.sleep(2)
    #     going_to.send_keys(Keys.ENTER)
    #     time.sleep(2)
    #     # search_results=self.wait_presence_of_all_elements_located(By.XPATH,"//div[@class='viewport']")
    #     # #
    #     # for results in search_results:
    #     #      if "New York (JFK)" in results.text:
    #     #          results.click()
    #     #          break
    #     time.sleep(2)
    #
    #
    #
    # def selectdate(self, selectdate):
    #     self.wait_element_to_be_clickable(By.XPATH, "//input[@id='BE_flight_origin_date']").click()
    #     all_dates = self.wait_element_to_be_clickable(By.XPATH, "//div[@class='month-wrapper']//tbody//tr//td[@class!='inActiveTD']") \
    #         .find_elements(By.XPATH, "//div[@class='month-wrapper']//tbody//tr//td[@class!='inActiveTD']")
    #     for date in all_dates:
    #         if date.get_attribute("data-date") == selectdate:
    #             date.click()
    #             break
    #     time.sleep(4)
    #
    # def searchflights(self):
    #     self.click_element(By.XPATH,"//input[@value='Search Flights']")
    #     print(self.driver.title)
    #     #self.driver.find_element(By.XPATH, "//input[@value='Search Flights']")
    #     time.sleep(4)