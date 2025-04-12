from bs4 import BeautifulSoup
import json

def extract_listings_with_rent(html):
    soup = BeautifulSoup(html, 'html.parser')
    listings = []
    
    # Look for all article tags with the class "placard" (which represent listings)
    for article in soup.find_all('article', class_='placard'):
        # Extract the listing URL from a data-attribute (if provided)
        url = article.get("data-url", "N/A")
        
        # Extract the listing name
        title_elem = article.select_one(".js-placardTitle.propertyTitle")
        name = title_elem.get_text(strip=True) if title_elem else "N/A"
        
        # Extract the rent value. In many cases, the rent is in an element with class "priceRange"
        price_elem = article.find(class_="priceRange")
        rent = price_elem.get_text(strip=True) if price_elem else "N/A"
        
        # (Optional) Extract the telephone if available; sometimes it may be stored in a data attribute.
        telephone = article.get("data-telephone", "N/A")
        # If telephone info is not available on the article tag, you could search for it within the article:
        if telephone == "N/A":
            tel_elem = article.find(lambda tag: tag.name in ['span', 'div'] and 'Call' in tag.get_text())
            if tel_elem:
                telephone = tel_elem.get_text(strip=True)
        
        # Similarly, you can extract additional info such as address:
        address_elem = article.select_one(".propertyAddress")
        address = address_elem.get_text(strip=True) if address_elem else "N/A"
        
        listings.append({
            "name": name,
            "url": url,
            "rent": rent,
            "telephone": telephone,
            "address": address,
        })
    return listings

if __name__ == "__main__":
    # Read the rendered HTML from a file (or you can use the HTML obtained from Playwright)
    with open("test/apt2.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    
    listings = extract_listings_with_rent(html_content)
    
    print(f"Found {len(listings)} listings:")

    apt_data = {"apts" : []}

    for listing in listings:
        apt_data["apts"].append(listing)

    with open("apt.json", "w") as file:
        json.dump(apt_data, file, indent=4)
    # for listing in listings:
    #     print("Name: ", listing["name"])
    #     print("URL: ", listing["url"])
    #     print("Rent: ", listing["rent"])
    #     print("Telephone: ", listing["telephone"])
    #     print("Address: ", listing["address"])
    #     print("-" * 40)
