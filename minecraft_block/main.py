import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns # pip install seaborn
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

df["category"] = df.apply(categorize_item, axis = 1)
print(df.head())