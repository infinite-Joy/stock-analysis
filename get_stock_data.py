from lxml import html
import requests
import time

from company_page import CompanyPage

def get_company_primary_stats(tree):
    company = CompanyPage(tree)
    pe_ratio = company.get_pe_ratio(tree)
    eps = company.get_eps(tree)
    price_of_stock = company.get_price_of_stock(tree)
    fifty_two_wk_high = company.get_fifty_two_wk_high(tree)
    fifty_two_wk_low = company.get_fifty_two_wk_low(tree)
    return {'pe_ratio': pe_ratio, 'eps': eps, 'price_of_stock': price_of_stock, 'fifty_two_wk_high': fifty_two_wk_high, 'fifty_two_wk_low': fifty_two_wk_low}

def company_page_analysis(stock_company):
    page = requests.get('http://money.rediff.com/%s' % stock_company)
    time.sleep(2)
    tree = html.fromstring(page.text)
    primary_stats = get_company_primary_stats(tree)
    print primary_stats
    if all([primary_stats.get('pe_ratio') < 15, primary_stats.get('eps') > 0, primary_stats.get('price_of_stock') < ((primary_stats.get('fifty_two_wk_high') - primary_stats.get('fifty_two_wk_low'))/2)]):
        # go to next page
        return stock_company
    else:
        pass

def main():
    stock_companies = ["Amtek-Auto-Ltd"]
    companies_to_invest = []
    for stock_company in stock_companies:
        companies_to_invest.append(company_page_analysis(stock_company))
    print companies_to_invest
    
    # balance_sheet = tree.xpath('/html/body/div[4]/div[8]/div[8]/div[2]/div/a[4]/@href')
    # print "".join(balance_sheet)
    # balance_sheet_page = requests.get('%s' % ''.join(balance_sheet))
    # tree = html.fromstring(balance_sheet_page.text)
    # Current_assets_loans_advances = tree.xpath('/html/body/div[2]/div[5]/table/tbody/tr[20]/td[3]/text()')
    # print Current_assets_loans_advances
    

if __name__ == '__main__':
    main()
    
    
    
    