import requests
import bs4
from pprint import pprint

url = 'https://www.ss.com/lv/transport/cars/volkswagen/'
data = requests.get(url)
html = bs4.BeautifulSoup(data.text, 'html.parser')

sludDict = {}

tables = html.select('#filter_frm table')
sludinajumi = tables[2]
ieraksti = sludinajumi.select('tr')
skaits = 0
for each in ieraksti:
  teksts = each.select('.msga2-o')
  sludDict[skaits] = {}
  for i, katrs in enumerate(teksts):
    if i == 1:
      sludDict[skaits]["Modelis"] = "VW / " + katrs.text
    if i == 3:
      sludDict[skaits]["Cena"] = katrs.text
  skaits += 1

del(sludDict[0])
del(sludDict[31])
pprint(sludDict, sort_dicts=False)
