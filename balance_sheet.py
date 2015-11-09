from try_module import trying as trying
from try_module import get_correct_ratio

class BalanceSheet:
    
    def __init__(self, tree):
        self.tree = tree
            
    def get_current_assets_loans_advances(self, tree):
        current_assets_loans_advances1 = trying(tree, '/html/body/div[2]/div[5]/table/tbody/tr[20]/td[2]/text()')
        current_assets_loans_advances2 = trying(tree, '/html/body/div[2]/div[5]/table/tbody/tr[20]/td[3]/text()')
        return get_correct_ratio(current_assets_loans_advances1, current_assets_loans_advances2)
        
    def get_current_liabilities_and_provisions(self, tree):
        current_liabilities_and_provisions = trying(tree, '/html/body/div[2]/div[5]/table/tbody/tr[21]/td[2]/text()')
        return current_liabilities_and_provisions
         
    def get_total_net_current_assets(self, tree):
        return trying(tree, '/html/body/div[2]/div[5]/table/tbody/tr[22]/td[2]/text()')