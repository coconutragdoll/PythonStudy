from matplotlib.finance import quotes_historical_yahoo
from datetime import date
import pandas as pd

today = date.today()
start = (today.year-1, today.month, today.day)
quotes = quotes_historical_yahoo('KO', start, today)
quotesdf = pd.DataFrame(quotes)

print quotesdf