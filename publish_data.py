import pandas as pd
import datetime
from datetime import datetime as dt
from data.yfinance_data import get_series_data_high, get_timed_tickers
from data_publishers import gsheet_publisher as gsp


if __name__ == '__main__':

    time_now = dt.today()
    prev_day_time = time_now - datetime.timedelta(days=1)
    ps = get_timed_tickers(prev_day_time, time_now, ['msft'], interval='15m')
    x = get_series_data_high(ps)
    x  = pd.DataFrame(x[0])

    client = gsp.authorize_client(service_account_file='service_file.json')
    gsp.update_main_sheet(client, 'nw', time_now.strftime('%Y%m%d'), x)


