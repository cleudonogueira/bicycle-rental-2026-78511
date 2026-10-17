from bicycle import Bicycle

def main():
    print("=== BICYCLE RENTAL SYSTEM ===")

    # Creating bicycles
    b1 = Bicycle("B1", "Mountain Bike", 5.0)
    b2 = Bicycle.from_string("B2, Speed Bike, 7.5")

    # Displaying initial status
    print(b1)
    print(b2)

    print("\n--- Testing Rent and Return ---")
    b1.borrow_item()
    
    # Calculating cost for 3 hours
    cost = b1.calculate_rental_cost(3)
    print(f"Cost for 3 hours: €{cost}")

    b1.return_item()

    print("\n--- Testing Errors and Validation ---")
    # Trying to return a bike that is not rented
    b1.return_item()

    # Trying to pass invalid hours with try/except
    try:
        b1.calculate_rental_cost(-1)
    except ValueError as e:
        print(f"Caught expected error: {e}")

if __name__ == "__main__":
    main()