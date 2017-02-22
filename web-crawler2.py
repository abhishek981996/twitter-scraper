#making of a web crawler by abhishektiwari981996
#github id abhishek981996
#Lets do it 
#Step 1 :searching in a given website


import urllib2
import re
from bs4 import BeautifulSoup
import random 
import download


class Find():
    def open_url(self,url):
        opener = urllib2.build_opener()
        opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
        page = opener.open(url)
        return page

    def find(self,word,page):
        list = re.findall(word, page)
        return list



class Search(Find):
    def ask_input(self):
        print("Enter the word you want to search")
        word = raw_input()
        words = word.replace(" ", "%20")


        return str(words)

    def google_search(self,lib):
        url = "https://www.google.co.in/search?q=" +(str(lib))+ "&oq="+(str(lib))+"&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
        object1 = Find()
        return object1.open_url(url)

    def pirate_torrent_seed(self,lib):
        url_open = "https://pirateproxy.vip/search/"
        url_base = "/0/7/0/"
        url = url_open + lib + url_base
        print url
        object1 = Find()
        page = object1.open_url(url)        
        return page

def Main():
    search = Search()
    word = search.ask_input()
    site_map = search.pirate_torrent_seed(word)
    soup = BeautifulSoup(site_map,"html.parser")
    
    links = soup.find_all('a', attrs={'href': re.compile("^magnet")})
    
    title = soup.find_all('a',attrs={'class': "detLink"})

    description = soup.find_all('font', attrs={'class': "detDesc"})

    i = random.randrange(0,3)
    print("Do you wish to download %s having description %s .Type(y/n)")%(title[i].get_text(), description[i].get_text())
    ask_input = raw_input()
    if str(ask_input) == 'y':
        print links[i]
        download.download(links[i])
    else:
        print("thks for using this")





    for t in title:
        print t.get_text()

if __name__ == '__main__':
    
    Main()