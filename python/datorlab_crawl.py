import requests
from bs4 import BeautifulSoup

url="http://www.datorlab.com/search?updated-max=2016-02-10T22%3A45%3A00%2B05%3A30&max-results=7#PageNo="
 
def spider(maxPages):
	page= 1
	while page<maxPages:
		link=url+str(page)
		sourceCode=requests.get(link)
	print (sourceCode)

spider(2)
