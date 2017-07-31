from try_module import trying as trying


class CompanyPage:

    def __init__(self, tree):
        self.tree = tree

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

    def _sheet_links(self, tree, this_xpath):
        """TODO: Docstring for _sheet_links.

        :tree: TODO
        :xpath: TODO
        :returns: TODO

        """
        try:
            _sheet_links = (tree.xpath(this_xpath))
            _sheet_link = _sheet_links[0].attrib['href']
        except KeyError:
            _sheet_link = ""
        return _sheet_link

    def get_balance_sheet_link(self, tree):
        return self._sheet_links(tree, '//*[@id="div_res_centre_more"]/a[4]')

    def get_ratio_link(self, tree):
        return self._sheet_links(tree, '//*[@id="div_res_centre_more"]/a[11]')
