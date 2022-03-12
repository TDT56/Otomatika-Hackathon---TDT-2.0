"""Template robot with Python."""


from RPA.Browser.Selenium import Selenium

browser = Selenium()

def open_the_website(url):

    browser.open_chrome_browser(url)

def main():
    try:
        open_the_website("https://www.worldometers.info/coronavirus/")
    finally:
        browser.close_all_browsers()

if __name__ == "__main__":
    main()