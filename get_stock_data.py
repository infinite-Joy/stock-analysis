from lxml import html
import requests
import time

from try_module import trying as trying
from company_page import CompanyPage

def company_page_analysis(stock_company):
    page = requests.get('http://money.rediff.com/%s' % stock_company)
    time.sleep(2)
    tree = html.fromstring(page.text)
    company = CompanyPage(tree)
    pe_ratio = company.get_pe_ratio(tree)
    eps = company.get_eps(tree)
    price_of_stock = company.get_price_of_stock(tree)
    fifty_two_wk_high = company.get_fifty_two_wk_high(tree)
    fifty_two_wk_low = company.get_fifty_two_wk_low(tree)
    print pe_ratio
    print eps
    print price_of_stock
    print fifty_two_wk_high, fifty_two_wk_low
    print price_of_stock < ((fifty_two_wk_high - fifty_two_wk_low)/2)
    

def main():
    stock_company = "Amtek-Auto-Ltd"
    company_page_analysis(stock_company)
    
    # balance_sheet = tree.xpath('/html/body/div[4]/div[8]/div[8]/div[2]/div/a[4]/@href')
    # print "".join(balance_sheet)
    # balance_sheet_page = requests.get('%s' % ''.join(balance_sheet))
    # tree = html.fromstring(balance_sheet_page.text)
    # Current_assets_loans_advances = tree.xpath('/html/body/div[2]/div[5]/table/tbody/tr[20]/td[3]/text()')
    # print Current_assets_loans_advances
    

if __name__ == '__main__':
    main()
    
    
    
    