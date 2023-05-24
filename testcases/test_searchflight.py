import time
import pytest
from pages.launch_page import LaunchPage
from ddt import ddt, data, file_data,unpack
from utilities.Utilities import Utils


@pytest.mark.usefixtures("setup")
@ddt
class TestFlightSearchAndVerify:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.util = Utils()

    @data(*Utils.read_data_from_csv("C://Users//anupam.chandan//Desktop//Python_Projects//PythonTestAutomationHybridFramework//testdata//testdata.csv"))
    @unpack
    def test_search_flights(self,goingfrom,goingto,date,stops):
        # sf = SearchFlightResults(self.driver)
        search_flight_results= self.lp.searchFlights(goingfrom,goingto,date)
        #lp.page_scroll()
        time.sleep(20)
        search_flight_results.filter_flights(stops)
        time.sleep(10)
        all_stops= search_flight_results.stops_list()
        self.util.assertListItemsText(all_stops,"1 stop")
        time.sleep(10)

    # def test_search_flights(self):
    #     # sf = SearchFlightResults(self.driver)
    #     search_flight_results= self.lp.searchFlights("New Delhi","Mumbai", "Tue May 23 2023")
    #     #lp.page_scroll()
    #     time.sleep(20)
    #     search_flight_results.filter_flights("3")
    #     time.sleep(10)
    #     all_stops= search_flight_results.stops_list()
    #     self.util.assertListItemsText(all_stops,"1 stop")
    #     time.sleep(10)








