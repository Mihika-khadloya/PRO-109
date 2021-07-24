import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st
import csv

df=pd.read_csv("StudentsPerformance.csv")
data=df["reading score"].tolist()
mean=st.mean(data)
sd=st.stdev(data)
print(sd,mean)

sd1start , sd1end=mean-sd,mean+sd
sd2start,sd2end=mean-(2*sd),mean+(2*sd)
sd3start,sd3end=mean-(3*sd),mean+(3*sd)

fig=ff.create_distplot([data],["Result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[sd1start,sd1start],y=[0,0.17],mode="lines",name="SD1"))
fig.add_trace(go.Scatter(x=[sd1end,sd1end],y=[0,0.17],mode="lines",name="SD1"))
fig.add_trace(go.Scatter(x=[sd2start,sd2start],y=[0,0.17],mode="lines",name="SD2"))
fig.add_trace(go.Scatter(x=[sd2end,sd2end],y=[0,0.17],mode="lines",name="SD2"))
fig.show()

list_of_data_between_sd1=[result for result in data if result>sd1start and result<sd1end]
list_of_data_between_sd2=[result for result in data if result>sd2start and result<sd2end]
list_of_data_between_sd3=[result for result in data if result>sd3start and result<sd3end]

print("{}% of data lies within 1 standard deviation", format(len(list_of_data_between_sd1)*100.0/len(data)))

print("{}% of data lies within 2 standard deviation", format(len(list_of_data_between_sd2)*100.0/len(data)))

print("{}% of data lies within 3 standard deviation", format(len(list_of_data_between_sd3)*100.0/len(data)))
