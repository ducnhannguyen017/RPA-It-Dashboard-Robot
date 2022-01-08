import datetime
from RPA.Browser.Selenium import Selenium


class GetAgencyDetail:
    BASE_URL = "https://itdashboard.gov/drupal/summary/005"

    def __init__(self):
        self.browser = Selenium()
        self.browser.open_available_browser(self.BASE_URL)
        self.run()

    def run(self):
        # self.browser.wait_until_element_is_visible(
        #     locator=[self.browser.find_element(
        #         'name:investments-table-object_length'), 'option:last-of-type'], timeout=datetime.timedelta(minutes=1))
        # self.browser.click_element(
        #     locator=[self.browser.find_element(
        #         'name:investments-table-object_length'), 'option:last-of-type'], timeout=datetime.timedelta(minutes=1))

        self.browser.wait_until_element_is_visible(
            locator='css:div#investments-table-widget div.pageSelect select option:last-of-type',
            timeout=datetime.timedelta(minutes=1)
        )
        self.browser.click_element(
            locator='css:div#investments-table-widget div.pageSelect select option:last-of-type'
        )
        self.browser.wait_until_element_is_visible(
            locator='css:div#investments-table-widget table#investments-table-object tbody tr:nth-of-type(11) td',
            timeout=datetime.timedelta(minutes=1)
        )
        agencies = self.browser.get_webelement(
            locator='css:div#investments-table-widget table#investments-table-object tbody tr'
        )
        print(agencies)
