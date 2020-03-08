from webapp.plots import *
from webapp.tests import sendAlert


class dataAnalysis():

    def tempAlgorithm(self, average_temp):
        if(average_temp > 20.0 and average_temp < 29):
            feedback_message = "Temperature is great!"
        elif(average_temp < 20.0):
            feedback_message = "Your temperature is not ideal! the temperature is too low!"
        elif(average_temp > 29):
            feedback_message = "Your temperature is not ideal! the temperature is too high!"
        return feedback_message

    def humidityAlgorithm(self, average_humidity):
        if(average_humidity > 65.0 and average_humidity < 75):
            feedback_message = "Humidity level is good!"
        elif(average_humidity < 65.0):
            feedback_message = "Humidity level is not ideal! Humidity is too low!"
        elif(average_humidity > 75):
            feedback_message = "Humidity level is not ideal! Humidity is too high!"
        return feedback_message

    def lightAlgorithm(self, average_light_reading):
        if(average_light_reading > 65.0 and average_light_reading < 75):
            feedback_message = "Light level is good!"
        elif(average_light_reading < 65.0):
            feedback_message = "Light level is not ideal! Light is too low!"
        elif(average_light_reading > 75):
            feedback_message = "Light level is not ideal! Light is too high!"
        return feedback_message

    def soilMoistureAlgorithm(self, average_soil_moisture):
        if(average_soil_moisture > 65.0 and average_soil_moisture < 75):
            feedback_message = "Soil moisture level is good!"
        elif(average_soil_moisture < 65.0):
            feedback_message = "Soil moisture level is not ideal! Soil moisture is too low!"
        elif(average_soil_moisture > 75):
            feedback_message = "Soil moisture level is not ideal! Soil moisture is too high!"
        return feedback_message

    def soilTempAlgorithm(self, average_soil_temp):
        if(average_soil_temp > 65.0 and average_soil_temp < 75):
            feedback_message = "Soil temperature level is good!"
        elif(average_soil_temp < 65.0):
            feedback_message = "Soil temperature level is not ideal! Soil temperature is too low!"
        elif(average_soil_temp > 75):
            feedback_message = "Soil temperature level is not ideal! Soil temperature is too high!"
        return feedback_message

    def algorithm(self):
        number_of_entries = 10
        data_date = []  # data_date from the last 'number' of entries
        soil_temp = []  # soil_temp from the last 'number' of entries
        soil_moisture = []  # soil_moisture from the last 'number' of entries
        temp = []  # temp from the last 'number' of entries
        humidity = []  # humidity from the last 'number' of entries
        light_reading = []
        recent_data = []  # data from the last 'number' of  entries
        sensor_data = sensorData("farm")
        
        average_temp = 0
        average_soil_temp = 0
        average_soil_moisture = 0
        average_humidity = 0
        average_light_reading = 0
        recent_date = ""
        feedback = ""
        suggestion_message = ""
        notification = ""
        msg = ""


        #mysql connection
        cursor = connection.cursor()

        #cmd for getting average values
        cmd = """SELECT AVG(temp)
                    FROM dataMCU 
                    WHERE '2020-02-20' = DATE(data_date)"""
        cursor.execute(cmd)
        average_temp = cursor.fetchone()[0]
        cmd = """SELECT AVG(humidity)
                    FROM dataMCU 
                    WHERE '2020-02-20' = DATE(data_date)"""
        cursor.execute(cmd)
        average_humidity = cursor.fetchone()[0]
        cmd = """SELECT AVG(soil_moisture)
                    FROM dataMCU 
                    WHERE '2020-02-20' = DATE(data_date)"""
        cursor.execute(cmd)
        average_soil_moisture = cursor.fetchone()[0]
        cmd = """SELECT AVG(soil_temp)
                    FROM dataMCU 
                    WHERE '2020-02-20' = DATE(data_date)"""
        cursor.execute(cmd)
        average_soil_temp = cursor.fetchone()[0]
        cmd = """SELECT AVG(light_reading)
                    FROM dataMCU 
                    WHERE '2020-02-20' = DATE(data_date)"""
        cursor.execute(cmd)
        average_light_reading = cursor.fetchone()[0]



        # getting all the data base entries in the form of a list
        # all_data = sensorData.getAllData(self)
        """

        # loading the list, recent_data with just a given number of dictionaries
        for i in range(number_of_entries):
            recent_data.append(all_data[i])

        # loading each list with their specified values in the dictionary
        for i in range(number_of_entries):
            data_date.append(recent_data[i]['data_date'])
            soil_temp.append(recent_data[i]['soil_temp'])
            temp.append(recent_data[i]['temp'])
            humidity.append(recent_data[i]['humidity'])
            soil_moisture.append(recent_data[i]['soil_moisture'])
            light_reading.append(recent_data[i]['light_reading'])


        for i in range(number_of_entries):  # calculating averages
            average_temp += temp[i]
            average_soil_temp += soil_temp[i]
            average_soil_moisture += soil_moisture[i]
            average_humidity += humidity[i]
            average_light_reading += light_reading[i]

        average_temp /= number_of_entries
        average_soil_temp /= number_of_entries
        average_soil_moisture /= number_of_entries
        average_humidity /= number_of_entries
        average_light_reading /= number_of_entries
        recent_date = data_date[0]"""

        msg = self.tempAlgorithm(average_temp)
        feedback += msg
        if "low" in msg:
            suggestion_message = "Increase temperature to yield optimal strawberries!"
            notification = "Temperature is below optimal!"
        if "high" in msg:
            suggestion_message = "Lower temperature to yield optimal strawberries!"
            notification = "Temperature is too high!"

        feedback += "\n"
        msg = self.humidityAlgorithm(average_humidity)
        feedback += msg
        if "low" in msg:
            suggestion_message = "Irrigate more to yield optimal strawberries!"
            notification = "Low humidity level!"

        feedback += "\n"
        msg = self.lightAlgorithm(average_light_reading)
        feedback += msg
        if "low" in msg:
            suggestion_message = "Increase Light exposure to yield optimal strawberries!"
            notification = "Light level is below optimal!"
        if "high" in msg:
            suggestion_message = "Lower light exposure to yield optimal strawberries!"
            notification = "Light level is too high!"

        feedback += "\n"
        msg = self.soilMoistureAlgorithm(average_soil_moisture)
        feedback += msg

        if "low" in msg:
            suggestion_message = "Increase soil moisture to yield optimal strawberries!"
            notification = "Soil moisture is below optimal!"
        if "high" in msg:
            suggestion_message = "Lower soil moisture to yield optimal strawberries!"
            notification = "Soil moisture is too high!"

        feedback += "\n"
        msg = self.soilTempAlgorithm(average_soil_temp)
        feedback += msg

        if "low" in msg:
            suggestion_message = "Increase soil temperature to yield optimal strawberries!"
            notification = "Soil temperature is below optimal!"
        if "high" in msg:
            suggestion_message = "Lower soil temperature to yield optimal strawberries!"
            notification = "Soil temperature is too high!"

        if "ideal" in feedback:
            sendAlert("efai", feedback)

        feedback = feedback.split('\n')
        return average_temp, average_soil_temp, average_soil_moisture, average_humidity, recent_date, average_light_reading, feedback, suggestion_message, notification

    
