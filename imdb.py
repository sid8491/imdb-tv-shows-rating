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
seasons = soup.find('div', {"class": "seasons-and-year-nav"}).contents[7].find_all('a')
season_number = []
season_url = []
episode_list = []
for season in seasons:
    season_number.append(season.text)
    season_url.append("http://imdb.com" + season['href'])

# for i in sorted(season_number):
#     print(i)
#     print(season_url[-int(i)])

# for loop for looping through all the seasons
for i in sorted(season_number):
    soup = BeautifulSoup(requests.get(season_url[-int(i)]).text, "html.parser")
    episode_div = soup.find('div', {'class': 'list detail eplist'})

    # loop for looping through episodes of given season
    # ii = 0
    for child in episode_div.children:
        # ii += 1
        # print(child.find('div', {'class': 'airdate'}))
        if str(child) != "\n":
            # print(child)
            # loop for href link and name of all episodes
            for ep_a in child.find_all('a'):
                print(ep_a['title'])
                print("http://imdb.com/" + ep_a['href'])
                soup = BeautifulSoup(requests.get("http://imdb.com/" + ep_a['href']).text, "html.parser")
                print(soup.find('div', {'class': 'imdbRating'}).find('span').text.strip())
                print(soup.find('span', {'class': 'small'}).text.strip())
                break
            print(child.find('div', {'class': 'item_description'}).text.strip())
            print(child.find('div', {'class': 'airdate'}).text.strip())
            print("---------------------")
        else:
            pass
        # if ii == 2:
        #     break
    print("**************************************************************************************************************")
    # break

