# %% [markdown]
# # Canadian trade data
# 
# This notebook downloads raw trade data from [ISED Canada](https://ised-isde.canada.ca/site/trade-data-online/en)
# 
# Includes trade balance data by province/trade-partner and [HS2](https://en.wikipedia.org/wiki/Harmonized_System) product categorization.
# 
# 

# %%
# TODO
# download SUT tables: https://www150.statcan.gc.ca/n1/en/catalogue/15-602-X

# %%
import requests
import os
from datetime import datetime as dt

# %%
raw_dir = os.path.abspath('../raw/')

# %%
start, end = 1990, 2024

# years
years = [str(x) for x in range(start, end+1)]

# product codes
codes = ['C'+chr(n) for n in range(ord('A'), ord('U')+1)] # chapter codes
# codes = [str(x).zfill(2) for x in range(1, 100)] # HS2 codes

na_areas =  {
    '9999' : 'CA',
    'P10' : 'NL',
    'P11' : 'PE',
    'P12' : 'NS',
    'P13' : 'NB',
    'P24' : 'QC',
    'P35' : 'ON',
    'P46' : 'MB',
    'P47' : 'SK',
    'P48' : 'AB',
    'P59' : 'BC',
    'P61' : 'NT',
    'P60' : 'YT',
    'P62' : 'NU',
    }

url = 'https://ised-isde.canada.ca/app/ixb/tdo/report.csv'

# request parameters
params = {
    'cssIncludes': '%2Fcss%2Fadd_WET_4-0_Canada_Apps.css',
    'jsIncludes': 'js%2FsurveyPopup.js',
    'grouped': 'GROUPED',
    'searchType': 'All',
    'countryList': 'DET',
    'areaCodes': '',
    'toFromCountry': 'CDN',
    'reportType': 'TB',
    'periodString': '',
    'timePeriod': '%7CCustom+Years',
    'currency': 'CDN',
    'lang': '',
    'productType': 'HS6',
}

# %%
# iterate request parameters
n = 0
N = len(na_areas) * len(years) * len(codes)
t0 = dt.now()

for na_code in na_areas:

    for year in years:

        for code in codes:
            
            n += 1
            print(f'[{n:,} of {N:,}]')
            
            # destination file
            area_abbrev = na_areas[na_code]
            dst = os.path.join(raw_dir, f'{area_abbrev}-{year}-{code}.csv')
            if os.path.exists(dst):
                print('Skipped:', dst)
                continue

            # update parameters
            params['naArea'] = na_code
            params['customYears'] = year
            params['hSelectedCodes'] = code

            resp = requests.get(url, params=params)

            if resp:
                with open(dst, 'wb') as f:
                    f.write(resp.content)
            else:
                print(f'Error: {resp}')
                continue

            # update message
            t1 = dt.now()
            delta = t1 - t0
            avg = delta / n
            eta = avg * (N-n)

            print(f'status: {resp.status_code} | saved: {dst}')
            print(f'time: {t1} | delta: {delta} | eta: {eta}')

# %%
print('-- Complete --')


