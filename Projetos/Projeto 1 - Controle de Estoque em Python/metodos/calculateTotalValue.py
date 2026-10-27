def calculate_total_value(products):
    total_value = sum(product['price'] * product['quantity'] for product in products.values())
    print(f"Total inventory value: {total_value}")