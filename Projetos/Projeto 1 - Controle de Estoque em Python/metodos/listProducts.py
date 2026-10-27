def list_products(products):
        if not products:
            print("Product list is empty.")
        else:
            print("Produtos cadastrados:")
            for product in products.values():
                print(f"ID: {product['id']}, | "
                        f"Nome: {product['name']}, | "
                        f"Preço: {product['price']}, | "
                        f"Quantidade: {product['quantity']}")
