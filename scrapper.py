import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page  = requests.get(START_URL)
soup = bs(page.text, "html.parser")

star_table = soup.find_all('table')

temp_list = []
table_rows = star_table[4].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')

    row = [i.text.rstrip() for i in td]
    
    temp_list.append(row)

print(temp_list)

name = []
distance = []
mass = []
radius = []

for i in range(1, len(temp_list)):
    name.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])

df = pd.DataFrame(list(zip(name, distance, mass, radius)), columns = ['Dwarf_name', 'Distance', 'Mass', 'Radius'])

print(df)
df.to_csv('brown_dwarfs.csv')

with open('brown_dwarfs.csv') as input, open('brown_dwarfs_sorted.csv', 'w', newline= '') as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)
