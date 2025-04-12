import requests
from bs4 import BeautifulSoup

url = "https://www.civichub.us/ca/san-francisco/gov/police-department/crime-data/neighborhoods"
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# Find all <a> tags whose class is "ui-accordion-content" and that have an href
links = soup.find_all("a", class_="ui-accordion-content", href=True)

# Extract their hrefs
hrefs = [link["href"] for link in links]

print("Found hrefs:")
for url in hrefs:
    # 1. Request the page
    response = requests.get(url)
    response.raise_for_status()  # raise an HTTPError if there's a 4xx/5xx
    
    # 2. Parse with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 3. Find any <table> elements
    tables = soup.find_all("table")
    if not tables:
        print("No <table> elements found on this page.")
    
    # Let's assume there's at least one table; take the first:
    table = tables[0]
    
    # 4. Extract rows (each <tr>)
    rows = table.find_all("tr")
    
    # We'll store parsed rows here
    table_data = []
    
    for row in rows:
        # Each row can have <th> or <td> cells
        cells = row.find_all(["th", "td"])
        cell_texts = [cell.get_text(strip=True) for cell in cells]
        table_data.append(cell_texts)
    
    # 5. Print or save the table data
    print("Table contents:")
    for row in table_data:
        print(row)
