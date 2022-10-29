import pandas

def celcius_to_farenhite(x):
    x = x * 1.8 + 32
    return float(x)

data = pandas.read_csv("weather_data.csv")
monday_temp = data[data.day == "Monday"].temp
print(f"In celcius : {int(monday_temp)}\tIn Farenhite : {float(monday_temp.apply(celcius_to_farenhite))}")