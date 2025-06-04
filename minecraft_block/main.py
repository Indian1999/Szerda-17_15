import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns # pip install seaborn
import plotly.express as px
import os

dir_path = os.path.dirname(__file__)
with open(os.path.join(dir_path, "item_block_data.json"), "r", encoding="utf-8") as f:
    data = json.load(f)
    
print(type(data)) # <class dict>

df = pd.DataFrame.from_dict(data, orient="index")
print(df.head())

def categorize_item(item):
    if item["is_block"] == True:
        return "Block"
    elif "tool" in item["name"] or "sword" in item["name"] or "pickaxe" in item["name"] or "shovel" in item["name"]:
        return "Tool"
    elif "armor" in item["name"] or item["name"].endswith(("helmet", "chestplate", "leggings", "boots")):
        return "Armor"
    elif "c:foods" in item["item_tags"]:
        return "Food"
    else:
        return "Other"

# "acacia_boat".split("_") -> ["acacia", "boat"]
# "rail".split("_") -> ["rail"]   (Misc)
df["category"] = df.apply(categorize_item, axis = 1)
df["subcategory"] = df["name"].apply(
    lambda x: x.split("_")[0] if "_" in x else "misc"
)

category_counts = df.groupby(["category", "subcategory"]).size().reset_index(name="count")
print(category_counts)