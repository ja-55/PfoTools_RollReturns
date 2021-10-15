import pandas as pd
from yahoo_fin.stock_info import *
import datetime as dt

tckr = 'SKLZ'
first_date = dt.date(2021,1,1)
last_date = dt.date(2021,10,14)
thresh = 0.22
wdw = 40

srs = get_data(tckr, start_date = first_date, end_date = last_date)
prc = srs['adjclose']
prc = pd.DataFrame(prc)
prc.columns = [tckr]

prc['shift'] = prc[tckr].shift(wdw)
prc['shift_rtn'] = (prc[tckr] - prc['shift']) / prc['shift']
prc['shift_rtn_abs'] = prc['shift_rtn'].map(abs)

prc['shift_rtn_bad'] = prc['shift_rtn_abs'] <= thresh
prc['shift_rtn_good'] = prc['shift_rtn_abs'] > thresh


prc = prc.dropna()
#prc['shift_rtn'].hist();
#prc['shift_rtn_abs'].hist();

op = prc.loc[:,['shift_rtn_bad','shift_rtn_good']].sum() / len(prc.index)
