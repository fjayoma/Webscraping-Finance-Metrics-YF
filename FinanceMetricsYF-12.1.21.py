
import requests
import bs4


headers = {'Users-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
def pull_data():
    ticker = input('Enter Ticker Symbol Here: ')
    yahoo = 'https://finance.yahoo.com/quote/'+ticker.upper()+'/'
    r = requests.get(yahoo)
    soup = bs4.BeautifulSoup(r.text,'lxml') #lxml helps translate python files from html/xml files
    return soup

def financial_data(soup):
    
    name = soup.find('h1',{'class':"D(ib) Fz(18px)"}).text
    current_price = soup.find('span',{'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
    previous_price = soup.find('td',{'data-test':'PREV_CLOSE-value'}).text
    price_change = soup.find('span',{'data-reactid':'48'}).text
    market_cap = soup.find('td',{'data-test':'MARKET_CAP-value'}).text
    beta = soup.find('td',{'data-test':'BETA_5Y-value' }).text    
    pe_ratio = soup.find('td',{'data-test':'PE_RATIO-value' }).text
    eps = soup.find('td',{'data-test':'EPS_RATIO-value' }).text
    
    
    print('Stock: ' + name)
    print(f'Current Price: {current_price}')
    print(f'Previous Price: {previous_price}')
    print(f'Price Change: {price_change}')
    print(f'Market Cap: {market_cap}')
    print(f'Beta: {beta}')
    print(f'Price to Earnings Ratio: {pe_ratio}')
    print(f'Earnings Per Share: {eps}')

def scrape_again():

    choice = 'default' #default setting for play again option

    while choice[0].lower() not in ['y','n']:
        choice = input("\nWould you like to select another Ticker? Y or N ") 
        if choice[0].lower() not in ['y','n']: 
            print("Sorry, I don't understand. Y or N?")
    if choice[0].lower() == 'n': 
        print('Have a great day!')
        return False
    elif choice[0].lower() == 'y':
        print('')
        return True
    

print('StOnKs\n')
scrape = True
while scrape:
    soup = pull_data()
    financial_data(soup)
    scrape = scrape_again()
