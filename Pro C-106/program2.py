import pandas as pd
import csv
import plotly.express as px

df = pd.read_csv("Data4.csv")
fig = px.scatter(df, x="Roll No",y="Marks In Percentage")
fig.show()
with open("data4.csv", newline="")as f:
    reader=csv.reader(f)
    data=list(reader)
data.pop(0)
import numpy as np
MarksPercent=[]
RollNo=[]
for n in data:
    MarksPercent.append(float(n[0]))
    RollNo.append(float(n[1]))
correlation = np.corrcoef(MarksPercent,RollNo)
print(correlation[0,1])
# the correlation coefficient value is 0 which means that the data is not correlated