from bs4 import BeautifulSoup
import json

def parse_zip_map(file_path):
    # Open the file and read its content.
    with open(file_path, "r", encoding="iso-8859-1") as file:
        html = file.read()

    soup = BeautifulSoup(html, "html.parser")
    zip_to_neighborhood = {}
    
    # Find the table with the ZIP code mappings; here we search for the table with a border attribute of "1"
    table = soup.find("table", {"border": "1"})
    if table is None:
        raise ValueError("Could not find the ZIP code table in the provided HTML.")

    # Loop through all rows except the header row
    rows = table.find_all("tr")[1:]  # assuming the first row is the header
    for row in rows:
        tds = row.find_all("td")
        if len(tds) >= 2:
            # Get the ZIP code: check if it's wrapped in an <a> tag
            zip_code_tag = tds[0].find("a")
            zip_code = zip_code_tag.get_text(strip=True) if zip_code_tag else tds[0].get_text(strip=True)
            
            # Get the neighborhood name from the second column
            neighborhood = tds[1].get_text(strip=True)
            
            zip_to_neighborhood[zip_code] = neighborhood
            
    return zip_to_neighborhood

if __name__ == "__main__":
    file_path = "test/zips.html"  # change to your file path if needed
    mapping = parse_zip_map(file_path)
    zips_dict = {}
    for zipcode, neighborhood in mapping.items():
        neighborhood = neighborhood.replace("\n", "")
        zips_dict[str(zipcode)] = neighborhood
        # print(f"{zipcode}: {neighborhood}")
    with open("zip2neighborhood.json", "w") as file:
        json.dump(zips_dict, file, indent=4)
