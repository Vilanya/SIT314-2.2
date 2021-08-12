import chart_studio
chart_studio.tools.set_credentials_file(username='Vilanya', api_key='ZPzPNqvben0JgHmTF5a9')
chart_studio.tools.set_config_file(world_readable=True,
                             sharing='public')                             
import chart_studio.plotly as py
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("MData.csv")

fig = go.Scatter(x = df['Time'], y = df['Data'],
                  name='Soil Moisture data')
data = [fig]
py.plot(data, filename = 'basic-line', auto_open=True)                             
                             
                             
