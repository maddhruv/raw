#import random
import urllib

def download(url):
	#name = random.randrange(1000, 10000)
	name = "main.jpg"
	urllib.urlretrieve(url, name)

download("https://github.com/midhruvjaink/midhruvjaink.github.io/blob/master/images/main.jpg")