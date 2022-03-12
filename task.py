"""Template robot with Python."""


from RPA.Browser.Selenium import Selenium

browser = Selenium()

def open_worldometers_website():
    browser.open_available_browser("https://covid19.who.int/")

def click_Data_Table():
    browser.click_link('Data Table')

def main():
    try:
        open_worldometers_website()
        click_Data_Table()
        browser.wait_until_page_contains('Situation by Region, Country, Territory & Area')
        browser.capture_page_screenshot('Screenshot2.png')
        #browser.capture_page_screenshot
        #USA_table_contents = browser.get_element_attribute('usa_table_countries_today', 'outerHTML')
        #print(USA_table_contents)
    finally:
        browser.close_all_browsers()

if __name__ == "__main__":
    main()