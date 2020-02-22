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

    # set user to find the appropriate data
    def __init__(self, current_user):
        self.user = current_user
        #self.moduleList = [module.mcu_no for module in modulePlantLink.objects.filter(username=self.user)]

    # get avg graphs for certain time intervals
    # default page should be at hours
    def getAvgGraph(self, typeofData, timeInterval):

        if timeInterval == "hour":
            cmd = """SELECT data_date, AVG({})
                    FROM dataMCU 
                    GROUP BY DATE(data_date), HOUR(data_date)""".format(typeofData)
        elif timeInterval == "day":
            cmd = """SELECT data_date, AVG({})
                    FROM dataMCU 
                    GROUP BY DATE(data_date)""".format(typeofData)
        elif timeInterval == "months":
            cmd = """SELECT data_date, AVG({})
                    FROM dataMCU 
                    GROUP BY MONTH(data_date)""".format(typeofData)

        cursor.execute(cmd)
        avgDataList = cursor.fetchall()
        x = [row[0] for row in avgDataList]
        y = [row[1] for row in avgDataList]

        figure = go.Figure()
        figure.add_trace(go.Scatter(x=x, y=y, mode='lines',
                                    name=typeofData,
                                    line=dict(color="#5AFFC9", width=4),
                                    connectgaps=True,
                                    ))

        plot_div = plot(figure, output_type='div', include_plotlyjs=False)
        return plot_div

    # get graphs for each module
    def moduleGraph(self, typeofData, timeInterval):
        for module in moduleList:
            cmd = """SELECT AVG({})
                    FROM dataMCU
                    WHERE mcu_no = {}
                    GROUP BY HOUR(date_data)""".format(typeofData, module)
        cursor.execute(cmd)
        moduleData = cursor.fetchall()
        x = [row[0] for row in moduleData]

    # for testing purposes

    def createTestGraph(self):
        data = Testtemp.objects.all()
        x = [row.id for row in data]
        y = [row.temp for row in data]

        figure = go.Figure()
        figure.add_trace(go.Scatter(x=x, y=y, mode='lines',
                                    name="Testing",
                                    line=dict(color="#ff0000", width=4),
                                    connectgaps=True,
                                    ))

        plot_div = plot(figure, output_type='div', include_plotlyjs=False)
        return plot_div

    # getting all data, delete after
    def getAllData(self):
        data = dataMCU.objects.values(
            'data_date', 'soil_temp', 'soil_moisture', 'temp', 'humidity').order_by('-data_date')
        x = data
        return x
