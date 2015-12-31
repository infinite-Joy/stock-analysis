from lxml import html
import os

from balance_sheet import BalanceSheet

f = open(r"G:\Python\projects\stock_analysis\stock_analysis\tests\balance_sheet_page_content")
balance_sheet_page_content = f.read()
f.close()

balance_sheet_tree = html.fromstring(balance_sheet_page_content)
balance_sheet = BalanceSheet(balance_sheet_tree)


def test_get_current_assets_loans_advances():
    current_assets_loans_advances = balance_sheet.get_current_assets_loans_advances(balance_sheet_tree)
    assert current_assets_loans_advances != 0.00
    assert isinstance(current_assets_loans_advances, float)
    
def test_get_current_liabilities_and_provisions():
    current_liabilities_and_provisions = balance_sheet.get_current_liabilities_and_provisions(balance_sheet_tree)
    assert current_liabilities_and_provisions != 0.00
    assert isinstance(current_liabilities_and_provisions, float)
    
def test_get_total_net_current_assets():
    total_net_current_assets = balance_sheet.get_total_net_current_assets(balance_sheet_tree)
    assert total_net_current_assets != 0.00
    assert isinstance(total_net_current_assets, float)