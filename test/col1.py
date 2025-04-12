import requests

url = "https://www.healthysf.org/bdi/outcomes/zipmap.htm"
response = requests.get(url)
response.raise_for_status()  # raise error if there's a 4xx/5xx

# Save the HTML to a file named "sfpd_crime_statistics.html"
with open("test/zips.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print("HTML saved to sfpd_crime_statistics.html!")