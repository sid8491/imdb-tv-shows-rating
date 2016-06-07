__author__ = 'Sid'

import requests
from bs4 import BeautifulSoup
global a1
global season_number, season_url, epsiode_list
search = "how i met your mother"
# search = "person of interest"
url = "http://www.imdb.com/find?q=" + search
soup = BeautifulSoup(requests.get(url).text, "html.parser")
show = soup.find("table").find_next()
for a in show.find_all('a'):
    a1 = a['href']
    break
print("You searched for :" + show.text.strip())
show_url = "http://www.imdb.com" + a1
print("IMDB URL : " + show_url)

soup = BeautifulSoup(requests.get(show_url).text, "html.parser")
print(soup.title)
seasons = soup.find('div', {"class" : "seasons-and-year-nav"}).contents[7].find_all('a')
season_number = []
season_url = []
episode_list = []
for season in seasons:
    season_number.append(season.text)
    season_url.append("http://imdb.com" + season['href'])

# for i in sorted(season_number):
#     print(i)
#     print(season_url[-int(i)])

for i in sorted(season_number):
    soup = BeautifulSoup(requests.get(season_url[-int(i)]).text, "html.parser")
    episode_div = soup.find('div', {'class': 'list detail eplist'})
    abc = 0
    # for child in episode_div.children:
    #     abc += 2
    #     # print(child.find('div', {'class': 'airdate'}))
    #     print(child)
    #     if(abc==3):
    #         break
    # for ep in episode_div:
    episode_date = episode_div.find('div', {'class' : 'airdate'})
    # episode_synopsis = episode_div.find('div', {'class' : 'item_description'})
    print(episode_date.text.strip())
    # print(episode_synopsis.text.strip())
    # break

