from producto import Prod

class Bod:
    def __init__(self, nom, ubic, cap_max):
        self.nom = nom
        self.ubic = ubic
        self.cap_max = cap_max
        self.prod_almac = {}

    def agrProd(self, prod: Prod, cant: int):
        if self.capDisp() < cant:
            raise ValueError("No hay suficiente espacio en la bodega.")
        if prod in self.prod_almac:
            self.prod_almac[prod] += cant
        else:
            self.prod_almac[prod] = cant

    def retProd(self, prod: Prod, cant: int):
        if prod not in self.prod_almac or self.prod_almac[prod] < cant:
            raise ValueError("Cantidad a retirar excede el stock disponible.")
        self.prod_almac[prod] -= cant
        if self.prod_almac[prod] == 0:
            del self.prod_almac[prod]

    def consDisp(self, prod: Prod):
        return self.prod_almac.get(prod, 0)

    def capDisp(self):
        total_ocup = sum(self.prod_almac.values())
        return self.cap_max - total_ocup

    # Consulta la información completa de la bodega
    def consInfo(self):
        prods = {prod.nom: cant for prod, cant in self.prod_almac.items()}
        return {
            "nom": self.nom,
            "ubic": self.ubic,
            "cap_max": self.cap_max,
            "prod_almac": prods
        }
