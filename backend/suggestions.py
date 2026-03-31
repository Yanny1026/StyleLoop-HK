def suggest_clothing_categories(temperature, humidity):
    """
    Suggests clothing categories based on temperature and humidity.
    
    Args:
        temperature (float): Temperature in Celsius
        humidity (float): Humidity percentage
    
    Returns:
        list: List of suggested clothing categories
    """
    suggestions = []
    
    if temperature is None or humidity is None:
        return ["Unable to fetch weather data"]
    
    # Temperature-based suggestions
    if temperature < 15:
        suggestions.append("Warm layers (e.g., jackets, sweaters)")
    elif 15 <= temperature < 20:
        suggestions.append("Light layers (e.g., cardigans, long sleeves)")
    elif 20 <= temperature < 25:
        suggestions.append("Comfortable casual wear")
    else:  # > 25
        suggestions.append("Light and airy clothing (e.g., shorts, t-shirts)")
    
    # Humidity-based suggestions
    if humidity > 80:
        suggestions.append("Breathable fabrics (e.g., cotton, linen)")
    elif humidity > 60:
        suggestions.append("Moisture-wicking materials")
    
    # Additional suggestions for extreme conditions
    if temperature < 10:
        suggestions.append("Heavy winter clothing")
    if humidity > 90:
        suggestions.append("Quick-dry fabrics")
    
    return suggestions