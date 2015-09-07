# +++++++++++++++UrlReader2.0++++++++++++++++
# This version fixes minor errors in the urls list and makes the output clearer to read.
# AGAIN: this code is very basic.

import urllib

urls = []
html_text = urllib.urlopen(raw_input("Type a url"))
urls.append(html_text)
print html_text.read()

while len(urls) < 5:
    another_url = urllib.urlopen(raw_input("Type another url"))
    urls.append(another_url)
    print another_url.read()
    print ("---------------------------------------------------------------------")
    print ("Urls entered: " + str(len(urls)))

if len(urls) == 5:
    print ("ALL URLS HAVE BEEN ANALYZED")
