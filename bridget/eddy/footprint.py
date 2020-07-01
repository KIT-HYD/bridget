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

def footprint(t_air, a, p, u, cov_uw, cov_vw, cov_wt, var_v, z = 2.0, method = "Kormann_Meixner"):
    """
    Top-level footprint function.

    If more than one footprint method is implemented, these should go
    into functions in this module. This function then has a **string**
    parameter to switch the method.

    Parameters
    ----------
    z : float
        measurement height [m]
    u : list
        horizontal wind component for the direction in which the sonic is oriented [m/s].
    cov_uw : list
        Covariance between the wind components u and w [m2/s2].
    cov_vw : list
        Covariance between the wind components v and w [m2/s2].
    cov_wt : list
        Covariance between the wind components w and temperature [(m*°C)/s].
    var_v : list
        variance of v (horizontal wind component for the direction rectangular to the orientation of the sonic) [m/s].
    t_air : list
        air temperature [°C].
    a : list
        absolute humidity [g/m3].
    p : list
        air pressure [hPa].
    """

    raise NotImplementedError
