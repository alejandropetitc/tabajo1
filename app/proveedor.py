from producto import Prod

class Prov:
    def __init__(self, nom, dir, tel):
        self.nom = nom
        self.dir = dir
        self.tel = tel
        self.prods = []

    def agrProdSumin(self, prod: Prod):
        if prod not in self.prods:
            self.prods.append(prod)

    def elimProdSumin(self, prod: Prod):
        if prod in self.prods:
            self.prods.remove(prod)

    # Consulta la información completa del proveedor
    def consInfo(self):
        prods_noms = [prod.nom for prod in self.prods]
        return {
            "nom": self.nom,
            "dir": self.dir,
            "tel": self.tel,
            "prods_suministrados": prods_noms
        }
