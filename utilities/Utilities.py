import re
import logging
import csv

class Utils():

    def assertListItemsText(self, stopsList,expectedVal):
        for stops in stopsList:
            print("Stop is : " + stops.text)
            assert re.search(expectedVal, stops.text)
            print("assert pass")

    def customlogger(loglevel=logging.DEBUG):
        logger= logging.getLogger(__name__)
        logger.setLevel(loglevel)
        ch=logging.StreamHandler()
        fh = logging.FileHandler("executionlog.log")
        formatter=logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        logger.addHandler(ch)
        logger.addHandler(fh)
        return logger

    def read_data_from_csv(filename):
        datalist=[]
        csvdata=open(filename, 'r')
        reader = csv.reader(csvdata)
        next(reader) #Skip header
        for rows in reader:
            datalist.append(rows)
        print(datalist)
        return datalist



