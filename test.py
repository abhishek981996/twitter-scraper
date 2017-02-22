#!/usr/bin/env python2
import urllib
import zlib
#import os
from subprocess import call

def choose_torrent(torrents_found):
    input_given = False
    while not input_given:
        try:
            choice = input('Choose: ')
            while choice < 0 or choice > torrents_found:
                print 'Not available, choose again.'
                choice = input('Choose again: ')
            input_given = True
        except NameError:
            print "Smartass."
    return choice

def search_for_torrents(search_str):
    url_open = "https://pirateproxy.vip/search/"
    url_base = "/0/7/0/"
    url = url_open + str(search_str) + url_base
    page_source = zlib.decompress(urllib.urlopen(url).read(), 16+zlib.MAX_WBITS)

    paths = []
    i = last_pos = 0
    while i < 10 and page_source.find('cellMainLink', last_pos) != -1:
        torrent_page_start_url = page_source.rfind('<a href=', 0, page_source.find('cellMainLink', last_pos))
        torrent_page_end_url = page_source.find('"', torrent_page_start_url + 10)
        url = page_source[torrent_page_start_url + 10: torrent_page_end_url]
        paths.append(url)
        print '[' + str(i) + '] ' + url[:-15].replace('-', ' ').title()
        last_pos = page_source.find('cellMainLink', last_pos) + 1
        i += 1
    if i == 0:
        print 'No torrents found.\n'
        return
    else:
        print '[' + str(i) + '] None || Search Again.'

    choice = choose_torrent(i)
    while choice != i:
        url = paths[choice]
        page_source = zlib.decompress(urllib.urlopen('https://kickass.to/' + url).read(), 16+zlib.MAX_WBITS)
        magnet_link =  page_source[page_source.find('magnet:'):page_source.find('"', page_source.find('magnet:') + 7)]

        #call(["xdg-open", magnet_link]) -> Linux
        #call(['deluge-console.exe', 'add ' + magnet_link]) -> Windows Deluge
        #os.startfile(magnet_link) -> Windows other clients -> Windows other clients
        choice = choose_torrent(i)
    print

if __name__ == '__main__':
    try:
        print 'Hit CTRL+C to terminate execution.'
        while True:
            search_str = raw_input('Input search term: ')
            search_for_torrents(search_str)
    except KeyboardInterrupt:
        print "Goodbye!"