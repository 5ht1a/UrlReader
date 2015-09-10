# +++++++++++++++UrlReader++++++++++++++++
# This script takes a url as an input and prints its source code
# AGAIN: this code is very basic.
# Edit 

import urllib

urls = []
html_text = urllib.urlopen(raw_input("Type a url: "))
urls.append(html_text)
print html_text.read()

print '\033[1;33m---------------------------------------------------------------------\033[1;m'
again = (raw_input("Would you like to analyze another url? Y or N?: "))
if again == 'Y':
    while len(urls) < 5:
        another_url = urllib.urlopen(raw_input("Type another url: "))
        urls.append(another_url)
        print another_url.read()
        print '\033[1;44m---------------------------------------------------------------------\033[1;m'
        print ("Urls entered: " + str(len(urls)))
else:
    print '\033[1;34m---------------------------------------------------------------------\033[1;m'
    print '\033[1;36mALL URLS HAVE BEEN ANALYZED\033[1;m'
    print '\033[1;34m---------------------------------------------------------------------\033[1;m'

if len(urls) == 5:
    print '\033[1;36mALL URLS HAVE BEEN ANALYZED\033[1;m'
    print '\033[1;44m---------------------------------------------------------------------\033[1;m'
