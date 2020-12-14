"""
Sap Flow package
----------------

These functions can be used to process sap flow measurements to 
evapotranspiration estimations. Each of the function will return the output 
along with estimated/calculated uncertainties. To suppress the output, 
set the with_uncertainties parameter to False.

"""

def heat_pulse_velocity(temperatures, m_c, rho_b, probe_spacing, with_uncertainties=True):
    """Calculate heat pulse velocity

    [Description]

    Parameters
    ----------
    temperatures : list, numpy.array
        Array of coupled temperatures
    m_c : list, numpy.array
        Water content of the wood
    rho_b : list, numpy.array
        Sapwood density
    probe_spacing : int
        Spacing of the probes, that measured the temperatures
    with_uncertainties : bool
        If True (default), all estimated uncertainties will be returned 
        along with the data

    Returns
    -------
    vh : numpy.array
        Array of heat pulse velocity. 
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
    """Calculate sap velocity

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


def flux_density(vs, bark_depth: float, dbh: float, As: float, with_uncertainties=True):
    r"""Calculate sap velocity

    [Description]

    Parameters
    ----------
    vs : numpy.array
        Array of sap flow velocity across As
    bark_depth : float
        Bark depth in [cm]
    dbh : float
        Breast height diameter in [cm]
    As : float
        Stem area at dbh in [cm²]
    with_uncertainties : bool
        If True (default), all estimated uncertainties will be returned 
        along with the data

    Returns
    -------
    Q : numpy.array
        sap flow flux density

    """
    raise NotImplementedError
