import pandas as pd
import numpy as np
import plotly.express as px
import plotly.offline as py
import plotly.graph_objects as go

data = pd.read_csv(r"C:\Users\Pramod\Desktop\Kohli performance.csv")
print(data.head())
print(data.isnull().sum())      # returns the number of missing values in the data set

# total runs between 18 August 2008 to 22 Jan 2017
print("total runs : ", data["Runs"].sum())

# Average Runs between 18 August 2008 to 22 Jan 2017
print(" average runs : ", data["Runs"].mean())

# trend of runs scored by Virat Kohli in his career from 18 August 2008 to 22 January 2017
matches = data.index
figure = px.line(data, x=matches, y="Runs", title='Runs Scored by Virat Kohli Between 18 August 2008 to 22 January 2017')

print(py.plot(figure))

# Batting positions
data["Pos"] = data["Pos"].map({3.0: "Batting at 3", 4.: "Batting at 4", 2.0: "Batting At 2", 1.0: "Batting At 1",7.0:"Batting At 7", 5.0:"Batting At 5", 6.0: "batting At 6"})
Pos = data["Pos"].value_counts()
label = Pos.index
count = Pos.values
colors = ['gold','lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]
ppp = go.Figure(data=[go.Pie(labels=label, values=count)])
ppp.update_layout(title_text='Number of Matches At Different Batting Positions')
ppp.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black',width=3)))
print(py.plot(ppp))
# total runs scored by Virat Kohli in different positions:
labels = data["Pos"]
counts = data["Runs"]
colors = ["gold", "lightgreen", "pink", "blue", "skyblue", "cyan", "orange"]
fig = go.Figure(data=[go.Pie(labels=labels, values=counts)])
fig.update_layout(title_text='Runs by Virat Kolhi at different batting positions')
fig.update_traces(hoverinfo= 'label+percent', textinfo='value', textfont_size= 30, marker=dict(colors=colors, line=dict(color='black',width=3)))
print(py.plot(fig))

#number of centuries scored by Virat Kohli while batting in the first innings and second innings:
centuries = data.query("Runs >= 100")
figure = px.bar(centuries, x=centuries["Inns"], y=centuries["Runs"], color=centuries["Runs"], title="Centuries By Virat Kohli in First Innings Vs. Second Innings")
print(py.plot(figure))

# kind of dismissals Virat Kohli faced most of the time:
# Dismissals of Virat Kohli
dismissal = data["Dismissal"].value_counts()
labelss = dismissal.index
countss = dismissal.values
colors = ['gold','lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]
figg = go.Figure(data=[go.Pie(labels=labelss, values=countss)])
figg.update_layout(title_text='Dismissal of Virat Kohli')
figg.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30, marker=dict(colors=colors,line=dict(color='black', width=3)))
print(py.plot(figg))

aaa = px.bar(data, x=data["Opposition"], y = data["Runs"], color = data["Runs"], title="Most runs against teams")
print(py.plot(aaa))
# at against which team Virat Kohli scored most of his centuries:
bbb = px.bar(centuries, x=centuries["Opposition"], y=centuries["Runs"], color=centuries["Runs"])
print(py.plot(bbb))

# Virat Kohli’s strike rate
strike_rate = data.query("SR >= 120")
print(strike_rate)

# Virat Kohli plays with high strike rates in the first innings or second innings:?

ccc = px.bar(strike_rate, x = strike_rate["Inns"], y = strike_rate["SR"], color = strike_rate["SR"], title="Virat Kohli's High Strike Rates in First Innings Vs. Second Innings")
py.plot(ccc)
# relationship between runs scored by Virat Kohli and fours played by him in each innings:
dddd = px.scatter(data_frame= data, x="Runs", y="4s", size="SR", trendline="ols", title="Relationship between Runs Scored and Fours")
print(py.plot(dddd))

#relationship with the sixes:
abcd = px.scatter(data_frame=data, x="Runs", y="6s", size="SR", trendline="ols", title="Relationship Between Runs Scored and Sixes")
print(py.plot(abcd))


