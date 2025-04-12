from playwright.sync_api import sync_playwright

def scrape_apartment_listings(url):
    with sync_playwright() as p:
        # Launch the browser (start with headless=False for debugging)
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.110 Safari/537.36"
        )
        page = context.new_page()

        # Navigate to the URL and wait until network is idle,
        # meaning most XHR/JS has been completed.
        page.goto(url, wait_until="networkidle")

        # Wait for the apartment listings container to be visible.
        # (Update the selector below based on what you see on the page.)
        listings_container_selector = "div.placardContainer"
        page.wait_for_selector(listings_container_selector, timeout=30000)

        # Now select each listing element.
        # Update ".placard" to the correct class/selector for individual listings.
        listings = page.query_selector_all(f"{listings_container_selector} div.placard")
        print(f"Found {len(listings)} listings.")

        # Loop through listings and extract details.
        for listing in listings:
            try:
                # Replace these with the actual selectors for your listing title, price, etc.
                title_el = listing.query_selector("h2.placardTitle")
                price_el = listing.query_selector("div.placardPrice")

                title = title_el.inner_text().strip() if title_el else "No title"
                price = price_el.inner_text().strip() if price_el else "No price info"

                print("Listing:", title, "—", price)
            except Exception as e:
                print("Error parsing a listing:", e)

        browser.close()

if __name__ == "__main__":
    url = "https://www.apartments.com/san-francisco-ca/"
    scrape_apartment_listings(url)
