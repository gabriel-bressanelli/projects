import requests
from bs4 import BeautifulSoup
URL = "https://www.imdb.com/chart/top/"
r = requests.get(URL)
soup = BeautifulSoup(r.text, 'html.parser')
actors_dict={}
tbody = soup.find('tbody', attrs = {'class':'lister-list'})

for row in tbody.findAll('td',attrs = {'class':'titleColumn'}): 
    actor1 = row.a['title'].split(",")[1]
    actor2 = row.a['title'].split(",")[2]
    actors_dict[actor1] = actors_dict.get(actor1,0) + 1
    actors_dict[actor2] = actors_dict.get(actor2,0) + 1
    actors_sorted = sorted(actors_dict.items(), key=lambda x:x[1])
    actors_sorted.reverse()
    top_10 = actors_sorted[0:10]
##print(top_10)
for i in top_10:
    print(i)