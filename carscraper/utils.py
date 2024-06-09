import re

def extract_number(price_text):
    """
    Extracts and converts a price string to a float.
    
    Args:
    price_text (str): The price string to be processed, e.g., "Preço R$ 73.480,00".
    
    Returns:
    float: The price as a float, e.g., 73480.00.
    """
    # Remove all non-numeric characters except for ',' and '.'
    cleaned_price = re.sub(r'[^\d,]', '', price_text)
    
    # Replace the comma with a period to convert to a float
    cleaned_price = cleaned_price.replace('.', '').replace(',', '.')
    
    # Convert the cleaned string to a float
    price_float = float(cleaned_price)
    
    return price_float
    
    
def extract_engine_size(car_description):
    """
    Extracts the engine size from a car description string.
    
    Args:
    car_description (str): The car description string, e.g., "TRACKER LT 1.4 Turbo 16V Flex 4x".
    
    Returns:
    str: The engine size, e.g., "1.4". Returns None if no match is found.
    """
    # Define the regular expression pattern to match engine sizes like "1.0", "1.4", etc.
    pattern = r'\b\d\.\d\b'
    
    # Search for the pattern in the car description
    match = re.search(pattern, car_description)
    
    # If a match is found, return the matched string; otherwise, return None
    return match.group() if match else None