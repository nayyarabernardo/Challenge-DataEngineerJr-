import pandas as pd
import json

df = pd.read_json("data.json")
df.to_excel("Desafio beAnalytic.xlsx")
