import numpy as np
import matplotlib.pyplot as plt
def calculate_temperature(humidity):
    a = 0.002
    b = 0.1
    c = 20.0
    temperature = a * humidity**2 + b * humidity + c
    return temperature
def calculate_temperature_from_pressure(pressure):
    slope = 0.02
    intercept = 10.0
    temperature = slope * pressure + intercept
    return temperature
def read_inputs_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            humidity_values = [float(line.strip()) for line in lines[:len(lines)//2]]
            pressure_values = [float(line.strip()) for line in lines[len(lines)//2:]]
        return humidity_values, pressure_values
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return [], []
file_path = 'input_data.txt' 
humidities, pressures = read_inputs_from_file(file_path)
temperatures_humidity = [calculate_temperature(h) for h in humidities]
temperatures_pressure = [calculate_temperature_from_pressure(p) for p in pressures]
plt.plot(humidities, temperatures_humidity, label='Predicted Temperature (Humidity)', color='red')
plt.title('Temperature vs. Humidity')
plt.xlabel('Humidity')
plt.ylabel('Temperature')
plt.legend()
plt.show()
plt.plot(pressures, temperatures_pressure, label='Predicted Temperature (Pressure)', color='blue')
plt.title('Temperature vs. Pressure')
plt.xlabel('Pressure')
plt.ylabel('Temperature')
plt.legend()
plt.show()
