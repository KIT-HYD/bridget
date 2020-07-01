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

    import numpy as np

    #1) calculate u_star [m/s]
    u_star = (cov_uw**2 + cov_vw**2)**(1/4)

    #2) calculate saturation vapor pressure e_w [hPa]
    #WMO (https://library.wmo.int/doc_num.php?explnum_id=3151): first part of the euqation is the pressure function, but no big influence (around 1)
    #e_w' = f(p) * e_w
    e_w = (1.0016 + 3.15 * 10**(-6) * p - 0.074 * p**(-1)) * (6.112 * np.exp((17.62 * t_air) / (243.12 + t_air)))

    #3) calculate relative humidity with e_w
    #input a: [g/m3] -> need a in [kg/m3] here
    #input t_air: [°C] -> need t_air in [K] here
    #e_w: [hPa] -> need e_w in [Pa] here
    R_v = 461.5     #specific gas constant for water vapor [J/(kg*K)]
    rh = 100 * (a * 10**(-3)) * R_v * (t_air + 273.15) * (e_w * 100)**(-1)

    #4) calculate actual vapor pressure e_a [hPa]
    e_a = rh * e_w / 100

    #5) calculate rho (density of air)
    #first calculate the pressure of dry air (p_d)
    p_d = p - e_a   #[hPa]
    R_d = 287.1     #specific gas constant for dry air [J/(kg*K)]

    #calculate rho, pressure in [Pa] and t_air in [K]
    rho = (p_d * 100) / (R_d * (t_air + 273.15)) + (e_a * 100) / (R_v * (t_air + 273.15))

    #different formula for rho, results are nearly equal/very similar, first formula is more intuitive (from perfect gas law)
    rho_1 = 1.201 * ((290 * ((p * 100) - 0.378 * (e_a * 100))) / (1000 * (t_air + 273.15))) / 100

    #6) calculate specific heat capacity of air (c_p)
    c_p = 0.24 * 4185.5 * (1 + 0.8 * 0.622 * (e_a * 100) / (p * 100 - e_a * 100))

    #7) calculate sensible heat flux (hts) [W/m2]
    #easiest formula for hts, but there are others
    hts = rho * c_p * cov_wt

    #results for hts are pretty much in compliance with the results in the TK2-file
    #but many numbers are -9999 in the TK2-file -> when is hts not defined??


    #x) specific humidity and virtual temperature
    q = 0.622 * (e_a/(p - 0.378 * e_a))     #[kg/kg]    Foken, 2017, p. 49
    t_virt = (1 + 0.61 * q) * t_air         #[°C]       Foken, 2017, p. 37

    #http://www.shodor.org/os411/courses/_master/tools/calculators/virtualtemp/tv1calc.html



    #7) calculate Obukhov length (zl) [m]
    k = 0.4    # von Karman constant
    g = 9.81    # gravity

    #using the actual air temperature
    L = - (rho * c_p * u_star**3 * (t_virt + 273.15)) / (k * g * hts)    #[m]   Foken 2017, p. 55

    #using the virtual temperature


    zol = z/L

    #z/L is differing from the values in the TK2-file --> look at the calculation aggregation

    #####
    ### calculations above could be "outsourced" into stand-alone functions, which are called in the footrpint function
    ### as these are pretty basic meteorological functions which could may be used in other bridget functions
    #####

    ### core-footprint-calculation starts here

    #f.1) calculate phi_c and phi_m (stability functions) [-], Kormann_Meixner gives no calculation if L == 0
    for i in L:
        if (i > 0):
            phi_c = 1 + 5 * zol
            phi_m = 1 + 5 * zol
        elif (i < 0):
            phi_c = (1 - 16 * zol)**(-1/2)
            phi_m = (1 - 16 * zol)**(-1/4)

    #f.2) calculate m (exponent of the wind velocity power law) and n (exponent of the eddy diffusivity power law) [-]
    k = 0.4    # von Karman constant

    m = (u_star * phi_m) / (k * u)

    for i in L:
        if (i > 0):
            n = 1 / (1 + 5 * zol)
        elif (i < 0):
            n = (1 - 24 * zol) / (1- 16 * zol)

    #f.3) calculate r (shape factor) [-]
    r = 2 + m - n

    #f.4) calculate eddy diffusivity K [m2/s]
    K = (k * u_star * z) / (phi_c * zol)

    #f.5) calculate U (constant in power law profile of the wind velocity) [m^(1-m)/s] and kappa (constant in power law profile of the eddy diffusivity) [m^(2-n/m)] (dimensions not realy working here)
    U = u / z**m
    kappa = K / z**n

    #f.6) calculate xi (flux length scale) [m]
    xi = (U * z**r) / (r**2 * kappa)


    #f.7) calculate the flux footprint [1/m2]
    mu = (1 + m) / r





    pass
