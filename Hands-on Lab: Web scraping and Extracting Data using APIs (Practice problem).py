'''
Try the following practice problems to test your understanding of the lab. Please note that the solutions for the following are not shared. You are encouraged to use the discussion forums in case you need help.

Modify the code to extract Film, Year, and Rotten Tomatoes' Top 100 headers.

Restrict the results to only the top 25 entries.

Filter the output to print only the films released in the 2000s (year 2000 included).


'''


import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

# URL of the web page
url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'

# Database and table details
db_name = "Movie25.db"
table_name = "Top_25"
csv_path = "/home/project/top_25_films.csv"

# Initialize an empty DataFrame with specified columns
df = pd.DataFrame(columns=["Film", "Year", "Rotten Tomatoes' Top 100"])
count = 0

# Request the HTML page
html_page = requests.get(url).text
data = BeautifulSoup(html_page, 'html.parser')

# Find the tables in the HTML
tables = data.find_all('tbody')
rows = tables[0].find_all('tr')

# Iterate over the rows of the table
for row in rows:
    if count < 25:
        cols = row.find_all('td')
        if len(cols) != 0:
            # Extract data from the columns
            film = cols[1].get_text(strip=True)
            year = cols[2].get_text(strip=True)
            rotten_tomatoes_rank = cols[3].get_text(strip=True)
            
            # Ensure year is numeric and compare
            if year.isdigit() and 2000 <= int(year):
                # Create a dictionary with the extracted data
                data_dict = {"Film": film, "Year": year, "Rotten Tomatoes' Top 100": rotten_tomatoes_rank}
                # Convert the dictionary to a DataFrame
                df1 = pd.DataFrame(data_dict, index=[0])
                # Concatenate the new DataFrame with the main DataFrame
                df = pd.concat([df, df1], ignore_index=True)
                count += 1
    else:
        break

# Print the DataFrame
print(df)

# Save the DataFrame to a CSV file
df.to_csv(csv_path, index=False)

# Connect to the SQLite database and save the DataFrame to a table
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()
