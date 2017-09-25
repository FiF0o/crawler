import sys
from module import logger
# print(sys.path)

# Append module to sys path here


import urllib
from lxml import html

url = "http://wiprodigital.com/"
page = html.fromstring(urllib.urlopen(url).read())

def printLink(page):
    for link in page.xpath("//a"):
        print "Name", link.text, "URL", link.get("href")
    return

if __name__ == "__main__":
    print("running the program...")
    printLink(page)