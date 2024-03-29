# 원리만

from forex_python.converter import CurrencyRates

rate = CurrencyRates()
krw_rate = rate.get_rate("USD","KRW")
print(krw_rate)
