from bs4 import BeautifulSoup
import pprint
import json

# Read the HTML content from the file (replace 'your_file.html' with your actual filename)
with open("test/high.html", "r", encoding="utf-8") as file:
    html = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find the ordered list that contains all the high school items.
schools_list = soup.find("ol", class_="item-list__OrderedListStyled-sc-18yjqdy-0")
if not schools_list:
    print("Could not find the high schools list; please check the selector.")
    exit(1)

# Create a list to hold the extracted data for each school
schools_data = []

# Loop through each list item that represents a school
for li in schools_list.find_all("li", recursive=False):
    # Each real school entry is wrapped in a <section>; skip if not found (ads or spacers)
    section = li.find("section")
    if not section:
        continue

    # ========================
    # Extract the School Name
    # ========================
    school_name = "N/A"
    h2 = section.find("h2")
    if h2:
        a_tag = h2.find("a")
        if a_tag:
            school_name = a_tag.get_text(strip=True)

    # =================================
    # Extract Location and District Info
    # =================================
    location = "N/A"
    district = "N/A"
    location_div = section.find("div", class_="DetailCardHighSchools__LocationContainer-zfywu8-3")
    if location_div:
        paragraphs = location_div.find_all("p")
        if len(paragraphs) >= 2:
            location = paragraphs[0].get_text(strip=True)
            district = paragraphs[1].get_text(strip=True)
        elif paragraphs:
            location = paragraphs[0].get_text(strip=True)

    # ============================
    # Extract the Ranking Details
    # ============================
    rankings = {}
    ranking_ul = section.find("ul", class_="RankingList__ListStyled-sc-7e61t7-0")
    if ranking_ul:
        # Each ranking is in an <li>
        for li_rank in ranking_ul.find_all("li"):
            # Grab all text in the li; typically formatted as something like:
            # "#1 in San Francisco Unified School District Rankings"
            full_text = li_rank.get_text(" ", strip=True)
            if " in " in full_text:
                # Split the ranking number from the description.
                rank_value, description = full_text.split(" in ", 1)
                rankings[description.strip()] = rank_value.strip()
            else:
                # Fallback if the expected format is missing
                rankings["general"] = full_text

    # =======================
    # Extract the School Stats
    # =======================
    stats = {}
    stats_column = section.find("div", class_="DetailCardHighSchools__StatsColumn-zfywu8-2")
    if stats_column:
        # Each stat is in a container div with a specific class name.
        stat_containers = stats_column.find_all("div", class_="QuickStatHug__Container-hb1bl8-0")
        for stat in stat_containers:
            dl = stat.find("dl")
            if dl:
                # Often the dt (label) and dd (value) are wrapped in a div inside the dl.
                container = dl.find("div")
                if container:
                    dt = container.find("dt", class_="label-wrapper")
                    dd = container.find("dd", class_="QuickStatHug__Description-hb1bl8-1")
                    if dt and dd:
                        label = dt.get_text(strip=True)
                        value = dd.get_text(strip=True)
                        stats[label] = value

    # ==============================================
    # Collect all data into a dictionary for this school
    # ==============================================
    school_entry = {
        "name": school_name,
        "location": location,
        "district": district,
        "rankings": rankings,
        "stats": stats,
    }
    schools_data.append(school_entry)

# Print out all the collected data in a readable format:
pprint.pprint(schools_data)
with open("high.json", 'w') as file:
    json.dump(schools_data, file, indent=4)
