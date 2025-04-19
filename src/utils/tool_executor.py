from gadgets.decryptor import decrypt_message
from gadgets.weather import get_weather
from gadgets.translate import translate_to_english
from gadgets.lat_long_lookup import get_country_from_coordinates


def execute_tool(tool_name, parameters):
    """
    - Extract parameters
    - Execute the requested tool
    - Return the result.
    """

    if tool_name == "weather":
        # Extract parameters for the weather tool
        city = parameters.get("city")
        if not city:
            return "Error: 'city' parameter is required for the weather tool."
        # Execute the weather tool
        result = get_weather(city)

    elif tool_name == "decrypt":
        # Extract parameters for the decryptor tool
        encrypted_message = parameters.get("encrypted_message")
        if not encrypted_message:
            return "Error: 'encrypted_message' parameter is required for the decrypt tool."
        # Execute the decryptor tool
        result = decrypt_message(encrypted_message)

    elif tool_name == "translate":
        # Extract parameters for the translate tool
        text = parameters.get("text")
        if not text:
            return "Error: 'text' parameter is required for the translate tool."
        # Execute the translate tool
        result = translate_to_english(text)

    elif tool_name == "lat_long_lookup":
        # Extract parameters for the lat_long_lookup tool
        latitude = parameters.get("latitude")
        longitude = parameters.get("longitude")
        if latitude is None or longitude is None:
            return "Error: 'latitude' and 'longitude' parameters are required for the lat_long_lookup tool."
        # Execute the lat_long_lookup tool
        result = get_country_from_coordinates(latitude, longitude)
    else:
        result = "Unknown tool requested."

    return result
