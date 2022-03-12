"""Template robot with Python."""


from RPA.Browser.Selenium import Selenium

browser = Selenium()

def open_worldometers_website():
    browser.open_headless_chrome_browser("https://www.worldometers.info/coronavirus/")
    browser.maximize_browser_window()

def click_USA():
    browser.scroll_element_into_view('USA')
    browser.click_link('USA')

def main():
    try:
        open_worldometers_website()
        click_USA()
        browser.capture_page_screenshot('Screenshot.png')
    finally:
        browser.close_all_browsers()

if __name__ == "__main__":
    main()