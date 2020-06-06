
#iTunesの無料Appランキングに表示されている100個のアイコン画像を、カレントディレクトリのimagesディレクトリ内にすべてダウンロードしてください。
#iTunes - App Storeでトップ無料Appをチェックする - Apple（日本）
#http://www.apple.com/jp/itunes/charts/free-apps/
#ダウンロードする際は、リクエスト間隔を1秒空けるようにしてください。time.sleep()関数で指定秒数スリープできます。
#余裕があれば、保存する画像のファイル名を2.Super_Mario_Run.jpgのようにわかりやすい名前にしてみてください

from bs4 import BeautifulSoup
import requests
import time

r = requests.get('http://topappranking300.appios.net/')

soup = BeautifulSoup(r.content, "html.parser")

links = [url.get('src') for url in soup.select('.app-icon')]
names = [i.get_text().strip('\n').replace(" ","") for i in soup.select('.go_dl.h40')]


#for i in names:
#    print(i)



for url,name in zip(links[:100],names[:100]):
    
    time.sleep(1)
    r = requests.get(url)
    filename = 'images/' + str(names.index(name) + 1) + "." + name.replace("/","") + '.jpg'

    if r.status_code == 200:
        f = open(filename,'wb')
        f.write(r.content)
        f.close