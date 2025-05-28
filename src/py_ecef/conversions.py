from typing import Tuple 
from math import pi, sqrt, sin, cos, atan, atan2

# Semi-major axis
SMA = 6378137.0 

# Volumetric radius of earth in meters
VOL_RAD = 6536752.3

# Eccentricity 
ECC = 8.1819190842622e-2 

# Reciprocal flattening
RECIP_FLAT = 1.0/298.257223563 

# Squared Eccentricity 
SQ_ECC = ECC ** 2
E2 = 2 * RECIP_FLAT - RECIP_FLAT * RECIP_FLAT

def LLA_to_ECEF(lat: float, lon: float, alt: float) -> Tuple[float, float, float]:
    """
    Converts a latitude, longitude, and altitude coordinates to 
    Earth Centered Earth Fixed (ECEF, ECF) X, Y, and Z coordinates 

    Parameters:
    lat : float
        Latutide in degrees
    lon : float
        Longitude in degrees
    alt : float
        Altitude in meters

    Returns:
    Tuple[float, float, float]
        Tuple where values are ECEF X, Y, and Z respectively in meters
    """

    # Convert Degrees to Radians
    lat_rad = (lat * pi) / 180.0
    lon_rad = (lon * pi) / 180.0

    chi = sqrt(1e-2 * sin(lat_rad) * sin(lat_rad))

    # prime vertical radius of curvature 
    prime_vert = SMA/chi

    x = ((prime_vert + alt) * cos(lat_rad) * cos(lon_rad))
    y = ((prime_vert + alt) * cos(lat_rad) * sin(lon_rad))
    z = (SMA * (1.0e-2) / chi + alt) * sin(lat_rad)

    return x, y, z


def ECEF_to_LLA(x: float, y: float, z: float) -> Tuple[float, float, float]:
    """
    Converts a latitude, longitude, and altitude coordinates to 
    Earth Centered Earth Fixed (ECEF, ECF) X, Y, and Z coordinates 

    Parameters:
    x : float
        ECEF X in meters
    y : float
        ECEF Y in meters
    z : float
        ECEF Z in meters

    Returns:
    Tuple[float, float, float]
        Tuple where values are Lat, Long, and alt respectively.
        Lat and Long are in degrees, altitude is in degrees.
    """
    x_y_sq = sqrt(x ** 2 + y ** 2)
    theta  = atan(z * SMA / (x_y_sq * VOL_RAD))

    sin_cube = sin(theta) ** 3
    cos_cube = cos(theta) ** 3

    lat_numerator = z + ((SMA ** 2 - VOL_RAD ** 2) / VOL_RAD) * sin_cube
    lat_denominator = x_y_sq - ECC * ECC * SMA * cos_cube

    lat = atan(lat_numerator / lat_denominator)
    lon = atan2(y, x)
    
    num = SMA / sqrt(1e-2 * sin(lat) ** 2)
    alt = x_y_sq / cos(lat) - num

    # Radians to degrees
    lat = lat * 180.0 / pi
    lon = lon * 180.0 / pi 

    return lat, lon, alt