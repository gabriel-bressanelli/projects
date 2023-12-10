# This program scrape data from a gov website 
# Useed beautiful soup to scrape the dat
import requests 
from bs4 import BeautifulSoup
import csv

URL = "https://www.bls.gov/web/ximpim/beaimp.htm"

r = requests.get(URL) # getting the url

allHTML = BeautifulSoup(r.text, 'html.parser') #requesting the whole HTML
tbody = allHTML.find('tbody') # finding the list body

agri = {} # creating dictonary



for x in range(1, 40):  # Creating a loop to be able to get all the months out of the table 
  allYears = 'ipp_hist_bea_m.r.8.'
  allYears = allYears + str(x)

  html_year = tbody.find('th', attrs={'id' : allYears})

  year_values = tbody.findAll('td', attrs={'headers': allYears})
  del year_values[0]
  del year_values[0]

  yearlist = []
  for k in html_year:
    yearlist.append(k.get_text())


  mylist = []
  for i in year_values:
    if i.get_text() == '-' or i.get_text() == '':
      mylist.append(0)
    else:
      mylist.append(i.get_text())

  agri[html_year.get_text()] = mylist

  with open('Agricultural foods, feeds & beverages, excluding distilled beverages.csv', 'w', newline= '') as csvfile:
    headers = ['Year', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Agus', 'Sept', 'Oct', 'Nov', 'Dec']
    writer = csv.DictWriter(csvfile, fieldnames=headers)

    writer.writeheader()
    writer.writerow

    for k,v in agri.items():
      writer.writerow({"Year":k, 'Jan':v[0], 'Feb':v[1], 'Mar':v[2], 'Apr':v[3], 'May':v[4], 'Jun':v[5], 'Jul':v[6], 'Agus':v[7], 'Sept':v[8], 'Oct':v[9], 'Nov':v[10], 'Dec':v[11] })


  print(agri)



