"""
Sap Flow package
----------------

These functions can be used to process sap flow measurements from different sensors 
and measurement methods in order to to calculate transpiration estimates for 
individual trees and scale up to stands. Method-specific differences exist in 
the calculations from the temperature measurements up to sap velocity or sap 
flux density, whereas subsequent calculations can be applied to all methods. 

"""

def heat_pulse_velocity(temperatures, m_c, rho_b, probe_spacing):
    """Calculate heat pulse velocity from temperature measurements of sensors
    using the heat pulse / heat ratio method.  

    [Description]

    Parameters
    ----------
    temperatures : list, numpy.array
        Array of two coupled temperatures per measurement depth
    m_c : list, numpy.array
        Water content of the wood
    rho_b : list, numpy.array
        Sapwood density
    probe_spacing : int
        Spacing between the temperature probes and the heating 
    

    Returns
    -------
    vh : numpy.array
        Array of heat pulse velocity per measurement depth.  
    t_rise : numpy.array
        timing offset in maximum temperature rise. 
        Will only be returned if ``with_uncertainties=True``.
    var_mc : numpy.array
        variance in m_v
        Will only be returned if ``with_uncertainties=True``.
    var_rho : numpy.array
        variance in rho_b
        Will only be returned if ``with_uncertainties=True``.
    t_diffusivity : numpy.array
        temperature diffusivity
        Will only be returned if ``with_uncertainties=True``.
    
    """
    raise NotImplementedError

def sap_velocity(m_c, rho_b, with_uncertainties=True):
    """Calculate sap velocity from heat pulse velocity.  

    [Description]

    Parameters
    ----------
    m_c : list, numpy.array
        Water content of the wood
    rho_b : list, numpy.array
        Sapwood density
    with_uncertainties : bool
        If True (default), all estimated uncertainties will be returned 
        along with the data

    Returns
    -------
    vs : numpy.array
        Array of sap flow velocity. 
    var_mc : numpy.array
        variance in m_v
        Will only be returned if ``with_uncertainties=True``.
    var_rho : numpy.array
        variance in rho_b
        Will only be returned if ``with_uncertainties=True``.

    """
    raise NotImplementedError






def sap_velocity(method='East30_3needle', **kwargs):
    if method.lower() == 'East30_3needle':
        return _sap_velocity_East30_3needle(**kwargs)
    else:
        raise NotImplementedError

    # warum hat die so nen komischen _ davor, die Funktion?
def _sap_velocity_East30_3needle(vs, probe_spacing, wound_diameter, **kwargs):
    """Calculate sap velocity for East30 3-needle sap flow sensors for two corresponding
    temperature measurements below and above the middle heater needle. 
    Sap velocity (equation (6) page 33 East30 3-needle sap flow sensor manual), last term omitted, in [m/s]

    [Description]

    Parameters
    ----------
    k_sapwood: float
        thermal conductivity of sapwood in [W m-1 K-1], 0.5 is a literature value
    Cw: float
        specific heat of water in [J m-3 K-1], 4.1796 J/(cm³ K) at 25°C is a literature value
    ru, rd: float
        distance from heater to sensor, upstream (ru) and downstream (rd), in [m]
        (upstream corresponds to the needle below the heater, downstream in above the heater, in an assumed upward water movement)
    dTu: list, numpy.array
        time series of temperature differences in [K] at the upstream thermistor (below the heater in an upward water movement), differences are between initial 
        temperature and 60 seconds after heating. 
    dTd: list, numpy.array
        time series of temperature differences in [K] at the downstream thermistor (above the heater in an upward water movement), differences are between initial 
        temperature and 60 seconds after heating.
       

    Returns
    -------
    vs : numpy.array
        Array of sap velocity, here converted to [cm h-1]. 
    var_mc : numpy.array
        variance in m_v
        Will only be returned if ``with_uncertainties=True``.
    """

    kw_sapwood = 0.5               
    Cw <- 4.1796 *1000000         
    ru =  0.006            
    rd =  0.006
    
    # calculation of sap velocity and conversion to [cm/h]
    vs = 2 * kw_sapwood /(Cw*(ru + rd)) * log(dTu/dTd) *100*3600

    return(vs)
    


def sapwood_area():
    """Calculate sapwood area after a Gebauer et al. 2008.  ?

    [Description]

    Parameters
    ----------
    dbh: float

    Returns
    -------
    As : float
        Sapwood area (at breast height) in [cm²]


    """
    raise NotImplementedError







def sap_flow(vs, bark_depth: float, dbh: float, As: float):
    """Calculate sap flow from sap velocity and sapwood area. 

    [Description]

    Parameters
    ----------
    vs : numpy.array
        Array of (corrected) sap velocity/sap flux density
    bark_depth : float
        Bark depth in [cm]
    dbh : float
        Diameter at breast height in [cm]
    num_vel: float
        number of sap velocity measurements at different depths
    As : float
        Sapwood area (at breast height) in [cm²]


    Returns
    -------
    Q : numpy.array
        sap flow per tree in [litres/h]

    """
    raise NotImplementedError
