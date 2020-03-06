from webapp.plots import *

class dataAnalysis():
    
    def tempAlgorithm(self, average_temp):
        if(average_temp > 20.0 and average_temp < 29 ):
            suggestion_message = "Temperature is great!"
        elif(average_temp < 20.0):        
            suggestion_message = "Your temperature is not ideal! the temperature is too low!"
        elif(average_temp > 29):
            suggestion_message = "Your temperature is not ideal! the temperature is too high!"
        return suggestion_message
    
    def humidityAlgorithm(self, average_humidity):
        if(average_humidity > 65.0 and average_humidity < 75 ):
            suggestion_message = "Humidity level is good!"
        elif(average_humidity < 65.0):        
            suggestion_message = "Humidity level is not ideal! Humidity is too low!"
        elif(average_humidity > 75):
            suggestion_message = "Humidity level is not ideal! Humidity is too high!"
        return suggestion_message
    
    
    def algorithm(self):
        number_of_entries = 10
        data_date = []                                  #data_date from the last 'number' of entries
        soil_temp = []                                  #soil_temp from the last 'number' of entries
        soil_moisture = []                              #soil_moisture from the last 'number' of entries
        temp = []                                       #temp from the last 'number' of entries
        humidity = []                                   #humidity from the last 'number' of entries
        light_reading = []
        recent_data = []                                #data from the last 'number' of  entries 
        sensor_data = sensorData("farm")
        all_data = sensorData.getAllData(self)          #getting all the data base entries in the form of a list
        average_temp = 0
        average_soil_temp = 0
        average_soil_moisture = 0
        average_humidity = 0
        average_light_reading = 0
        recent_date = ""
        suggestion_message = ""
      
        
        for i in range(number_of_entries):                  #loading the list, recent_data with just a given number of dictionaries
            recent_data.append(all_data[i])     
        
        for i in range(number_of_entries):                  #loading each list with their specified values in the dictionary
            data_date.append(recent_data[i]['data_date'])
            soil_temp.append(recent_data[i]['soil_temp'])
            temp.append(recent_data[i]['temp'])
            humidity.append(recent_data[i]['humidity'])
            soil_moisture.append(recent_data[i]['soil_moisture'])  
            light_reading.append(recent_data[i]['light_reading'])

        for i in range(number_of_entries):                  #calculating averages
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
        recent_date = data_date[0]
        
        suggestion_message += self.tempAlgorithm(average_temp)
        suggestion_message += " and "
        suggestion_message += self.humidityAlgorithm(average_humidity)


        return average_temp, average_soil_temp, average_soil_moisture, average_humidity, recent_date, average_light_reading, suggestion_message
    