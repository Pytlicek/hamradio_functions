"""
@author: 4X5DM
"""

from math import floor

# Constants
ASCII_0 = 48
ASCII_A = 65
ASCII_a = 97


def square_to_location(qth_locator: str) -> tuple[float, float] | None:
    """
    Converts QTH locator to latitude and longitude in decimal format.
    Gets QTH locator as string.
    Returns Tuple containing latitude and longitude as floats.
    """

    # Validate input
    try:
        assert isinstance(qth_locator, str)
        assert len(qth_locator) == 6
    except AssertionError as e:
        # print(f"qth_locator is wrong\n{e}")
        return None

    qth_locator = qth_locator.upper()

    # Separate fields, squares and subsquares

    # Fields
    lon_field = ord(qth_locator[0]) - ASCII_A
    lat_field = ord(qth_locator[1]) - ASCII_A

    # Squares
    lon_sq = ord(qth_locator[2]) - ASCII_0
    lat_sq = ord(qth_locator[3]) - ASCII_0

    # Subsquares
    lon_sub_sq = ord(qth_locator[4]) - ASCII_A
    lat_sub_sq = ord(qth_locator[5]) - ASCII_A

    # Calculate latitude and longitude
    lon = -180.0
    lat = -90.0

    lon += 20.0 * lon_field
    lat += 10.0 * lat_field

    lon += 2.0 * lon_sq
    lat += 1.0 * lat_sq

    lon += 5.0 / 60 * lon_sub_sq
    lat += 2.5 / 60 * lat_sub_sq

    lat = round(lat, 6)
    lon = round(lon, 6)

    return lat, lon


def location_to_square(lat: float, lon: float) -> None | str:
    """
    Converts latitude and longitude in decimal format to QTH locator.
    Gets latitude and longitude as floats.
    Returns QTH locator as string.
    """

    # Validate input
    try:
        assert isinstance(lat, float)
        assert isinstance(lon, float)
        assert -90.0 <= lat <= 90.0
        assert -180.0 <= lon <= 180.0
    except AssertionError as e:
        # print(f"Latitude or Longitude is wrong\n{e}")
        return None

    # Separate fields, squares and subsquares
    lon += 180
    lat += 90

    # Fields
    lon_field = int(floor(lon / 20))
    lat_field = int(floor(lat / 10))

    lon -= lon_field * 20
    lat -= lat_field * 10

    # Squares
    lon_sq = int(floor(lon / 2))
    lat_sq = int(floor(lat / 1))

    lon -= lon_sq * 2
    lat -= lat_sq * 1

    # Subsquares
    lon_sub_sq = int(floor(lon / (5.0 / 60)))
    lat_sub_sq = int(floor(lat / (2.5 / 60)))

    # Chain into result
    qth_locator = f"{chr(lon_field + ASCII_A)}"
    qth_locator += chr(lat_field + ASCII_A)

    qth_locator += chr(lon_sq + ASCII_0)
    qth_locator += chr(lat_sq + ASCII_0)

    qth_locator += chr(lon_sub_sq + ASCII_a)
    qth_locator += chr(lat_sub_sq + ASCII_a)

    return qth_locator
