from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info(img_num=2):
    browser = init_browser()

    # Visit visitcostarica.herokuapp.com
    url = "https://visitcostarica.herokuapp.com/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the average temps
    temps_div = soup.find("div", id="weather")

    # Get the min avg temp
    min_temp = temps_div.find_all("strong")[0].text

    # Get the max avg temp
    max_temp = temps_div.find_all("strong")[1].text

    # BONUS: Find the src for the sloth image
    sloth_rel_path = soup.find_all("img")[img_num]["src"]
    sloth_img = url + sloth_rel_path

    # Store data in a dictionary
    costa_data = {
        "sloth_img": sloth_img,
        "min_temp": min_temp,
        "max_temp": max_temp
    }

    # Quite the browser after scraping
    browser.quit()

    # Return results
    return costa_data
