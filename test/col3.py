from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Set up options to mimic a full browser
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless (you can remove this if you need to see the browser)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36")

# Create the driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=chrome_options)

# This script fixes a common Selenium detection issue:
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# Open the page and wait for it to load
driver.get("https://www.rentcafe.com/average-rent-market-trends/us/ca/san-francisco/")
time.sleep(5)  # Adjust waiting time if necessary

# Grab the page source
html_content = driver.page_source

# Parse with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
# print(soup.prettify())

with open("test/rents.html", "w", encoding="utf-8") as f:
    f.write(soup.prettify())

driver.quit()
