def calculate_discount(price, discount):
    """
    Calculate final price after applying a discount.
    Accepts any numeric type (int, float).
    """
    return price * (1 - discount / 100)

def main():
    print("Original price: 100, discount 20% ->", calculate_discount(100, 20))
    print("Original price: 59.99, discount 15% ->", calculate_discount(59.99, 15))
    print("Original price: 200, discount 5.5% ->", calculate_discount(200, 5.5))

if __name__ == "__main__":
    main()
