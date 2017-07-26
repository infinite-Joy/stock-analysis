from try_module import trying as trying


class CompanyPage:

    def __init__(self, tree):
        self.tree = tree

    def _get_correct_ratio(self, tree, x_path_first_part, x_path_sec_part):
        ratio_not_found = True
        i = 8
        while ratio_not_found and i > 0:
            x_path = x_path_first_part + str(i) + x_path_sec_part
            ratio = trying(tree, x_path)
            if ratio != 0.00:
                ratio_not_found = False
            i = i - 1
        return ratio

    def get_pe_ratio(self, tree):
        pe_ratio = trying(tree, '//*[@id="div_rcard_more"]/div[1]/div[2]')
        return pe_ratio

    def get_eps(self, tree):
        eps = trying(tree, '//*[@id="div_rcard_more"]/div[2]/div[2]')
        return eps

    def get_price_of_stock(self, tree):
        pos = trying(tree, '//*[@id="ltpid"]')
        return pos

    def get_fifty_two_wk_high(self, tree):
        return (
            float(
                tree.xpath('//*[@id="FiftyTwoHighlow"]/text()')[0]
                .split()[0]
                .replace(",", "")
            )
        )

    def get_fifty_two_wk_low(self, tree):
        return (
            float(
                tree.xpath('//*[@id="FiftyTwoHighlow"]/text()')[0]
                .split()[-1]
                .replace(",", "")
            )
        )

    def get_balance_sheet_link(self, tree):
        try:
            balance_sheet_links = (
                tree
                .xpath(
                    '//*[@id="div_res_centre_more"]/a[4]'
                )
            )
            balance_sheet_link1 = balance_sheet_links[0].attrib['href']
        except KeyError:
            balance_sheet_link1 = ""
        return balance_sheet_link1

    def get_dividend_link(self, tree):
        import pdb
        pdb.set_trace()
        try:
            balance_sheet_links = (
                tree
                .xpath(
                    '//*[@id="div_res_centre_more"]/a[14]'
                )
            )
            balance_sheet_link1 = balance_sheet_links[0].attrib['href']
        except KeyError:
            balance_sheet_link1 = ""
        return balance_sheet_link1

    def get_ratio_link(self, tree):
        try:
            balance_sheet_link1 = tree.xpath('/html/body/div[4]/div[8]/div[8]'
                                             '/div[2]/div/a[11]/@href')[0]
        except KeyError:
            balance_sheet_link1 = ""

        try:
            balance_sheet_link2 = tree.xpath('/html/body/div[4]/div[8]/div[7]'
                                             '/div[2]/div/a[11]/@href')[0]
        except KeyError:
            balance_sheet_link2 = ""

        if balance_sheet_link1 is not "":
            return balance_sheet_link1
        elif balance_sheet_link2 is not "":
            return balance_sheet_link2
        else:
            return ""
