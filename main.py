import requests
from bs4 import BeautifulSoup
import sys 

url = "https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "lxml")
# Finding the table consisting the superbowl data
tables = soup.find_all("table", class_="wikitable sortable")

# Initializing all the variables
packers_wins = 0
highest_attendance = 0
lowest_attendance = sys.maxsize
total_attendance = 0
year = 0
refree_name = ''

# Iterating over all the rows in the table
for row in tables[0].find_all("tr"):
  # Checking if a particular row has columns or not
  if row.find_all("td"):
      # Finding the attendance text
      attendance = row.find_all("td")[7].text
      attendance = attendance[:len(attendance)-1]
      # Converting attendance string to interger
      attendance = int(attendance.replace(",", ""))
      
      # Finding out the value of total attendance
      total_attendance += attendance

      # Finding out highest attendance and it's year
      if(highest_attendance < attendance):
          highest_attendance = attendance
          year = row.find_all("td")[1].text

      # Finding out lowest attendance
      if(lowest_attendance > attendance):
          lowest_attendance = attendance

  # Finding out the number of times 'Green Bay Packers' won
  for inner_row in row.find_all("td"):
      if "Green Bay Packers" in inner_row.text:
          packers_wins += 1

# Finding out the refree name in 49th superbowl
fourtyNinethSuperBowlRow = tables[0].find_all("tr")[49]
if fourtyNinethSuperBowlRow.find_all("td"):
    refree_name = fourtyNinethSuperBowlRow.find_all("td")[8].text

print(f"Packers: {packers_wins-1}")
print(f"High: {highest_attendance} in the year {year}")
print(f"Low: {lowest_attendance}")
print(f"Total: {total_attendance}")
print(f"Refree: {refree_name}")