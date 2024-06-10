import re
from unidecode import unidecode

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
    str: The engine size, e.g., "1.4 Turbo". Returns None if no match is found.
    """

    #Check if car is eletric
    if "eletrico" in unidecode(car_description.lower()):
        return "Elétrico"

    # Define the regular expression pattern to match engine sizes like "1.0", "1.4", etc and check if there is tb (Turbo) in it.
    pattern = r'\b\d\.\d tb\b|\b\d\.\d\b'
    
    # Search for the pattern in the car description
    match = re.search(pattern, car_description.lower())

    #If "tb" in match, replace it with Turbo
    result = match.group().replace("tb", "Turbo") if match else None

    # Check if engine is turbo
    is_turbo = " Turbo" if match and 'turbo' in car_description.lower() and "Turbo" not in result else ""
    
    # If a match is found, return the matched string; otherwise, return None
    return result + is_turbo