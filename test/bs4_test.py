import requests
from bs4 import BeautifulSoup

def scrape_table():
    url = "https://www.civichub.us/ca/san-francisco/gov/police-department/crime-data/treasure-island"
    
    # 1. Request the page
    response = requests.get(url)
    response.raise_for_status()  # raise an HTTPError if there's a 4xx/5xx
    
    # 2. Parse with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 3. Find any <table> elements
    tables = soup.find_all("table")
    if not tables:
        print("No <table> elements found on this page.")
        return
    
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

if __name__ == "__main__":
    scrape_table()
