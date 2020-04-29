import pandas as pd

from ._util import get_header


def read_TK2_file(fname, strict=True, na_values=-9999.9003906):
    """Read TK2 File

    Reads in a TK2 Eddy data file and sets the default columns as column names.
    If strict is True, the resulting DataFrame will be forced to have the
    expected column names. On failure, a ValueError is raised.

    Parameters
    ==========
    fname : str
        Filename of the TK2 data file. Can also be a file-like object, file
        stream or url.
    strict : bool
        If True, the data structure will be checked to include all columns
        expected. On failure a ValueError will be raised.
    na_values : scalar, str, list-like, or dict, optional
        Additional values to recognize as NA/NaN.
    """
    read_kwargs = dict(na_values = na_values)
    return _reader(fname, 'TK2', strict=strict, **read_kwargs)


def read_QA_QC_file(fname, strict=True):
    """Read QA_QC File

    Reads in a QA QC Eddy flag file and sets the default columns as column
    names. If strict is True, the resulting DataFrame will be forced to have
    the expected column names. On failure, a ValueError is raised.

    Parameters
    ==========
    fname : str
        Filename of the QA QC data file. Can also be a file-like object, file
        stream or url.
    strict : bool
        If True, the data structure will be checked to include all columns
        expected. On failure a ValueError will be raised.
    """
    return _reader(fname, 'QA_QC', strict=strict)


def _reader(fname, type_str, strict=True, **read_kwargs):
    # read the file
    data = pd.read_csv(fname, sep=',', header=None, index_col=None, na_values=[read_kwargs['na_values']])
    # drop empty columns
    data.dropna(axis=1, how='all', inplace=True)

    # set the column names
    data.columns = get_header(type_str)

    # strict mode
    if strict:
        assert (get_header(type_str) == data.columns).all()

    # return
    return data
