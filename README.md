# Discount Calculator

A simple Python program that calculates final prices with discount validation.

## Function

```python
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    return price
```

## Features

- Applies discount only if 20% or higher
- User input with validation
- Clear price display

## Usage

Run the script and enter:
1. Original price
2. Discount percentage

**Example:**
```
Enter original price: $100
Enter discount: 25

Discount applied: 25%
Final price: $75.00
```

## Requirements

- Python 3.x
