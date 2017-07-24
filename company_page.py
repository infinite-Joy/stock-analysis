from try_module import trying as trying
from try_module import get_correct_ratio

class CompanyPage:

    def __init__(self, tree):
        self.tree = tree


    def _get_correct_ratio(self, tree, x_path_first_part, x_path_sec_part):
        ratio_not_found = True
        i = 8
        while ratio_not_found == True and i > 0:
            x_path = x_path_first_part + str(i) + x_path_sec_part
            ratio = trying(tree, x_path)
            if ratio != 0.00:
                ratio_not_found = False
            i = i - 1
        return ratio


    def get_pe_ratio(self, tree):
        pe_ratio = trying(tree, '//*[@id="div_rcard_more"]/div[1]/div[2]')
        import pdb
        pdb.set_trace()
        return pe_ratio
        # return self._get_correct_ratio(tree, '/html/body/div[4]/div[8]/div[', ']/div[1]/div/div[1]/div[2]/text()')


    def get_eps(self, tree):
        return self._get_correct_ratio(tree, '/html/body/div[4]/div[8]/div[', ']/div[1]/div/div[2]/div[2]/text()')


    def get_price_of_stock(self, tree):
        return trying(tree, '//*[@id="ltpid"]/text()')


    def get_fifty_two_wk_high(self, tree):
        return float(tree.xpath('//*[@id="FiftyTwoHighlow"]/text()')[0].split()[0].replace(",", ""))


    def get_fifty_two_wk_low(self, tree):
        return float(tree.xpath('//*[@id="FiftyTwoHighlow"]/text()')[0].split()[-1].replace(",", ""))


    def get_balance_sheet_link(self, tree):
        try:
            balance_sheet_link1 = tree.xpath('/html/body/div[4]/div[8]/div[8]/div[2]/div/a[4]/@href')[0]
        except:
            balance_sheet_link1 = ""

        try:
            balance_sheet_link2 = tree.xpath('/html/body/div[4]/div[8]/div[7]/div[2]/div/a[4]/@href')[0]
        except:
            balance_sheet_link2 = ""

        if balance_sheet_link1 is not "":
            return balance_sheet_link1
        elif balance_sheet_link2 is not "":
            return balance_sheet_link2
        else:
            return ""


    def get_dividend_link(self, tree):
        try:
            balance_sheet_link1 = tree.xpath('/html/body/div[4]/div[8]/div[7]/div[2]/div/a[7]/@href')[0]
        except:
            balance_sheet_link1 = ""

        try:
            balance_sheet_link2 = tree.xpath('/html/body/div[4]/div[8]/div[8]/div[2]/div/a[7]/@href')[0]
        except:
            balance_sheet_link2 = ""

        if balance_sheet_link1 is not "":
            return balance_sheet_link1
        elif balance_sheet_link2 is not "":
            return balance_sheet_link2
        else:
            return ""

    def get_ratio_link(self, tree):
        try:
            balance_sheet_link1 = tree.xpath('/html/body/div[4]/div[8]/div[8]/div[2]/div/a[11]/@href')[0]
        except:
            balance_sheet_link1 = ""

        try:
            balance_sheet_link2 = tree.xpath('/html/body/div[4]/div[8]/div[7]/div[2]/div/a[11]/@href')[0]
        except:
            balance_sheet_link2 = ""

        if balance_sheet_link1 is not "":
            return balance_sheet_link1
        elif balance_sheet_link2 is not "":
            return balance_sheet_link2
        else:
            return ""
