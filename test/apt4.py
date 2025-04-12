import json
from bs4 import BeautifulSoup

def extract_listings_from_json_ld(html):
    # Parse the HTML
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find all <script> tags with type "application/ld+json"
    scripts = soup.find_all("script", type="application/ld+json")
    
    # Loop through all JSON-LD script tags to find the one that is a SearchResultsPage
    for script in scripts:
        try:
            # Load the JSON data from the script text
            data = json.loads(script.string)
        except Exception as e:
            # Skip if it's not valid JSON
            continue
        
        # Check if the top-level object is of type SearchResultsPage.
        # (Depending on the page, you might have multiple JSON-LD scripts.)
        if data.get("@type") == "SearchResultsPage":
            # Once we've found our SearchResultsPage, the listings are usually under the "about" key.
            return data.get("about", [])
    
    # Return an empty list if the data is not found
    return []

# Example usage:
if __name__ == "__main__":
    # Assume you have obtained the rendered HTML content from a headless browser.
    with open("test/apt2.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    
    listings = extract_listings_from_json_ld(html_content)
    
    print(f"Found {len(listings)} listings:")
    for listing in listings:
        name = listing.get("name", "N/A")
        url = listing.get("url", "N/A")
        image = listing.get("image", "N/A")
        telephone = listing.get("telephone", "N/A")
        
        # Address details are nested in the "Address" key
        address_info = listing.get("Address", {})
        street_address = address_info.get("streetAddress", "N/A")
        locality = address_info.get("addressLocality", "N/A")
        region = address_info.get("addressRegion", "N/A")
        postal_code = address_info.get("postalCode", "N/A")
        
        print(f"Name: {name}")
        print(f"URL: {url}")
        print(f"Image: {image}")
        print(f"Telephone: {telephone}")
        print(f"Address: {street_address}, {locality}, {region} {postal_code}")
        print("-" * 40)
