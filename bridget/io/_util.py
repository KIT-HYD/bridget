"""
Util
====

This is for internal use. The `bridget.io._util` defines some static dicts 
which are used to define default file structures.
"""
import os
import pandas as pd

BASEPATH = os.path.abspath(os.path.dirname(__file__))


def get_header(file_type='TK2', full=False):
    """Get the File header

    The Header for either TK2 or QA_AC files is returned. 

    Parameters
    ==========
    file_type : str
        The file type for which a header is required. Has to be in 
        ['TK2', 'QA_QC']
    full : bool, optional
        If False (default), only the Header names are returned as an array. 
        If True, the descriptions and units are returned as 
        :class:`pandas.DataFrame`.
    
    Returns
    =======
    header : numpy.array, pandas.DataFrame
        Either the header names only (array) or the full header table including 
        descriptions and units

    Raises
    ======
    ValueError : in case file_type is not in ['TK2', 'QA_QC']
    """
    # get the correct file
    if file_type == 'TK2':
        path = os.path.join(BASEPATH, 'default_columns_TK2.csv')
    elif file_type == 'QA_QC':
        path = os.path.join(BASEPATH, 'default_columns_QA_QC.csv')
    else:
        raise ValueError("file_type has to be in ['TK2', 'QA_QC']")

    # read
    df = pd.read_csv(path, header=None, index_col=None)
    df.columns = ['colname', 'description', 'unit']

    # return 
    if full:
        return df
    else:
        return df.colname.values
