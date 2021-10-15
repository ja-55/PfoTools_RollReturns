import pandas as pd
from yahoo_fin.stock_info import *
import datetime as dt

tckr = 'SKLZ'
first_date = dt.date(2021,1,1)
last_date = dt.date(2021,10,14)
wdw = 40

srs = get_data(tckr, start_date = first_date, end_date = last_date)
prc = srs['adjclose']
prc = pd.DataFrame(prc)
prc.columns = [tckr]

prc['shift'] = prc[tckr].shift(wdw)
prc['shift_rtn'] = (prc[tckr] - prc['shift']) / prc['shift']

prc = prc.dropna()
prc['shift_rtn'].hist();
