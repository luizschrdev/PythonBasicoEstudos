def search_product(productId, products):
    if productId in products:
        product = products[productId]
        print(f"Product found: ID: {product['id']}, Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")
        return    
    print("Product not found.")
    return