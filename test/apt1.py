from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "https://www.apartments.com/san-francisco-ca/?bb=w1539yyq0O91mg-jE"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

html_source = driver.page_source  # This is the rendered HTML
with open("test/apt1.html", "w", encoding="utf-8") as f:
    f.write(html_source)

driver.quit()
