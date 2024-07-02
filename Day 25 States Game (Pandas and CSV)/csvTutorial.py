# CSV: Comma Separated Values
import csv

day, temperature, weather = [], [], []
with open("C:/Users/minia/Documents/Projects/Python-100-Days-of-Code-Bootcamp/Day 25/weather_data.csv") as weatherData:
    data = csv.reader(weatherData)
    for row in data:
        if (row[0] != "day"):
            day.append(row[0])
            temperature.append(row[1])
            weather.append(row[2])

print(day)
print(temperature)
print(weather)
