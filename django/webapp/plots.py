from plotly.offline import plot
import plotly.graph_objs as go 
import pandas as pd 
from datetime import datetime 
import requests
import numpy as np
from .models import Testtemp

def get_graph():
    data = Testtemp.objects.all()
    x = [row.id for row in data]
    y = [row.temp for row in data]
    
    figure = go.Figure()
    figure.add_trace(go.Scatter(x=x,y=y,mode='lines',
            name = "Testing",
            line = dict(color="#ff0000", width = 4),
            connectgaps = True,
    ))

    plot_div = plot(figure, output_type='div', include_plotlyjs=False)
    return plot_div
'''    x = np.arange(10)
    figure = go.Figure(data=go.Scatter(x=x, y=x**2)) 
    plot_div = plot(figure, output_type='div', include_plotlyjs=False)
'''
 



    