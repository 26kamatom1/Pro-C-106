import pandas as pd
import csv
import plotly.express as px

df = pd.read_csv("Data1.csv")
fig = px.scatter(df,x="Coffee in ml", y="sleep in hours")
fig.show()
with open("data1.csv",newline="")as f:
    reader=csv.reader(f)
    data=list(reader)
data.pop(0)
import numpy as np
coffee=[]
sleep=[]
for n in data:
    coffee.append(float(n[1]))
    sleep.append(float(n[2]))
correlation = np.corrcoef(coffee,sleep)
print(correlation[0,1])
# the correlation coefficient value is -1 which means that the data is inversly correlated