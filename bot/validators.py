def validate_side(side: str) -> bool:
    """Checks if the user typed BUY or SELL."""
    valid_sides = ["BUY", "SELL"]
    if side.upper() in valid_sides:
        return True
    return False

def validate_quantity(quantity: str) -> bool:
    """Checks if the quantity is a valid positive number."""
    try:
        qty = float(quantity)
        if qty > 0:
            return True
        return False
    except ValueError:
        return False

def validate_price(price: str) -> bool:
    """Checks if the price is a valid positive number."""
    try:
        p = float(price)
        if p > 0:
            return True
        return False
    except ValueError:
        return False
