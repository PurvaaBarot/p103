import pandas as pd
import plotly_express as px

df = pd.read_csv("Projectfile1class103.csv")
fig1 = px.bar(df , x="date", y="cases" , color="Country" )
fig2 = px.scatter(df , x="date", y="cases" , color="Country")
fig1.show()
fig2.show()

