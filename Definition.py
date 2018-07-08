import re
import urllib.request
from urllib.request import Request


url = "http://www.dictionary.com/browse/"
word = input("Enter the word to find its definition.\n")
url = url + word

newUrl = Request(url,headers={"User-Agent":"Mozilla/5.0"})
data = urllib.request.urlopen(newUrl).read()
actualData = data.decode("utf-8")

#print(actualData)
#<meta name="description" content="Energy definition, the capacity for vigorous activity; available power: I eat chocolate to get quick energy. See more.">

de = re.search('<meta name="description" content="',actualData)
df = re.search(' See more.">',actualData)


print(actualData[de.end():df.start()])



