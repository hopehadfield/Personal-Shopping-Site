from __init__ import Product, BasicSelection
import pandas
import numpy as np
import csv

csv_path = "C:/Users/Katherine Zhang/OneDrive/Documents/Capstone/Product Dataset.csv"
database = []
select = BasicSelection(csv_file=csv_path)

print(select.parse_dataset())

