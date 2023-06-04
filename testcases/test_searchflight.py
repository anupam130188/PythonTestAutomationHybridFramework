import time
import unittest
from unittest import TestCase
import pytest
from base import loguru_logging
from pages.launch_page import LaunchPage
from ddt import ddt, data, unpack
from utilities.utils import Utils

#logging.basicConfig(level=logging.DEBUG)
#mylogger = logging.getLogger()
@pytest.mark.usefixtures("setup")
@ddt
class TestFlightSearchAndVerify(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.util = Utils()

    @data(*Utils.read_data_from_csv("C:\\Users\\anupam.chandan\\Desktop\\Python_Projects\\PythonTestAutomationHybridFramework\\testdata\\testdata.csv"))
    #@data(("BOM", "New Delhi", "Thu Jun 08 2023","2"))
    @unpack
    def test_search_flights(self,goingfrom,goingto,date,stops):
        # sf = SearchFlightResults(self.driver)
        #print("printing data ", goingfrom,goingto,date,stops)
        #loguru_logging.func('Inside Setup1')
        search_flight_results= self.lp.searchFlights(goingfrom,goingto,date)
        #loguru_logging.func('Inside Setup2')
        #search_flight_results = self.lp.searchFlights("BOM", "New Delhi", "Thu Jun 08 2023")
        #lp.page_scroll()
        time.sleep(10)
        search_flight_results.filter_flights(stops)
        #loguru_logging.func('Inside Setup3')
        time.sleep(20)
        #self.lp.page_scroll()
        all_stops= search_flight_results.stops_list()
        self.util.assertListItemsText(all_stops,"0 stop")
        time.sleep(10)

    def test_search_text(self):
       # sf = SearchFlightResults(self.driver)
       #loguru_logging.func('Inside Setup5')
       print("Hello Python")








