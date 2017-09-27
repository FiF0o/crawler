import sys
from module import logger
# print(sys.path)

# Append module to sys path here


import urllib
from lxml import html

url = "http://wiprodigital.com/"
page = html.fromstring(urllib.urlopen(url).read())

def getAllLinks(page):
    for link in page.xpath("//a"):
        print "Name", link.text, "URL", link.get("href")
    return

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    print("running the program...")
    getAllLinks(page)
    print(factorial(5))