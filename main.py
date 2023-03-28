items = [{"name": "cebula", "quantity": 99, "unit_name": "kg", "unit_price": 4.5},
         {"name": "papryka", "quantity": 44, "unit_name": "kg", "unit_price": 4}]
def add_item():
    name = input("Item name: ")
    quantity = input("Item quantity: ")
    unit_name = input("Item unit of measure Eg. l, kg, pcs: ")
    unit_price = input("Item price in PLN: ")
    items.append({"name": name, "quantity": int(quantity), "unit_name": unit_name, "unit_price": float(unit_price)})

    print("Successfully added to warehouse. Current status:")
    show_warehouse()

def sell_item(name, quantity_sold):
    for item in items:
        if item["name"] == name:
            item["quantity"] -= quantity_sold
            print(f"Successfully sold {quantity_sold} {item['unit_name']}")



def exit_warehouse():
    print("Exiting... Bye!")
    exit()

def show_warehouse():
    print("""Name\t\t\tQuantity\tUnit\tUnit Price (PLN)
    ---------------------------------------""")
    for x in range(len(items)):
        print(f"{items[x]['name']:<16}{items[x]['quantity']:<12}{items[x]['unit_name']:<8}{items[x]['unit_price']}")



if __name__ == '__main__':
    while True:
        inp = input("What would you like to do? ")
        if inp == "add":
            add_item()
        if inp == "sell":
            name = input("Item name: ")
            quantity_sold = input("Quantity to sell: ")
            sell_item(name, int(quantity_sold))
        if inp == "show":
            show_warehouse()
        if inp == "exit":
            exit_warehouse()
