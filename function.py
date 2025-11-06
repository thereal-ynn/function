def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    
    Args:
        price (float): The original price of the item
        discount_percent (float): The discount percentage
    
    Returns:
        float: The final price after discount (if applicable), otherwise original price
    """
    # Check if discount is 20% or higher
    if discount_percent >= 20:
        # Calculate discount amount and final price
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Return original price if discount is less than 20%
        return price


# Main program to get user input and display results
def main():
    # Get user input
    try:
        original_price = float(input("Enter the original price of the item: $"))
        discount_percentage = float(input("Enter the discount percentage: "))
        
        # Calculate final price using the function
        final_price = calculate_discount(original_price, discount_percentage)
        
        # Display results
        if discount_percentage >= 20:
            print(f"Original price: ${original_price:.2f}")
            print(f"Discount applied: {discount_percentage}%")
            print(f"Final price after discount: ${final_price:.2f}")
        else:
            print(f"No discount applied (needs to be 20% or higher)")
            print(f"Final price: ${final_price:.2f}")
            
    except ValueError:
        print("Please enter valid numbers for price and discount percentage.")


# Run the program
if __name__ == "__main__":
    main()