from try_module import trying as trying


class Ratio:

    def __init__(self, tree):
        self.tree = tree

    def get_present_year_dividend_present_year_dividend_per_share(self, tree):
        p1 = trying(
            tree, '//*[@id="leftcontainer"]/table/tbody/tr[6]/td[2]'
        )
        return p1

    def get_present_year_dividend_present_year_dividend_per_share_minus1(
        self, tree
    ):
        p2 = trying(
            tree, '//*[@id="leftcontainer"]/table/tbody/tr[6]/td[3]'
        )
        return p2

    def get_present_year_dividend_present_year_dividend_per_share_minus2(
        self, tree
    ):
        p3 = trying(
            tree, '//*[@id="leftcontainer"]/table/tbody/tr[6]/td[4]'
        )
        return p3

    def get_present_year_dividend_present_year_dividend_per_share_minus3(
        self, tree
    ):
        return trying(
            tree, '//*[@id="leftcontainer"]/table/tbody/tr[6]/td[5]'
        )

    def get_present_year_dividend_present_year_dividend_per_share_minus4(
        self, tree
    ):
        return trying(
            tree, '//*[@id="leftcontainer"]/table/tbody/tr[6]/td[6]'
        )

    def consistent_dividend_payout(self, tree):
        all_dividends = list(map(
            lambda f: f(tree) > 0,
            [self.get_present_year_dividend_present_year_dividend_per_share,
             self.get_present_year_dividend_present_year_dividend_per_share_minus1,
             self.get_present_year_dividend_present_year_dividend_per_share_minus2,
             self.get_present_year_dividend_present_year_dividend_per_share_minus3,
             self.get_present_year_dividend_present_year_dividend_per_share_minus4]
        ))
        return all(all_dividends)
