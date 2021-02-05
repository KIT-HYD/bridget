class BURGESS_FACTORS:
    """
    Do not instantiate this class.
    The class will return the factors for wound corrections for different
    probe configurations and wound sizes.
    The numbers are taken from Table 1 (p.595) in Burgess et al. (2001)
    
    References
    ----------
    Burgess, Stephen SO, et al. "An improved heat pulse method to measure low 
        and reverse rates of sap flow in woody plants." Tree physiology 21.9 
        (2001): 589-598.

    """
    size_06 = {
        17: [1.6565, -0.0014, 0.0002],
        18: [1.7077, -0.0014, 0.0002],
        19: [1.7701, -0.0017, 0.0002],
        20: [1.8292, -0.0019, 0.0003],
        21: [1.8909, -0.0022, 0.0003],
        22: [1.9554, -0.0025, 0.0004],
        23: [2.0026, -0.0029, 0.0004],
        24: [2.0685, -0.0031, 0.0005],
        26: [2.1932, -0.0038, 0.0006],
        28: [2.3448, -0.0047, 0.0008],
        30: [2.4908, -0.0057, 0.0010],
    }
    size_05 = {
        17: [1.6821, -0.0015, 0.0002],
        18: [1.7304, -0.0013, 0.0002],
        19: [1.7961, -0.0016, 0.0002],
        20: [1.8558, -0.0018, 0.0003],
        21: [1.9181, -0.0021, 0.0003],
        22: [1.9831, -0.0024, 0.0004],
        23: [2.0509, -0.0028, 0.0004],
        24: [2.0972, -0.0030, 0.0005],
        26: [2.2231, -0.0037, 0.0006],
        28: [2.3760, -0.0046, 0.0008],
        30: [2.5232, -0.0055, 0.0010],
    }
    
    @classmethod
    def __idx(cls, keys, wound):
        idx = int(wound * 100)
        i = 0
        while idx not in keys:
            i += 1
            if i > 500 or idx <= 17:
                raise ValueError("Can't find Burgess Factor for wound size of %.2f." % wound)
            idx -= 1
        return idx
    
    @classmethod
    def get(cls, probe, wound):
        if probe == '0.6':
            idx = cls.__idx(cls.size_06.keys(), wound)
            return cls.size_06[idx]
        elif probe == '0.5':
            idx = cls.__idx(cls.size_05.keys(), wound)
            return cls.size_05[idx]
        else:
            raise ValueError("%s is not a known probe config. Allowed values: ['0.5', '0.6']" % probe)


def misalignment_correction():
    pass


def wounding_correction(method='burgess', **kwargs):
    if method.lower() == 'burgess':
        return _wounding_correction_burgess(**kwargs)
    else:
        raise NotImplementedError


def _wounding_correction_burgess(probe_size, wound_size, **kwargs):
    # get the factors
    b, c, d = BURGESS_FACTORS.get(probe_size, wound_size)
    
    # go crazy
    pass


def t_stand():
    pass
