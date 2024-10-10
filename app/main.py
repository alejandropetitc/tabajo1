from producto import Prod
from categoria import Cat
from proveedor import Prov
from bodega import Bod
from informe import InfStock
import random

cats = [
    Cat("Electrónica", "Dispositivos electrónicos"),
    Cat("Ropa", "Prendas de vestir"),
    Cat("Hogar", "Artículos para el hogar"),
    Cat("Juguetes", "Juguetes para niños"),
    Cat("Libros", "Libros de diversas temáticas")
]

provs = [
    Prov("Prov A", "Calle 123", "555-1234"),
    Prov("Prov B", "Avenida 456", "555-5678"),
    Prov("Prov C", "Calle 789", "555-9876")
]

noms_prods = [
    "Smartphone", "Laptop", "Televisor", "Auriculares", "Tablet",
    "Camiseta", "Pantalones", "Chaqueta", "Zapatos", "Sombrero",
    "Sofá", "Mesa", "Silla", "Cama", "Lámpara",
    "Pelota", "Muñeca", "Rompecabezas", "Carro de juguete", "Robot",
    "Novela", "Libro de cocina", "Enciclopedia", "Cómic", "Libro infantil",
    "Cámara", "Consola de videojuegos", "Mouse", "Teclado", "Impresora"
]

prods = []
for i in range(30):
    prod = Prod(
        nom=noms_prods[i],
        desc=f"Descripción del {noms_prods[i]}",
        pre=random.uniform(10.0, 1000.0),
        stocki=random.randint(10, 100)
    )
    prods.append(prod)

for i, prod in enumerate(prods):
    cat = cats[i % len(cats)]
    cat.agrProd(prod)

for i, prod in enumerate(prods):
    prov = provs[i % len(provs)]
    prov.agrProdSumin(prod)

bods = [
    Bod("Bod Central", "Ciudad", 1000),
    Bod("Bod Sur", "Ciudad", 800)
]

for prod in prods:
    cant = random.randint(5, 50)
    bod = random.choice(bods)
    try:
        bod.agrProd(prod, cant)
    except ValueError as e:
        print(f"No se pudo almacenar el producto {prod.nom} en {bod.nom}: {e}")

prod_random = random.choice(prods)
print("\nInformación del producto aleatorio:")
print(prod_random.consInfo())

cat_random = random.choice(cats)
print("\nInformación de la categoría aleatoria:")
print(cat_random.consInfo())


bod_random = random.choice(bods)
print("\nInformación de la bodega aleatoria:")
print(bod_random.consInfo())

inf_stock = InfStock(prods, cats, provs, bods)

print("\nInforme de stock total:")
print(inf_stock.genInfStockTotal())

print("\nInforme de stock por categoría:")
print(inf_stock.genInfStockPorCat())

print("\nInforme de stock por proveedor:")
print(inf_stock.genInfStockPorProv())

print("\nInforme de stock por bodega:")
print(inf_stock.genInfStockPorBod())

Prov_random = random.choice(provs)
print("\nInformación del proveedor aleatorio:")
print(Prov_random.consInfo())