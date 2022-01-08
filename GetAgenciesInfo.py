from RPA.Browser.Selenium import Selenium
from RPA.Excel.Files import Files
import datetime
from string import ascii_uppercase


class GetAgenciesInfo:

    def __init__(self):
        self.URL = "https://itdashboard.gov/drupal/#home-dive-in"
        self.browser = Selenium()
        self.browser.open_available_browser(self.URL)
        self.excel = Files()
        self.run()

    def get_agencies_info(self):
        self.browser.wait_until_element_is_visible(
            locator='css:div#agency-tiles-2-widget>div>div>div>div>div>div')
        agencies = self.browser.get_webelements(
            locator='css:div#agency-tiles-2-widget>div>div>div>div>div>div')
        return agencies

    def run(self):
        self.excel.create_workbook("output/Agencies.xlsx")
        self.excel.rename_worksheet("Sheet", "Agencies")
        agencies = [
            {"id": "ID", "name": "Agency Name", "amount": "Amount"}]
        # self.set_header(agencies[0].values())
        for agency_element in self.get_agencies_info():
            self.browser.wait_until_element_is_visible(
                locator=[agency_element, 'css:div:nth-of-type(1)'])
            timeout = datetime.timedelta(minutes=1)
            info = self.browser.get_webelement(
                locator=[agency_element, 'css:div:nth-of-type(1)']).text.splitlines()
            id = self.browser.get_webelement(
                locator=[agency_element, 'css:a']).get_attribute('href').split("/")[-1]
            name = info[0]
            amount = info[2]

            # self.set_header(info.keys())
            agency = {
                'id': id,
                'name': name,
                'amount': amount,
            }
            agencies.append(agency)

        row_number = 1
        for agency in agencies:
            for num, val in enumerate(agencies[row_number-1].values()):
                self.excel.set_cell_value(
                    row_number, ascii_uppercase[num], val, "Agencies")
            row_number += 1
        self.excel.save_workbook()

        print(agencies)
        # return agencies
