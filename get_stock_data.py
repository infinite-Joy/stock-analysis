from __future__ import print_function
from sys import argv
from lxml import html
import requests
import time
import multiprocessing
import logging

from company_page import CompanyPage
from balance_sheet import BalanceSheet
from ratio_module import Ratio

# logging
logging.basicConfig(
    filename='log/exception_logging.txt',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
)
logger = logging.getLogger(__name__)

# constants
MIN_PE_THRESHOLD = 0
MAX_PE_THRESHOLD = 15
MIN_EPS_THRESHOLD = 0
TESTING = None
MY_RISK_TOLERANCE = 50000  # investment per company


def _get_company_primary_stats(company, tree):
    pe_ratio = company.get_pe_ratio(tree)
    eps = company.get_eps(tree)
    price_of_stock = company.get_price_of_stock(tree)
    fifty_two_wk_high = company.get_fifty_two_wk_high(tree)
    fifty_two_wk_low = company.get_fifty_two_wk_low(tree)
    volume = company.get_volume(tree)
    return {'company': company,
            'volume': volume,
            'pe_ratio': pe_ratio,
            'eps': eps,
            'price_of_stock': price_of_stock,
            'fifty_two_wk_high': fifty_two_wk_high,
            'fifty_two_wk_low': fifty_two_wk_low}


def company_page_analysis(stock_company):
    try:
        page = requests.get('http://money.rediff.com/%s' % stock_company)
        time.sleep(1)
        tree = html.fromstring(page.content)
        company = CompanyPage(tree)
        primary_stats = _get_company_primary_stats(company, tree)

        # PE has to be greater than 0, Negative PE means that the company is
        # not making profit.
        pe_ratio_min = primary_stats.get('pe_ratio') > MIN_PE_THRESHOLD

        # PE has to be less than 15. If greater it means that the company is
        # overpriced.
        pe_ratio_max = primary_stats.get('pe_ratio') < MAX_PE_THRESHOLD

        # Company should be making some profit.
        eps_cond = primary_stats.get('eps') > MIN_EPS_THRESHOLD

        # prices towards the lower range.
        price_somewhr_in_middle = (
            primary_stats.get('price_of_stock') < (
                (primary_stats.get('fifty_two_wk_high') +
                 primary_stats.get('fifty_two_wk_low'))/2
            )
        )

        # total money interchanged greater than 10 times what I will be
        # investing. Else I may not find people that will be willing to buy or
        # sell at the expected rate and there may be too much fluctuation.
        total_money_floating = (
            primary_stats.get('volume') * primary_stats.get('price_of_stock')
        )
        if total_money_floating < 10 * MY_RISK_TOLERANCE:
            return

        if TESTING:
            print('primary_stats: {}'.format(primary_stats))
        conditions = [
            pe_ratio_min, pe_ratio_max, eps_cond, price_somewhr_in_middle
        ]
        if TESTING:
            print('all_conditions: {}'.format(conditions))
        if all(conditions):
            # get all links
            balance_sheet_link = company.get_balance_sheet_link(tree)
            ratio_link = company.get_ratio_link(tree)

            # go to balance sheet page for further analysis
            balance_sheet_page = requests.get(
                '%s' % ''.join(balance_sheet_link)
            )
            balance_sheet_tree = html.fromstring(balance_sheet_page.content)
            balance_sheet = BalanceSheet(balance_sheet_tree)
            current_liabilities_and_provisions = (
                balance_sheet
                .get_current_liabilities_and_provisions(balance_sheet_tree)
            )
            total_net_current_assets = (
                balance_sheet.get_total_net_current_assets(balance_sheet_tree)
            )
            if TESTING:
                print('{stock_company} has '
                      'total_net_current_assets: {total_net_current_assets}'
                      'and current_liabilities_and_provisions: '
                      '{current_liabilities_and_provisions}'.format(
                          stock_company=stock_company,
                          total_net_current_assets=total_net_current_assets,
                          current_liabilities_and_provisions=current_liabilities_and_provisions
                      ))
            if total_net_current_assets > current_liabilities_and_provisions:
                if TESTING:
                    print(
                        'company {} has net asset greater than net liabilities'
                        .format(stock_company))
                # go to ratio page
                ratio_page = requests.get('%s' % ''.join(ratio_link))
                ratio_tree = html.fromstring(ratio_page.content)
                ratio = Ratio(ratio_tree)
                if TESTING:
                    print(
                        'ratio consistent_dividend_payout: {}'.format(
                            ratio.consistent_dividend_payout(ratio_tree)))
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
        TESTING = True
    else:
        stock_companies = companies_to_investigate()
    if TESTING:
        for company in stock_companies:
            import time
            time.sleep(1)
            print(company)
            company_page_analysis(company)
            print('###################################')
    else:
        jobs = []
        pool = multiprocessing.Pool(processes=10)
        for stock_company in stock_companies:
            pool.apply_async(company_page_analysis, args=(stock_company,))
        pool.close()
        pool.join()
