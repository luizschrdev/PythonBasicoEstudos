def remove_product(productId, products):
        if productId in products:
                del products[productId]
                print("Product removed successfully.")
                return
        else:
                print("Product not found.")
                return
        
