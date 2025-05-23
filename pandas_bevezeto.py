import pandas as pd # terminálba: pip install pandas
import matplotlib.pyplot as plt # pip install matplotlib.pyplot

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

# Mennyi volt a záráskori részvény állás, azon a napon, amikor a valaha volt legkisebb értéken állt a részvény?

min_row = data[data["Low"] == all_time_low]
print(min_row)
lowest_close = min_row.iloc[0, 4]
print(f"A záráskori érték a 'legrosszabb' napon: {lowest_close} $.")

# Alap tulajdonságok:
print(data.dtypes)
print(data.describe())

# Mennyi volt a záráskori érték 2017-02-10 -én?
data["Date"] = pd.to_datetime(data["Date"])
print(data.dtypes)
filtered_row = data[data["Date"] == "2017-02-10"]
print(filtered_row)
filtered_close = filtered_row.iloc[0, 4]
print(f"Close értéke 2017-02-10-én: {round(filtered_close, 2)} $.")

# Szűrjük ki a 2019 novemberi sorokat
novemeber_2019 = data[data["Date"] >= "2019-11-01"]
novemeber_2019 = novemeber_2019[novemeber_2019["Date"] <= "2019-11-30"]
print(novemeber_2019)

print(novemeber_2019.describe())

# Hány napon volt a zárási érték az átlag 5%-os környezetében

close_mean = data["Close"].mean()
average_days = data[data["Close"] >= close_mean * 0.95]
average_days = average_days[average_days["Close"] <= close_mean * 1.05]

print(average_days)
print(f"{len(average_days)} átlagos napot zárt a tőzsdén a Netflix.")



# Ábrázoljuk grafikonon az összes napra a nyitó értékeket

plt.plot(data["Date"], data["Open"])
plt.title("Stock values over time")
plt.ylabel("Price in $")
plt.xlabel("Date")
plt.xticks(rotation=45)
plt.close()

#
data.set_index("Date", inplace=True)
print(data)
monthly_average = data["Close"].resample("ME").mean()
monthly_average = monthly_average.reset_index()
monthly_average["Date"] = monthly_average["Date"].dt.to_period("M")
print(monthly_average)

print(monthly_average.dtypes)

plt.plot(monthly_average["Date"].astype("string"), monthly_average["Close"])
plt.title("Monthly Stock Values")
plt.ylabel("Price in USD")
plt.xlabel("Month")
plt.xticks(ticks=monthly_average["Date"].astype("string")[::4], rotation = 45)
plt.grid(True)
plt.show()