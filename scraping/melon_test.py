from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request

class Melon(object):
    def __init__(self, url):
        self.url = url

    def scrap(self):
        soup = BeautifulSoup(urlopen(Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})), 'lxml')
        n_artist = 0
        n_title = 0
        ls_artist = soup.find_all(name='div', attrs={'class': 'ellipsis rank01'})
        ls_title = soup.find_all(name='div', attrs={'class': 'ellipsis rank02'})
        for i in ls_artist:
            n_artist += 1
            print(f'{n_artist} 위')
            print()

def main():
    Melon('https://www.melon.com/chart/index.htm?dayTime=2021072016').scrap()

if __name__ == '__main__':
    main()