#! ./bin/python

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


#first plot test
#fig1 = go.Figure(data=go.Bar(y=[2, 3, 1]))
#fig1.write_html('first_figure.html', auto_open=True)

df = pd.read_csv('./bme280/weather_BME280_sensor_data.txt', sep=" ", names=('Date', 'Time', 'Temp', 'Pressure', 'Humidity'))
df['DateTime'] = df['Date'] + " " + df['Time']
df['dt'] = pd.to_datetime(df['DateTime'])
# print(df)
print(df.info())

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df['dt'],
    y=df['Temp'],
    name="Temperature data",
    line=dict(color="#1f77b4"),
))

fig.add_trace(go.Scatter(
    x=df['dt'],
    y=df['Pressure'],
    name="Pressure data",
    line=dict(color="#228B22"), # forest green
    yaxis="y2"
))

fig.add_trace(go.Scatter(
    x=df['dt'],
    y=df['Humidity'],    
    name="Humidity",
    line=dict(color="#d62728"),
    yaxis="y3"
))

# Create axis objects
fig.update_layout(
    xaxis=dict(domain=[0.1, 1.0]),
    yaxis=dict(
        title="Temperature",
        titlefont=dict(color="#1f77b4"),
        tickfont=dict(color="#1f77b4")
    ),
    yaxis2=dict(
        title="Pressure",
        titlefont=dict(color="#228B22"),
        tickfont=dict(color="#228B22"),
        anchor="free",
        overlaying="y",
        side="left",
        position=0.05
    ),
    yaxis3=dict(
        title="Humidity",
        titlefont=dict(color="#d62728"),
        tickfont=dict(color="#d62728"),
        anchor="x",
        overlaying="y",
        side="right"
        #position=0.1
    )
)

# Update layout properties
fig.update_layout(
    title_text="Temperature, Pressure, Humidity",
    #width=800,
)

#fig.show()
fig.write_html('bme-280_data.html', auto_open=True)
