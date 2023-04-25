import pandas

data = pandas.read_csv(
    "C:/Users/minia/Documents/Projects/Python-100-Days-of-Code-Bootcamp/Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

greys = len(data[data["Primary Fur Color"] == "Gray"])
reds = len(data[data["Primary Fur Color"] == "Cinnamon"])
blacks = len(data[data["Primary Fur Color"] == "Black"])

squirrelData = {
    "Fur Color": ["Grey", "Red", "Black"],
    "Count": [greys, reds, blacks]
}

squirrelData = pandas.DataFrame(squirrelData)

squirrelData.to_csv(
    "C:/Users/minia/Documents/Projects/Python-100-Days-of-Code-Bootcamp/Day 25/squirrelData.csv")
