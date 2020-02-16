import pandas as pd
import json

excel_data = pd.read_excel("statisztika.xlsx")
json_data = excel_data.to_json(r'statisztika.json')