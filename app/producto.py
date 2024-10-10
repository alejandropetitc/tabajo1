from categoria import Cat

# stocki = stock inicial
class Prod:
    def __init__(self, nom, desc, pre, stocki):
        self.nom = nom
        self.desc = desc
        self.pre = pre
        self.stocki = stocki
        self.cat = None
        self.provs = []

    def agrStock(self, cant):
        self.stocki += cant

    def retStock(self, cant):
        if cant > self.stocki:
            raise ValueError("Cantidad a retirar excede el stock disponible.")
        self.stocki -= cant

    def calcStock(self):
        return self.pre * self.stocki

    def setCat(self, cat: Cat):
        self.cat = cat

    def consInfo(self):
        provs_noms = [prov.nom for prov in self.provs]
        return {
            "nom": self.nom,
            "desc": self.desc,
            "pre": self.pre,
            "stock_actual": self.stocki,
            "cat": self.cat.nom if self.cat else "Sin categoría",
            "provs": provs_noms
        }