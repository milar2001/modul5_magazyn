items = []
def add_item():
    name = input("Item name: ")
    quantity = input("Item quantity: ")
    unit_name = input("Item unit of measure Eg. l, kg, pcs: ")
    unit_price = input("Item price in PLN: ")
    items.append({"name": name, "quantity": quantity, "unit_name": unit_name, "unit_price": unit_price})
    print("Successfully added to warehouse. Current status:")
    show_warehouse()

def exit_warehouse():
    print("Exiting... Bye!")
    exit()

def show_warehouse():
    print("Name\tQuantity\tUnit\tUnit Price (PLN)")
    for x in range(len(items)):
        print(f"{items[x]['name']}\t{items[x]['quantity']}\t{items[x]['unit_name']}\t{items[x]['unit_price']}")

if __name__ == '__main__':
    while True:
        inp = input("What would you like to do? ")
        if inp == "add":
            add_item()
        if inp == "show":
            show_warehouse()
        if inp == "exit":
            exit_warehouse()
