"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: David Smětala
email: x213@centrum.com
discord: davids1682
"""

import requests
from bs4 import BeautifulSoup as BS
import csv
import sys

if len(sys.argv) != 3:
    print("Pro správný běh programu je nutno zadat dva argumenty. \
A to odkaz a jméno výstupního souboru")
    quit()

url = sys.argv[1]
file_name = sys.argv[2]
auxiliary_url = "https://volby.cz/pls/ps2017nss/"
data = dict()
data_colected = []
#url for tests
#url = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7105"
print(f"Získávám data z {url}")
url_data = requests.get(url)
soup = BS(url_data.text, 'html.parser')
#gets tables from site
tables = soup.find_all("table", {"class": "table"})  

for table in tables:
    # finds all table rows
    all_tr = table.find_all("tr")   
    for one_tr in all_tr[2:]:
        # finds all table data except first and second rows
        all_td = one_tr.find_all("td") 
        # skips empty rows
        if 'hidden_td' in all_td[0].get('class', []): continue 
        #gets link from td and comlpetes url for next use
        district_url = all_td[0].a.get("href")
        url_district = auxiliary_url + district_url
        # gets code and location for dictionary from first page
        data["code"] = all_td[0].text
        data["location"] = all_td[1].text

        # for more data needs to go to next page geted from first page
        # requests for data from specific district
        district_data = requests.get(url_district)            
        district_soup = BS(district_data.text, "html.parser") 
        # gets tables from site
        district_tables = district_soup.find_all("table", {"class": "table"})
        # first table contains data about registered,
        # envelopes and valid on third row      
        d_all_tr = district_tables[0].find_all("tr")   
        d_all_td = d_all_tr[2].find_all("td")           
        # saving data to dictionary
        data["registered"] = d_all_td[3].text
        data["envelopes"] = d_all_td[6].text
        data["valid"] = d_all_td[7].text
       
        # gets rows from tables except first table
        for district_table in district_tables[1:]:
            d_all_tr = district_table.find_all("tr")
            # gets name of party, the number of votes and saves to dictionary
            for d_one_tr in d_all_tr[2:]:       
                 d_all_td = d_one_tr.find_all("td")
                 # skips empty rows
                 if 'hidden_td' in d_all_td[0].get('class', []): continue
                 data[d_all_td[1].text] = d_all_td[2].text
        # saves colection of data in dictionary to list
        copy_of_data = data.copy()
        data_colected.append(copy_of_data)
        

def write_data(data: list, file_name: str) -> str:
    """
    Write informations from parameter "data" to file in format .csv.
    """
    with open(file_name, mode="w", encoding="utf-8", newline="") as csv_file:
        collums = data[0].keys()

        record = csv.DictWriter(csv_file, fieldnames=collums)
        record.writeheader()
        record.writerows(data)

print(f"Zapisuji data do souboru {file_name}")
write_data(data_colected, file_name)
print("Ukončuji Elections Scraper")

   





