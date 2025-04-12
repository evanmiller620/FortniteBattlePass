from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "https://www.usnews.com/education/best-high-schools/california/districts/san-francisco-unified-school-district-111777"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

html_source = driver.page_source  # This is the rendered HTML
with open("test/high.html", "w", encoding="utf-8") as f:
    f.write(html_source)

driver.quit()
