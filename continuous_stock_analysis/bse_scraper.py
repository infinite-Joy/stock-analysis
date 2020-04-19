from datetime import datetime
from lxml import html
import requests

urls = {
    'tcs': 'https://www.moneycontrol.com/india/stockpricequote/computers-software/tataconsultancyservices/TCS',
    'infosys': 'https://www.moneycontrol.com/india/stockpricequote/computers-software/infosys/IT',
    'hcl': 'https://www.moneycontrol.com/india/stockpricequote/computers-software/hcltechnologies/HCL02',
    'tech mahindra': 'https://www.moneycontrol.com/india/stockpricequote/computers-software/techmahindra/TM4',
    'oracle finserv': 'https://www.moneycontrol.com/india/stockpricequote/computers-software/techmahindra/TM4',
    'mphasis': 'https://www.moneycontrol.com/india/stockpricequote/computers-software/mphasis/MB02',
}


print(datetime.now())
for company_name, company_url in urls.items():
    page = requests.get(company_url)
    tree = html.fromstring(page.content)
    price = tree.xpath('/html/body/section[1]/div[2]/section[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[2]/span[1]/text()')
    price = price[0]
    print(f'company: {company_name}; price: {price}')
