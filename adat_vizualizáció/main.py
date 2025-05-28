import pandas as pd # pip install pandas
import matplotlib.pyplot as plt
import seaborn as sns # pip install seaborn
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
        
def total_bill_tip_scatter(file_path = None, show_fig = True):
    sns.scatterplot(data = data, x = "total_bill", y = "tip", hue = "day") # hue - szín
    plt.title("Total amount vs Tip amount") 
    if file_path: 
        plt.savefig(file_path)
    if show_fig:
        plt.show()
    if file_path:
        plt.close()
        
def day_tip_line(file_path = None, show_fig = True):
    sns.lineplot(data = data, x = "day", y = "tip")
    plt.title("Average tip on different days")
    if file_path: 
        plt.savefig(file_path)
    if show_fig:
        plt.show()
    if file_path:
        plt.close()
        
def data_line_plot(file_path = None, show_fig = True):
    sns.lineplot(data=data.drop(columns=["total_bill"]))
    plt.title("Tip and Size")
    if file_path: 
        plt.savefig(file_path)
    if show_fig:
        plt.show()
    if file_path:
        plt.close()
        
def total_bill_histogram(file_path = None, show_fig = True):
    # kde - vonalat illeszt a diagrammra
    # hue - szín, mi határozza meg az oszlop színét
    sns.histplot(data = data, x = "total_bill", kde=True, hue="sex")
    plt.title("Total amount frequency per sex")
    plt.xlabel("Total amount")
    if file_path: 
        plt.savefig(file_path)
    if show_fig:
        plt.show()
    if file_path:
        plt.close()
    
def determine_tip_percentage():
    data["tip_perc"] = data["tip"] / data["total_bill"] * 100
    
determine_tip_percentage()
print(data.head())

def tip_perc_vs_day(file_path = None, show_fig = True):
    sns.lineplot(data = data, x = "day", y = "tip_perc")
    plt.title("Tip percentage on days")
    if file_path: 
        plt.savefig(file_path)
    if show_fig:
        plt.show()
    if file_path:
        plt.close()

def tip_perc_vs_day(file_path = None, show_fig = True):
    sns.lineplot(data = data, x = "day", y = "tip_perc")
    plt.title("Tip percentage on days")
    if file_path: 
        plt.savefig(file_path)
    if show_fig:
        plt.show()
    if file_path:
        plt.close()
        
def smokers_tip_perc(file_path = None, show_fig = True):
    sns.barplot(data = data, x = "smoker", y = "tip_perc", hue = "sex")
    plt.title("Smoker tip percentage per sex")
    if file_path: 
        plt.savefig(file_path)
    if show_fig:
        plt.show()
    if file_path:
        plt.close()
   
def day_time_sex(file_path = None, show_fig = True):
    data["day_time"] = data["day"].values + " " + data["time"].values
    sns.countplot(data = data, x = "day_time", hue="sex")
    plt.title("Day-Time frequency per sex")
    plt.xlabel("Day-Time")
    if file_path: 
        plt.savefig(file_path)
    if show_fig:
        plt.show()
    if file_path:
        plt.close()
   
day_time_sex(os.path.join(DIAGRAMMOK_PATH, "day_time_freq_per_sex.png"), False) 
#smokers_tip_perc(os.path.join(DIAGRAMMOK_PATH, "smoker_tips.png"), False)
#tip_perc_vs_day(os.path.join(DIAGRAMMOK_PATH, "tip_perc_on_days.png"), False)
#total_bill_histogram(os.path.join(DIAGRAMMOK_PATH, "total_amount_hist.png"), False)
#days_bar_chart(os.path.join(DIAGRAMMOK_PATH, "days_vs_tips_bar.png"), False)
#total_bill_histogram(os.path.join(DIAGRAMMOK_PATH, "total_hist.png"), False)
#total_bill_tip_scatter(os.path.join(DIAGRAMMOK_PATH, "total_bill_tip_scatter_colored.png"), False)
#day_tip_line(os.path.join(DIAGRAMMOK_PATH, "day_tip_line.png"), False)
#data_line_plot(os.path.join(DIAGRAMMOK_PATH, "tip_size_line.png"), False)


