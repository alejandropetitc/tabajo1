class InfStock:
    def __init__(self, prods, cats, provs, bods):
        self.prods = prods
        self.cats = cats
        self.provs = provs
        self.bods = bods

    def genInfStockTotal(self):
        total_stock = sum([prod.stocki for prod in self.prods])
        return {"stock_total": total_stock}

    def genInfStockPorCat(self):
        inf = {}
        for cat in self.cats:
            stock_cat = sum([prod.stocki for prod in cat.prods])
            inf[cat.nom] = stock_cat
        return inf

    def genInfStockPorProv(self):
        inf = {}
        for prov in self.provs:
            stock_prov = sum([prod.stocki for prod in prov.prods])
            inf[prov.nom] = stock_prov
        return inf

    def genInfStockPorBod(self):
        inf = {}
        for bod in self.bods:
            stock_bod = sum(bod.prod_almac.values())
            inf[bod.nom] = stock_bod
        return inf
