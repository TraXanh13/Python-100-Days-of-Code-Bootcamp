# Pandas
import pandas

data = pandas.read_csv(
    "C:/Users/minia/Documents/Projects/Python-100-Days-of-Code-Bootcamp/Day 25/weather_data.csv")

# DataFrames
# print(type(data))

# Data Series
# print(type(data["temp"]))

# Print the column temp contents
# print(f"\n{data['temp']}")
#
# Output:
# 0    12
# 1    14
# 2    15
# 3    14
# 4    21
# 5    22
# 6    24

# Convert to list
dataDict = data.to_dict()
print(dataDict)

# Convert to series list
tempList = data["temp"].to_list()
print(tempList)

# Get the average of the temp column
print(data["temp"].mean())

# Get the max of the temp column
print(data["temp"].max())

# Getting Data in Columns
# print(data["condition"])
# print(data.condition)

# Gets the row that matches the condition
print(data[data.day == "Tuesday"])

# Get the row with the max temp
print(data[data.temp == data.temp.max()])

# Get monday's temp in fahrenheit
monday = data[data.day == "Monday"]
print(f"{monday.temp * 9/5 + 32}F")

# Create a dataframe from scratch
dataDict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

classData = pandas.DataFrame(dataDict)
print(classData)

# Creates a csv file with the data
classData.to_csv(
    "C:/Users/minia/Documents/Projects/Python-100-Days-of-Code-Bootcamp/Day 25/classData.csv")
