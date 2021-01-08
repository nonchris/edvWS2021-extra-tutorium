import numpy as np


# Task: convert cartesian coordinates in polar coordinates
# to_polar - expected version
# calculate from cartesian coordinates x and y
# polar coordinates r and theta
# FIXME only works in the first quadrant
def to_polar_expected(x, y):
    if np.isclose(x, 0):  # x == 0 is forbidden vor arctan(y/x)
        theta = np.pi / 2.
    else:
        theta = np.arctan(y / x)

    r = np.sqrt(x ** 2 + y ** 2)  # calculate radius

    # return radius and theta
    return r, theta


r, theta = to_polar_expected(1, 1)
print(r, theta * 180. / np.pi)  # Umrechnung in Grad!

r, theta = to_polar_expected(0, 1)
print(r, theta * 180. / np.pi)  # Umrechnung in Grad

r, theta = to_polar_expected(1, 0)
print(r, theta * 180. / np.pi)  # Umrechnung in Grad!


def to_polar_extended(x, y):
    """
    Fixed polar coordinate calculation for all quadrants.

    returns: (r, theta)

    theta: (-pi, pi]
    """
    r = np.sqrt(x ** 2 + y ** 2)

    if np.isclose(x, 0):
        if y >= 0:
            theta = np.pi / 2
        else:
            theta = -np.pi / 2

    elif x > 0:
        theta = np.arctan(y / x)

    else:
        if y >= 0:
            theta = np.arctan(y / x) + np.pi
        else:
            theta = np.arctan(y / x) - np.pi

    return r, theta


def to_polar_numpy(x, y):
    """
    Polar coordinate calculation using numpy.argtan2.

    returns: (r, theta)

    theta: (-pi, pi]
    """
    r = np.sqrt(x ** 2 + y ** 2)
    theta = np.arctan2(x, y)

    return r, theta


def to_polar_complex(x, y, deg=False):
    """
    Polar coordinate calculation using complex number conversion.

    deg: bool,optional
        Return angle in degrees if True, radians if False (default).

    returns: (r, theta)

    theta: (-pi, pi]
    """
    z = x + 1j * y
    r = np.abs(z)             # calculate absolute as radius
    theta = np.angle(z, deg)  # gets the angle from a complex argument

    return r, theta
