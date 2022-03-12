"""Template robot with Python."""


from RPA.Browser.Selenium import Selenium

browser = Selenium()

def open_worldometers_website():
    browser.open_chrome_browser("https://www.worldometers.info/coronavirus/")

def click_USA():
    browser.click_link('USA')

def main():
    try:
        open_worldometers_website()
        click_USA()
    finally:
        browser.close_all_browsers()

if __name__ == "__main__":
    main()