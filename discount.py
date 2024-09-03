def calculate_discount(price, discount_percent):
    # Check if the discount percentage is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate and return the final price after discount
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price

# Prompt the user for the original price of the item
price = float(input("Enter the original price of the item: "))

# Prompt the user for the discount percentage
discount_percent = float(input("Enter the discount percentage: "))

# Call the calculate_discount function to get the final price
final_price = calculate_discount(price, discount_percent)

# Print the final price
if final_price == price:
    print(f"No discount applied. The final price is: ${final_price:.2f}")
else:
    print(f"The final price after applying the discount is: ${final_price:.2f}")