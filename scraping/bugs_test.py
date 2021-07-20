from bs4 import BeautifulSoup
from urllib.request import urlopen

class Bugs(object):
    def __init__(self, url):
        self.url = url

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        n_artist = 0
        n_title = 0
        ls_artist = soup.find_all(name='p', attrs={'class': 'artist'})
        ls_title = soup.find_all(name='p', attrs={'class': 'title'})
        print(f'Chart {len(ls_artist)}!')
        for i in ls_artist:
            n_artist += 1
            print(f'{n_artist} Rank')
            print(f'Artist : {i.find("a").text}', end='\t\t')
            print(f'Title : {ls_title[n_title].find("a").text} ')
            n_title += 1
            print('*'*100)


def main():
    Bugs('https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20210720&charthour=16').scrap()

if __name__ == '__main__':
    main()