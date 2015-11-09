from lxml import html
import requests
import time

from get_stock_data import get_company_primary_stats
from company_page import CompanyPage

stock_company = "Amtek-Auto-Ltd"
page = requests.get('http://money.rediff.com/%s' % stock_company)
tree = html.fromstring(page.text)
company = CompanyPage(tree)

def test_get_company_primary_stats():
    primary_stats = get_company_primary_stats(company, tree)
    assert all([primary_stats.get('pe_ratio') > 0, primary_stats.get('eps') > 0, primary_stats.get('price_of_stock') > 0, primary_stats.get('fifty_two_wk_high') > 0, primary_stats.get('fifty_two_wk_low') > 0])