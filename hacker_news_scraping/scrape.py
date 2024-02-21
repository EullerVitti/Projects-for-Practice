import requests 
import sys
from bs4 import BeautifulSoup
import pprint

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key = lambda k:k['votes'], reverse = True)


def create_custom_hn(links,subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText() #page titles
        href = item.get('href', None) #page links (called href on "inspect") / None in case there's no link attached or link is broken
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            #print(points)
            if points > 99:
                hn.append({'title': title, 'link':href, 'votes': points})
    return sort_stories_by_votes(hn)


res = []
url = 'https://news.ycombinator.com/news?p=1'
num_pg = int(sys.argv[1])


if num_pg >= 1:
    for n in range(1, num_pg+1):
        url = url.replace('p=1',f'p={n}')
        res.append(url)


soup = BeautifulSoup(requests.get(res[0]).text, 'html.parser')
links = soup.select('.titleline > a')
subtext = soup.select('.subtext')

if num_pg > 1:
    for i in range(2,num_pg):
        soup = BeautifulSoup(requests.get(res[i]).text, 'html.parser')
        links += soup.select('.titleline > a')
        subtext += soup.select('.subtext')


pprint.pprint(create_custom_hn(links,subtext))
