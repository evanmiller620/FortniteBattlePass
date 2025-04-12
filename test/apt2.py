from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def scrape_apartments(search_url):
    # 1) Set up Chrome in headless mode (so it doesn't open a visible browser)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)

    # 2) Go to the target Apartments.com page
    driver.get(search_url)

    # 3) Wait briefly to let JS load listings
    time.sleep(5)  # Might increase if your connection is slow

    # 4) Locate the containers for the listings.
    #    The exact selectors may change over time, so you have to inspect in dev tools.
    #    Here is a generic example:
    listings = driver.find_elements(By.CSS_SELECTOR, "li.mortar-wrapper")

    # 5) Parse each listing
    results = []
    for listing in listings:
        try:
            # Example selectors:
            # Title/Name might be in an <a> with a data-tid or unique class
            # Price might be in <span> or <div> with a known class
            title_element = listing.find_element(By.CSS_SELECTOR, "a.property-link")
            price_element = listing.find_element(By.CSS_SELECTOR, "span.property-pricing")

            title = title_element.text.strip()
            price = price_element.text.strip()

            # Optionally, you might also find address, phone, bed/bath, etc.
            # address_element = listing.find_element(By.CSS_SELECTOR, "div.property-address")
            # address = address_element.text.strip()

            # Add to results
            results.append({
                "title": title,
                "price": price,
                # "address": address,
            })

        except Exception as e:
            # If any of the selectors fail, handle or skip
            print(f"Skipping one listing due to error: {e}")

    driver.quit()
    return results

if __name__ == "__main__":
    # Replace with the Apartments.com URL you want, e.g.:
    url = "https://www.apartments.com/san-francisco-ca/"
    data = scrape_apartments(url)
    for d in data:
        print(d)
