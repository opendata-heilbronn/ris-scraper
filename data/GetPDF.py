from bs4 import BeautifulSoup
import urllib
import datetime

now = datetime.datetime.now()
r = urllib.request.urlopen('https://gemeinderat.stadt-heilbronn.de/Sitzungstermine/GR/'+ str(now.year) + '/').read()

soup = BeautifulSoup(r,'html.parser')
soup_red = soup.find(id='cont').find('a')

print('https://gemeinderat.stadt-heilbronn.de'+ soup_red['href'])
urllib.request.urlretrieve('https://gemeinderat.stadt-heilbronn.de'+ soup_red['href'], 'C:/Users/Jonas/Documents/OpenDataDay/OpenParl/GetPDF/Sitzungstermine.pdf')


