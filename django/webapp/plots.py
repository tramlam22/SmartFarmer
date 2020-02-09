from plotly.offline import plot
import plotly.graph_objs as go 
import pandas as pd 
from datetime import datetime 
import requests
import numpy as np
from .models import *
from django.db import connection

cursor = connection.cursor()

class sensorData():
    user = ''
    moduleList = []

    #set user to find the appropriate data
    def __init__(self, current_user):
        self.user = current_user
        #self.moduleList = [module.mcu_no for module in modulePlantLink.objects.filter(username=self.user)]

    #get avg graphs for certain time intervals
    #default page should be at hours
    def getAvgGraph(self, typeofData, dateInterval):
     #   timeData, x, y = [], [], []
        cmd = """SELECT date_data, AVG({})FROM dataMCU GROUP BY DATE(date_data), HOUR(date_data)""".format(typeofData, moduleList[num])
        cursor.execute(cmd)
        avgDataList = cursor.fetchall()
        x = [row[0] for row in avgDataList]
        y = [row[0] for row in avgDataList]

        figure = go.Figure()
        figure.add_trace(go.Scatter(x=x,y=y,mode='lines',
            name = typeofData,
            line = dict(color="#ff0000", width = 4),
            connectgaps = True,
        ))

        plot_div = plot(figure, output_type='div', include_plotlyjs=False)
        return plot_div

    def createTestGraph(self):
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

    