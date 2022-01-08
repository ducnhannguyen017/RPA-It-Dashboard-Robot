from RPA.Browser.Selenium import Selenium
from RPA.Excel.Files import Files
import datetime
from string import ascii_uppercase
import GetAgenciesInfo
import GetAgencyDetail


class RPARobot:

    def __init__(self):
        # self.GetAgenciesInfo = GetAgenciesInfo.GetAgenciesInfo()
        self.GetAgencyDetail = GetAgencyDetail.GetAgencyDetail()
