import requests
from bs4 import BeautifulSoup
import csv
import time

def scrape_table_from_url(page_url, timeout=10):
    """
    Returns a list of rows from the first <table> on page_url.
    Each row is a list of cell texts (header or data).
    If no table is found, returns an empty list.
    """
    response = requests.get(page_url, timeout=timeout)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    tables = soup.find_all("table")
    if not tables:
        return []  # No tables found on this page

    # Let's just grab the first table for demonstration
    table = tables[0]
    rows = table.find_all("tr")
    
    table_data = []
    for row in rows:
        cells = row.find_all(["th", "td"])
        cell_texts = [cell.get_text(strip=True) for cell in cells]
        table_data.append(cell_texts)
    
    time.sleep(5)

    return table_data

def main():
    # 1. Grab the main "neighborhoods" page
    main_url = "https://www.civichub.us/ca/san-francisco/gov/police-department/crime-data/neighborhoods"
    response = requests.get(main_url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # 2. Find all <a> tags with class "ui-accordion-content" (the neighborhood links)
    links = soup.find_all("a", class_="ui-accordion-content", href=True)
    hrefs = [link["href"] for link in links]

    # 3. Open CSV file for writing
    with open("crime_data_all_neighborhoods.csv", "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        header_written = False

        # 4. Iterate over each link and scrape
        for link_url in hrefs:
            print(f"Scraping table from: {link_url}")

            try:
                table_data = scrape_table_from_url(link_url, timeout=15)
            except requests.exceptions.RequestException as e:
                print(f"Error fetching {link_url}: {e}")
                continue  # skip this URL

            if not table_data:
                print(f"No table found on {link_url}")
            else:
                # First row of table_data is likely the header row
                if not header_written:
                    # Write the header + an extra column for the "Source URL"
                    writer.writerow(table_data[0] + ["Source URL"])
                    header_written = True

                # Write the rest of the rows, appending the link_url to each
                for row in table_data[1:]:
                    writer.writerow(row + [link_url])

            # Optional: sleep to avoid hammering the server
            time.sleep(2)

    print("Done! All neighborhood tables saved to 'crime_data_all_neighborhoods.csv'.")

if __name__ == "__main__":
    main()
