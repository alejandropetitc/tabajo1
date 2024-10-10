class Cat:
    def __init__(self, nom, desc):
        self.nom = nom
        self.desc = desc
        self.prods = []

    def agrProd(self, prod):
        if prod not in self.prods:
            self.prods.append(prod)
            prod.setCat(self)

    def elimProd(self, prod):
        if prod in self.prods:
            self.prods.remove(prod)
            prod.setCat(None)

    # Consulta la información completa de la categoría
    def consInfo(self):
        prods_noms = [prod.nom for prod in self.prods]
        return {
            "nom": self.nom,
            "desc": self.desc,
            "prods": prods_noms
        }
