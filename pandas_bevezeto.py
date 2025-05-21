import pandas as pd # terminálba: pip install pandas

data = pd.read_csv("NFLX.csv")
print(data)
print(type(data)) # <class 'pandas.core.frame.DataFrame'>

all_time_high = data["High"].max()
all_time_low = data["Low"].min()
close_average = data["Close"].mean()
open_median = data["Open"].median()
close_std = data["Close"].std() # Standard deviation (szórás)

print(f"A Netflix részvények valaha volt legmagasabb értéke: {round(all_time_high, 2)} $.")
print(f"A Netflix részvények valaha volt legalacsonyabb értéke: {round(all_time_low, 2)} $.")
print(f"A Netflix részvények átlagos záráskori értéke: {round(close_average, 2)} $.")
print(f"A Netflix részvények medián nyitási értéke: {round(open_median, 2)} $.")
print(f"A Netflix részvények záráskori szórás értéke: {round(close_std, 2)} $.")

# Melyik napon volt a valaha volt legmagasabb értéken?
max_row = data[data["High"] == all_time_high]
print(max_row)
print(type(max_row)) # <class 'pandas.core.frame.DataFrame'>
max_date = max_row.iloc[0, 0]
print(f"A nap amikor a legmagasabb volt a részvények értéke: {max_date}.")

