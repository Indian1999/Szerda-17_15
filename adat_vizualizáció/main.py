import pandas as pd # pip install pandas
import matplotlib.pyplot as plt
import os

DIR_PATH = os.path.abspath(__file__) 
# Megadja annak a file-nak az útvonalát, amit futtatunk (main.py)
DIR_PATH = os.path.dirname(DIR_PATH)
DIAGRAMMOK_PATH = os.path.join(DIR_PATH, "diagrammok")

data = pd.read_csv(os.path.join(DIR_PATH, "tips.csv"))

print(data.head())
print(data.dtypes)
print(data.describe())

def days_bar_chart(file_path = None, show_fig = True):
    plt.bar(data["day"], data["tip"])
    plt.title("Tip amount on days")
    plt.xlabel("Day")
    plt.ylabel("Tip")
    if file_path: # Ha a file_path nem None
        plt.savefig(file_path) # NEM törli a plot tartalmát
    if show_fig:
        plt.show() # Megjelenít, törli is azt ami plot-on van
    if file_path:
        plt.close()

# Histogram az egy specifikus barplot (oszlopgriamm), tartományok vizualizációjára használjuk
def total_bill_histogram(file_path = None, show_fig = True):
    plt.hist(data["total_bill"])
    plt.title("Total bill amount frequency")
    plt.xlabel("Total amount")
    plt.ylabel("Frequency")
    if file_path: # Ha a file_path nem None
        plt.savefig(file_path) # NEM törli a plot tartalmát
    if show_fig:
        plt.show() # Megjelenít, törli is azt ami plot-on van
    if file_path:
        plt.close()
    
        
days_bar_chart(os.path.join(DIAGRAMMOK_PATH, "days_vs_tips_bar.png"), False)
total_bill_histogram(os.path.join(DIAGRAMMOK_PATH, "total_hist.png"), False)
