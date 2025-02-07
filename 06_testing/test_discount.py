"""Applies a discount to a given price."""


def apply_discount(price, discount):
    """
    Applies a discount to the given price.
    
    :param price: Original price (float or int)
    :param discount: Discount percentage (0-100)
    :return: Discounted price (float)
    """
    if not (0 <= discount <= 100):
        raise ValueError("Discount must be between 0 and 100")
    return round(price * (1 - discount / 100), 2)
