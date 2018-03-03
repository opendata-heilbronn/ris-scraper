import datetime
import os
import urllib.request

from bs4 import BeautifulSoup

now = datetime.datetime.now()
r = urllib.request.urlopen('https://gemeinderat.stadt-heilbronn.de/Sitzungstermine/GR/' + str(now.year) + '/').read()

soup = BeautifulSoup(r, 'html.parser')
soup_red = soup.find(id='cont').find('a')

print('https://gemeinderat.stadt-heilbronn.de' + soup_red['href'])
targetFile = os.path.join("..", "data", "sitzungsplan.pdf")
urllib.request.urlretrieve('https://gemeinderat.stadt-heilbronn.de' + soup_red['href'], targetFile)
