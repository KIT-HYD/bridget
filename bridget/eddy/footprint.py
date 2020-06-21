"""
The `footprint` submodule implements common methods to calculate the
footprint of the measurement from Eddy Covariance data.

Beside several methods that can calculate the timevariat footprint,
an aggregation method for defining a common footprint region is
given.

Examples
--------

.. note::

    More to come soon

"""

def footprint(height = 2, t_air, a, p, wndspeed, cov_uw, cov_vw, var_v, method = "Kormann_Meixner"):
    """
    Top-level footprint function.

    If more than one footprint method is implemented, these should go
    into functions in this module. This function then has a **string**
    parameter to switch the method.

    Parameters:
        - height = measurement height (z) [m]
        - wndspeed = horizontal wind component for the direction in which the sonic is oriented (u) [m/s]
        - cov_uw = Covariance between the wind components u and w
        - cov_vw = Covariance between the wind components v and w
        - var_v = variance of v (horizontal wind component for the direction rectangular to the orientation of the sonic
        - t_air = air temperature [°C]
        - a = absolute humidity [g/m3]
        - p = air pressure [hPa]
    """
    pass
