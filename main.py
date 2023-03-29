import csv
import sys

items = []
sold_items = []
def add_item():
    name = input("Item name: ")
    quantity = input("Item quantity: ")
    unit_name = input("Item unit of measure Eg. l, kg, pcs: ")
    unit_price = input("Item price in PLN: ")
    for item in items:
        if item["name"] != name:
            items.append({"name": name, "quantity": int(quantity), "unit_name": unit_name, "unit_price": float(unit_price)})
            print("Successfully added to warehouse. Current status:")
            show_warehouse()
            break
        else:
            print("Item currently exist in warehouse")
            break

def sell_item(name, quantity_sold):
    for item in items:
        if item["name"] == name:
            item["quantity"] -= quantity_sold
            print(f"Successfully sold {quantity_sold} {item['unit_name']}")
            sold_items.append({"name": name, "quantity": int(quantity_sold), "unit_name": item["unit_name"], "unit_price": float(item["unit_price"])})
            break
        else:
            print("Item doesn't exist in warehouse")
            break

def get_costs():
    costs = [float(item["quantity"]) * float(item["unit_price"]) for item in items]
    return sum(costs)

def get_income():
    costs = [float(item["quantity"]) * float(item["unit_price"]) for item in sold_items]
    return sum(costs)

def show_revenue():
    print(f"Income: {get_income()}")
    print(f"Costs: {get_costs()}")
    print("---------")
    print(f"Revenue: {float(get_income()) - float(get_costs())}")

def exit_warehouse():
    print("Exiting... Bye!")
    exit()

def show_warehouse():
    if len(items) > 0:
        print("""Name\t\t\tQuantity\tUnit\tUnit Price (PLN)
        ---------------------------------------""")
        for x in range(len(items)):
            print(f"{items[x]['name']:<16}{items[x]['quantity']:<12}{items[x]['unit_name']:<8}{items[x]['unit_price']}")
    else:
        print("No items in warehouse")

def export_items_to_csv():
    with open("warehouse_data.csv", "w", newline="") as csvfile:
        fieldnames = ["name", "quantity", "unit_name", "unit_price"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in items:
            writer.writerow(item)
        print("Successfully saved items data")

def export_sales_to_csv():
    with open("sales_data.csv", "w", newline="") as csvfile:
        fieldnames = ["name", "quantity", "unit_name", "unit_price"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in sold_items:
            writer.writerow(item)
        print("Successfully saved sales data")

def load_items_from_csv(csv_path=""):
    items.clear()
    sold_items.clear()
    if not csv_path:
        with open("warehouse_data.csv", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                items.append(row)
            print("Successfully loaded data from warehouse_data.csv")

        with open("sales_data.csv", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                sold_items.append(row)
            print("Successfully loaded data from sales_data.csv")
    else:
        with open(csv_path, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                items.append(row)
            print(f"Successfully loaded data from {csv_path}")


if __name__ == '__main__':
    if len(sys.argv) == 1:
        pass
    else:
        csv_path = sys.argv[1]
        load_items_from_csv(csv_path)
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
        if inp == "show_revenue":
            show_revenue()
        if inp == "save":
            export_items_to_csv()
            export_sales_to_csv()
        if inp == "load":
            load_items_from_csv()
        if inp == "exit":
            exit_warehouse()