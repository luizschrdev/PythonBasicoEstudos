from metodos.createProducts import create_product
from metodos.listProducts import list_products
from metodos.searchProducts import search_product
from metodos.updateStock import update_stock
from metodos.removeProduct import remove_product
from metodos.calculateTotalValue import calculate_total_value

close = bool(0)
products = {}
while close != 1:
    print("Choose an option:")
    print("1 - Create product")
    print("2 - List products")
    print("3 - Search product")
    print("4 - Update stock")
    print("5 - Remove product")
    print("6 - Calculate total value")
    print("0 - Exit")
    try:
        opcao = int(input("Selected: "))
    
        match opcao:
            case 1:
                product = create_product()
                if product["id"] not in products:
                    products[product["id"]] = product
                else:
                    print("Product with this ID already exists.")
            case 2:
                list_products(products)
            case 3:
                print("Enter product ID:")
                productId = input("Selected: ").strip()
                search_product(productId, products)
            case 4:
                print("Enter product ID:")
                productId = input("Selected: ").strip()
                update_stock(productId, products)
            case 5:
                print("Enter product ID:")
                productId = input("Selected: ").strip()
                remove_product(productId, products)
            case 6:
                calculate_total_value(products)
            case 0:
                close = bool(1)
            case _:
                print("Invalid option. Please try again.")
    except ValueError:
        print("Invalid input. Please enter an integer.")
                

    