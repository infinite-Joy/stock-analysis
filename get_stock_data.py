from __future__ import print_function
from sys import argv
from lxml import html
import requests
import time
import multiprocessing

# logging
import logging
logging.basicConfig(filename='log/exception_logging.txt', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

from company_page import CompanyPage
from balance_sheet import BalanceSheet
from ratio_module import Ratio

# constants
MIN_PE_THRESHOLD = 0
MAX_PE_THRESHOLD = 15
MIN_EPS_THRESHOLD = 0


def _get_company_primary_stats(company, tree):
    pe_ratio = company.get_pe_ratio(tree)
    eps = company.get_eps(tree)
    price_of_stock = company.get_price_of_stock(tree)
    fifty_two_wk_high = company.get_fifty_two_wk_high(tree)
    fifty_two_wk_low = company.get_fifty_two_wk_low(tree)
    return {'pe_ratio': pe_ratio,
            'eps': eps,
            'price_of_stock': price_of_stock,
            'fifty_two_wk_high': fifty_two_wk_high,
            'fifty_two_wk_low': fifty_two_wk_low}


def company_page_analysis(stock_company):
    try:
        page = requests.get('http://money.rediff.com/%s' % stock_company)
        time.sleep(2)
        tree = html.fromstring(page.content)
        company = CompanyPage(tree)
        primary_stats = _get_company_primary_stats(company, tree)
        pe_ratio_min = primary_stats.get('pe_ratio') > MIN_PE_THRESHOLD
        pe_ratio_max = primary_stats.get('pe_ratio') < MAX_PE_THRESHOLD
        eps_cond = primary_stats.get('eps') > MIN_EPS_THRESHOLD
        price_somewhr_in_middle = (
            primary_stats.get('price_of_stock') < (
                (primary_stats.get('fifty_two_wk_high') +
                 primary_stats.get('fifty_two_wk_low'))/2
            )
        )
        print('primary_stats: {}'.format(primary_stats))
        conditions = [pe_ratio_min, pe_ratio_max, eps_cond, price_somewhr_in_middle]
        print('all_conditions: {}'.format(conditions))
        if all(conditions):
            # get all links
            balance_sheet_link = company.get_balance_sheet_link(tree)
            dividend_link = company.get_dividend_link(tree)
            ratio_link = company.get_ratio_link(tree)

            # go to balance sheet page for further analysis
            balance_sheet_page = requests.get('%s' % ''.join(balance_sheet_link))
            balance_sheet_tree = html.fromstring(balance_sheet_page.content)
            balance_sheet = BalanceSheet(balance_sheet_tree)
            current_assets_loans_advances = balance_sheet.get_current_assets_loans_advances(balance_sheet_tree)
            current_liabilities_and_provisions = balance_sheet.get_current_liabilities_and_provisions(balance_sheet_tree)
            total_net_current_assets = balance_sheet.get_total_net_current_assets(balance_sheet_tree)
            print('{stock_company} has '
                  'total_net_current_assets: {total_net_current_assets}'
                  'and current_liabilities_and_provisions: '
                  '{current_liabilities_and_provisions}'.format(
                      stock_company=stock_company,
                      total_net_current_assets=total_net_current_assets,
                      current_liabilities_and_provisions=current_liabilities_and_provisions
                  ))
            if total_net_current_assets > current_liabilities_and_provisions:
                # go to ratio page
                ratio_page = requests.get('%s' % ''.join(ratio_link))
                ratio_tree = html.fromstring(ratio_page.content)
                ratio = Ratio(ratio_tree)
                if ratio.consistent_dividend_payout(ratio_tree):
                    print(stock_company)
    except Exception as err:
        logger.error(err)
    return


def companies_to_investigate():
    companies = []
    f = open('top_500_companies.txt', 'r')
    for company in f:
        companies.append(company)

    return companies


if __name__ == '__main__':
    if len(argv) > 1:
        stock_companies = argv[1:]
    else:
        stock_companies = companies_to_investigate()
    # jobs = []
    # pool = multiprocessing.Pool(processes=10)
    # for stock_company in stock_companies:
    #     pool.apply_async(company_page_analysis, args=(stock_company,))
    # pool.close()
    # pool.join()
    for company in stock_companies:
        import time
        time.sleep(1)
        print(company)
        company_page_analysis(company)
        print('###################################')
