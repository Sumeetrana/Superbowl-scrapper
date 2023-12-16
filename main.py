import requests
from bs4 import BeautifulSoup
import sys 

url = "https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "lxml")
tables = soup.find_all("table", class_="wikitable sortable")

packers_wins = 0
highest_attendance = 0
lowest_attendance = sys.maxsize
total_attendance = 0
year = 0
refree_name = ''

for row in tables[0].find_all("tr"):
    for inner_row in row.find_all("td"):
        if "Green Bay Packers" in inner_row.text:
            packers_wins += 1

for row in tables[0].find_all("tr"):
  if row.find_all("td"):
      attendance = row.find_all("td")[7].text
      attendance = attendance[:len(attendance)-1]
      attendance = attendance.replace(",", "")
      total_attendance += int(attendance)

      if(highest_attendance < int(attendance)):
          highest_attendance = int(attendance)
          year = row.find_all("td")[1].text

      if(lowest_attendance > int(attendance)):
          lowest_attendance = int(attendance)

fourtyNinethSuperBowlRow = tables[0].find_all("tr")[49]
if fourtyNinethSuperBowlRow.find_all("td"):
    refree_name = fourtyNinethSuperBowlRow.find_all("td")[8].text

print(f"Packers: {packers_wins-1}")
print(f"High: {highest_attendance} in the year {year}")
print(f"Low: {lowest_attendance}")
print(f"Total: {total_attendance}")
print(f"Refree: {refree_name}")