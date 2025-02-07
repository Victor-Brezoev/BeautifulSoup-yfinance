from bs4 import BeautifulSoup
import requests




url = "https://en.wikipedia.org/wiki/World_population"
data = requests.get(url).text

soup = BeautifulSoup(data, "html.parser")

tables = soup.find_all('table')
for index, table in enumerate(tables):
    if("10 most densely populated countries" in str(table)):
        table_index = index
print(table_index)
# print(tables[table_index].prettify())
import pandas as pd
import pandas as pd

# Initialize an empty list to store row data
data = []

# Iterate through table rows and extract data
for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if col:
        rank = col[0].text.strip()
        country = col[1].text.strip()
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        
        # Append row as a dictionary to the list
        data.append({
            "Rank": rank,
            "Country": country,
            "Population": population,
            "Area": area,
            "Density": density
        })

# Create DataFrame from the list of rows
population_data = pd.DataFrame(data)

print(population_data)

pd.read_html(str(tables[5]), flavor='bs4')
population_data_read_html = pd.read_html(str(tables[5]), flavor='bs4')[0]
print(population_data_read_html)