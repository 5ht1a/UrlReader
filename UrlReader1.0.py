import urllib

urls = ['']
htmltext = urllib.urlopen(raw_input("Type a url"))
urls.append(htmltext)
print htmltext.read()

while len(urls) < 5:
    anotherurl = urllib.urlopen(raw_input("Type another url"))
    urls.append(anotherurl)
    print anotherurl.read()
