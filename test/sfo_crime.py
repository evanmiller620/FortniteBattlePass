import requests
from bs4 import BeautifulSoup

def scrape_civichub():
    url = "https://www.civichub.us/sfpd-crime-statistics"

    # 1. GET the page
    response = requests.get(url)
    response.raise_for_status()  # raise exception if not 200 OK

    # 2. Extract the HTML text
    html_content = response.text

    # 3. Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # ---- EXAMPLE A: Get all paragraph text ----
    # paragraphs = soup.find_all('p')
    # print("\n--- Paragraphs ---")
    # for p in paragraphs:
    #     print(p.get_text(strip=True))

    # ---- EXAMPLE B: Find all hyperlinks (anchor tags) ----
    links = soup.find_all('a')
    print("\n--- Links ---")
    for link in links:
        href = link.get('href')
        text = link.get_text(strip=True)
        print(f"Text: {text} | Href: {href}")

    # ---- EXAMPLE C: If there's a table of data, scrape it ----
    # Let's assume there's a <table> element with rows <tr> and cells <td>:
    # tables = soup.find_all('table')
    # for i, table in enumerate(tables, start=1):
    #     print(f"\n--- Table #{i} ---")
    #     rows = table.find_all('tr')
    #     for row in rows:
    #         cols = row.find_all(['th','td'])
    #         # Extract text from each cell
    #         col_texts = [col.get_text(strip=True) for col in cols]
    #         print(col_texts)

if __name__ == "__main__":
    scrape_civichub()
