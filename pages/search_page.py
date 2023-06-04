import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class SearchFlightResults(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    log = Utils.customlogger()
    DIRECT_FLIGHT="(//div[contains(text(),'Stops')]/parent::div//input[@type='checkbox']/parent::label//span)[1]"
    ONE_STOP_FLIGHT ="(//div[contains(text(),'Stops')]/parent::div//input[@type='checkbox']/parent::label//span)[2]"
    TWO_STOP_FLIGHT ="(//div[contains(text(),'Stops')]/parent::div//input[@type='checkbox']/parent::label//span)[3]"
    STOPS_LIST="//*[contains(text(),'0 stop')]"

    def filter_flights(self,stop):
        self.click_element(By.XPATH, "(//div[contains(text(),'Stops')]/parent::div//input[@type='checkbox']/parent::label//span)["+stop+"]")

    def stops_list(self):
       Stops_list= self.wait_presence_of_all_elements_located(By.XPATH, self.STOPS_LIST)
       #self.log.info("list of flights found ", len(Stops_list))
       # print("list of flights found ***")
       # print(len(Stops_list))
       time.sleep(2)
       return Stops_list

