import pybit
from pybit.unified_trading import HTTP
import pandas as pd
import matplotlib.pyplot as plt

session = HTTP(
    testnet=False,
    api_key='VgBHoVP8jygqSdmVNp',
    api_secret='Yg0itDuYjMGOWQTzgBgLRDTwI0zyOjqG8Gro'
)

session.get_orderbook(category="linear", symbol="BTCUSDT")

# Create five long USDC Options orders.
# (Currently, only USDC Options support sending orders in bulk.)
payload = {"category": "option"}
orders = [{
  "symbol": "BTC-30JUN23-20000-C",
  "side": "Buy",
  "orderType": "Limit",
  "qty": "0.1",
  "price": i,
} for i in [15000, 15500, 16000, 16500, 16600]]

payload["request"] = orders
# Submit the orders in bulk.
session.place_batch_order(payload)

df = pd.DataFrame(payload, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'turnover'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')  # перетворюємо timestamp у дату та час
df[['open', 'high', 'low', 'close', 'volume', 'turnover']] = df[['open', 'high', 'low', 'close', 'volume', 'turnover']].astype(float)  # перетворюємо числові значення у тип float

plt.plot(df['timestamp'], df['close'])
plt.xlabel('Дата')
plt.ylabel('Ціна закриття')
plt.title('Графік цінової динаміки криптовалюти на площадці Bybit')
plt.show()
