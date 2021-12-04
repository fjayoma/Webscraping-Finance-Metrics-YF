
import requests
import bs4



headers = {'User-Agent': 'Batista'}



yahoo = 'https://finance.yahoo.com/quote/AMZN/'
r = requests.get(yahoo)
soup = bs4.BeautifulSoup(r.text,'lxml') #lxml helps translate python files from html/xml files



name = soup.find('h1',{'class':"D(ib) Fz(18px)"}).text
print('Stock: ' + name)
current_price = soup.find('span',{'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
print('Current Price: ' + current_price)
previous_price = soup.find('span',{'data-reactid':'97'}).text
print('Previous Price: ' + previous_price)
price_change = soup.find('span',{'data-reactid':'48'}).text
print('Price Change: '+ price_change)
marketcap = soup.find('span',{'data-reactid':'138'}).text
print('Market Cap: ' + marketcap)
beta = soup.find('span',{'data-reactid':'143' }).text
print('Beta: ' + beta)
pe_ratio = soup.find('span',{'data-reactid':'148' }).text
print('Price to Earnings Ratio: ' + pe_ratio)
eps = soup.find('span',{"data-reactid":'153' }).text
print('Earnings Per Share: ' + eps)
