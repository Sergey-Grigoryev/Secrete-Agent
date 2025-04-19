from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut


def get_country_from_coordinates(latitude, longitude):
    """
    Returns the country for the given latitude and longitude.

    Args:
        latitude (float): The latitude of the location.
        longitude (float): The longitude of the location.

    Returns:
        str: The name of the country, or an error message if not found.
    """
    geolocator = Nominatim(user_agent="geoapiExercises")
    try:
        # Perform reverse geocoding
        location = geolocator.reverse((latitude, longitude), language="en")
        if location and "country" in location.raw["address"]:
            return location.raw["address"]["country"]
        else:
            return "Country not found for the given coordinates."
    except GeocoderTimedOut:
        return "Error: Geocoding service timed out."
    except Exception as e:
        return f"Error: {e}"
