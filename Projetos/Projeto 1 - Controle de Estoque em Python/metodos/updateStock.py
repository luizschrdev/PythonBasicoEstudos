def update_stock(productId, products):
    if productId in products:
        product = products[productId]
        print(f"Current stock for {product['name']}: {product['quantity']}")
        new_quantity = int(input("Enter new stock quantity: "))
        product['quantity'] = new_quantity
        print("Stock updated successfully.")
        return
    else:
        print("Product not found.")
        return