from bs4 import BeautifulSoup
import requests

r = requests.get('http://qiita.com/advent-calendar/2016/crawler')

soup = BeautifulSoup(r.content, "html.parser")

soups = [i.get_text() for i in soup.find_all('a',rel = 'noopener noreferrer')]
# リスト内包表記：以下と同等
#
#soups=[]
#for i in soup.find_all('a',rel = 'noopener noreferrer'):
#    soups.append(i.get_text())
    
    
links = [url.get('href') for url in soup.find_all('a',rel = 'noopener noreferrer')]

for soups,links in zip(soups,links):
    print("{0},{1}".format(soups,links))

#zip関数
#for i, soups_e in enumerate(soups):
#    links_e = links[i]
#    print(soups_e, links_e)