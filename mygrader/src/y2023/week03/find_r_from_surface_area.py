import math


def find_r_from_surface_area(surface_area):
    """
    Calculates and returns the radius of a sphere given its surface area.
    """
    radius = (surface_area / (4 * math.pi)) ** 0.5
    return radius


def sphere_volume(radius):
    """
    Calculates and returns the volume of a sphere given its radius.
    """
    volume = (4 / 3) * math.pi * radius ** 3
    return volume

