def create_product():

    productId = input("Enter the product ID: ").strip()

    productName = input("Enter the product name: ").strip()

    while not productName:
        print("The product name cannot be empty. Please try again.")
        productName = input("Enter the product name: ").strip()

    productPrice = float(input("Enter the product price: "))
    while productPrice < 0:
        print("The product price cannot be negative. Please try again.")
        productPrice = float(input("Enter the product price: "))

    productQuantity = int(input("Enter the product quantity: "))
    while productQuantity < 0:
        print("The product quantity cannot be negative. Please try again.")
        productQuantity = int(input("Enter the product quantity: "))

    print(f"Produto cadastrado: {productId}, {productName}, {productPrice}, {productQuantity}")
    return {
        "id": productId,
        "name": productName,
        "price": productPrice,
        "quantity": productQuantity
    }