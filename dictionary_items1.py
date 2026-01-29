cart = {
    "client": "Ion",
    "products": [],
    "total": 0
}

product1 = {
    "name": "PC",
    "price": 1200,
    "qty": 1
}

product2 = {
    "name": "Camera",
    "price": 25,
    "qty": 2
}

product3 = {
    "name": "Keyboard",
    "price": 75,
    "qty": 1
}

cart["products"]. append (product1)
cart["products"].append(product2)
cart["products"]. append(product3)

for product in cart["products"]:
    print("Produs:")
    for key, value in product.items():
        print(key, ":", value)
        print('_________')

print("Total:", cart["total"])

cart["products"] [1] ["qty"] = 3 # Mouse


total = 0
for product in cart["products"]:
    total = total + product["price"] * product["qty"]

cart["total"] = total

print("Total dupa modificare:", cart["total"])