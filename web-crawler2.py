#making of a web crawler by abhishektiwari981996
#github id abhishek981996
#Lets do it 
#Step 1 :searching in a given website


import urllib2
import re
from bs4 import BeautifulSoup
import random 


class Find():
    def open_url(self,url):
        '''This opens the url and returns the entire htmlform of the page'''
        opener = urllib2.build_opener()
        opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
        page = opener.open(url)
        return page

    def find(self,word,page):
        list = re.findall(word, page)
        return list


def twitter_search():
        print("enter the user name of whom you want to get the details")
        ask_input = raw_input()
        words = ask_input.replace(" ", "%20")
        url = "https://twitter.com/"+str(words)
        object1 = Find()
        return url, ask_input

def Spider():
    url,username = twitter_search()
    object1 = Find()
    page = object1.open_url(url)

    #now we have the page that is the entire detail of the user in html.
    # what we need is to scrape all the details such as followers tweets likes etc
    #this can be accoumplished using beautiful so
    soup = BeautifulSoup(page,"html.parser")
    links = soup.find_all("span", class_="ProfileNav-value")
    location = soup.find_all("span",class_="ProfileHeaderCard-locationText")
    bio_info = soup.find_all('p',class_="ProfileHeaderCard-bio")
    name = soup.find_all('a',class_="ProfileHeaderCard-nameLink")
    print ("\n\nname:%s, \nusername:%s, \ntweets:%s, \nlikes:%s, \nfollowers:%s, \nfollowing:%s, \nbio:%s, \nlocation:%s") %(name[0].string,
                username,links[0].string,links[3].string,links[2].string,links[1].string,
                bio_info[0].string,location[0].string)
  

  #  title = soup.find_all('a',attrs={'class': "detLink"})

   # description = soup.find_all('font', attrs={'class': "detDesc"})

    #i = random.randrange(0,3)
   # print("Do you wish to download %s having description %s .Type(y/n)")%(title[i].get_text(), description[i].get_text())
    #ask_input = raw_input()
    #if str(ask_input) == 'y':
     #   print links[i]
      #  download.download(links[i])
    #else:
     #   print("thks for using this")
if __name__ == '__main__':
    Spider()