from try_module import trying as trying

class CompanyPage:
    
    def __init__(self, tree):
        self.tree = tree
        
    def _get_correct_ratio(self, ratio1, ratio2):
        if ratio1 > 0:
            return ratio1
        elif ratio2 > 0:
            return ratio2
        else:
            return 0
        
    def get_pe_ratio(self, tree):
        pe_ratio1 = trying(tree, '/html/body/div[4]/div[8]/div[8]/div[1]/div/div[1]/div[2]/text()')
        pe_ratio2 = trying(tree, '/html/body/div[4]/div[8]/div[7]/div[1]/div/div[1]/div[2]/text()')
        return self._get_correct_ratio(pe_ratio1, pe_ratio2)
            
    def get_eps(self, tree):
        eps1 = trying(tree, '/html/body/div[4]/div[8]/div[8]/div[1]/div/div[2]/div[2]/text()')
        eps2 = trying(tree, '/html/body/div[4]/div[8]/div[7]/div[1]/div/div[2]/div[2]/text()')
        return self._get_correct_ratio(eps1, eps2)
        
    def get_price_of_stock(self, tree):
        return trying(tree, '//*[@id="ltpid"]/text()')
        
    def get_fifty_two_wk_high(self, tree):
        return float(tree.xpath('//*[@id="FiftyTwoHighlow"]/text()')[0].split()[0])
        
    def get_fifty_two_wk_low(self, tree):
        return float(tree.xpath('//*[@id="FiftyTwoHighlow"]/text()')[0].split()[-1])
