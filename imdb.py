__author__ = 'Sid'

import requests
from bs4 import BeautifulSoup
# global show_url, season_number, season_url

search = "narcos"
# search = "person of interest"
# search = "rome"
# search on imdb
url = "http://www.imdb.com/find?q=" + search
soup = BeautifulSoup(requests.get(url).text, "html.parser")
show = soup.find("table").find_next()
for a in show.find_all('a'):
    show_url = a['href']
    break
show_url = "http://www.imdb.com" + show_url

soup = BeautifulSoup(requests.get(show_url).text, "html.parser")
print("Title : " + soup.title.text[:-7])
print("IMDB URL : " + show_url)
seasons = soup.find('div', {"class": "seasons-and-year-nav"}).contents[7].find_all('a')
season_number = []
season_url = []

for season in seasons:
    season_number.append(season.text)
    season_url.append("http://imdb.com" + season['href'])

# initializing arrays for storing values
episode_list = [[] for i in range(len(season_number)+1)]
title_list = [[] for i in range(len(season_number)+1)]
link_list = [[] for i in range(len(season_number)+1)]
synopsis_list = [[] for i in range(len(season_number)+1)]
rating_list = [[] for i in range(len(season_number)+1)]
raters_list = [[] for i in range(len(season_number)+1)]
airdate_list = [[] for i in range(len(season_number)+1)]

# for loop for looping through all the seasons
for i in sorted(season_number):
    soup = BeautifulSoup(requests.get(season_url[-int(i)]).text, "html.parser")
    episode_div = soup.find('div', {'class': 'list detail eplist'})
    episode_number = 0

    # loop for looping through episodes of given season
    ii = 0
    for child in episode_div.children:
        ii += 1
        if str(child) != "\n":
            # loop for href link and name of all episodes
            for ep_a in child.find_all('a'):
                episode_number += 1
                try:
                    episode_list[int(i)].append(episode_number)
                except:
                    episode_list[int(i)].append("NA")
                try:
                    title_list[int(i)].append(ep_a['title'])
                except:
                    title_list[int(i)].append("NA")
                link_list[int(i)].append("http://imdb.com/" + ep_a['href'])
                soup = BeautifulSoup(requests.get("http://imdb.com/" + ep_a['href']).text, "html.parser")
                try:
                    rating_list[int(i)].append(soup.find('div', {'class': 'imdbRating'}).find('span').text.strip())
                except:
                    rating_list[int(i)].append("NA")
                try:
                    raters_list[int(i)].append(soup.find('span', {'class': 'small'}).text.strip())
                except:
                    raters_list[int(i)].append("NA")
                break   # to avoid duplicates
            try:
                synopsis_list[int(i)].append(child.find('div', {'class': 'item_description'}).text.strip())
            except:
                synopsis_list[int(i)].append("NA")
            try:
                airdate_list[int(i)].append(child.find('div', {'class': 'airdate'}).text.strip())
            except:
                airdate_list[int(i)].append("NA")
            print("Fetching information of Season " + str(i) + " : Episode " + str(episode_number))
            print("---------------------")
        else:
            pass
    print("**************************************")

# printing values
for k in range(1, len(episode_list)):
    for l in range(1, len(episode_list[k])):
        print("Season: " + str(k) + " Episode: " + str(l))
        print("Rating : " + str(rating_list[int(k)][int(l)]) + " rated by " + str(raters_list[int(k)][int(l)]) + " users")
        print("Title : " + str(title_list[int(k)][int(l)]) + " Aired on (" + str(airdate_list[int(k)][int(l)]) + ")")
        print("Link : " + str(link_list[int(k)][int(l)]))