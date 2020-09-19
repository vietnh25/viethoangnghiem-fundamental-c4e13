import requests as r
from bs4 import BeautifulSoup
import pyexcel as p
from collections import OrderedDict

link = "https://www.cophieu68.vn/incomestatementq.php?id=fpt&view=ist&year=2018"

req = r.get(link, verify = False)
raw_db = req.content
soup = BeautifulSoup(req.content, "html.parser")
# print(soup)
db = soup.find('div', id="right_col")
# print(db.table)
table = db.table
tr_list = table.find_all("tr")

table_header = table.find("tr", class_ = "tr_header")
table_header = table_header.find_all("td")

data_header = []
for td in table_header:
  
  data_header.append(td.text)

data_exel = []
print(len(data_header))

for tr in tr_list:
  td_list = tr.find_all('td')
  data = {}
  index = 0
  for td in td_list:
    print(index)
    content = td.string
    data[data_header[index]] = content
    if index < len(data_header) - 1:
      index += 1
    else:
      pass

  data_exel.append(data)
print(data_exel)
  # data = {
  #   "year"
  # }
  # print(td.text)
# with open('file.html', 'wb') as f:
#   f.write(req.content)

p.save_as(records = data_exel, dest_file_name = "ex.csv")