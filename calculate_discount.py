#Question number 1

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price

# Example calls:
print(calculate_discount(100, 25))  # Should print 75.0
print(calculate_discount(100, 10))  # Should print 100
