import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import REST, TimeFrame
import constants as consts
import timeframe

# Instantiate REST API Connection
api = tradeapi.REST(key_id=consts.ALPACA_API_KEY, secret_key=consts.ALPACA_SECRET_KEY, base_url=consts.BASE_URL, api_version='v2')
# Fetch Account
account = api.get_account()
# Print Account Details
print(account.id, account.equity, account.status)

bars = api.get_bars("AAPL", TimeFrame.Minute, "2021-06-08", "2021-06-08", adjustment='raw')
print(bars.df.head())