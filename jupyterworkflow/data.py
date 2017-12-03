import os
from urllib.request import urlretrieve

import pandas as pd

URL = "https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"

def get_fremont_data (filename = 'Fremont.csv', url = URL, force_download = False):
    '''Download and cache the fremont data
    Parameters
    __________
    filename : string (optional)
        location to save the data
    url: string (optional)
        webloc of data
    force_download: bool (optional)
        if True, force the download

    Returns
    ---------
    data: pandas.DataFrame
        Fremont data in dataframe
    '''
    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)

    data = pd.read_csv("Fremont.csv", index_col = 'Date')
    try:
        data.index = pd.to_datetime(data.index, format = "%m/%d/%Y %H:%M:%S %p")
    except TypeError:
        data.index = pd.to_datetime(data.index)

    data.columns = ['West', 'East']
    data['Total'] = data['West'] + data['East']
    return data