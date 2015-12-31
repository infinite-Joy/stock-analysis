from try_module import trying as trying
from try_module import get_correct_ratio

class Ratio:
    
    def __init__(self, tree):
        self.tree = tree
        
    def get_present_year_dividend_present_year_dividend_per_share(self, tree):
        return trying(tree, '/html/body/div[2]/div[5]/table/tbody/tr[6]/td[2]/text()')
        
    def get_present_year_dividend_present_year_dividend_per_share_minus1(self, tree):
        return trying(tree, '/html/body/div[2]/div[5]/table/tbody/tr[6]/td[3]/text()')
        
    def get_present_year_dividend_present_year_dividend_per_share_minus2(self, tree):
        return trying(tree, '/html/body/div[2]/div[5]/table/tbody/tr[6]/td[4]/text()')
        
    def get_present_year_dividend_present_year_dividend_per_share_minus3(self, tree):
        return trying(tree, '/html/body/div[2]/div[5]/table/tbody/tr[6]/td[5]/text()')
        
    def get_present_year_dividend_present_year_dividend_per_share_minus4(self, tree):
        return trying(tree, '/html/body/div[2]/div[5]/table/tbody/tr[6]/td[6]/text()')
        
    def consistent_dividend_payout(self, tree):
        return True