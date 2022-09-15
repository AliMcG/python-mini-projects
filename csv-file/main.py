# with open("./weather_data.csv") as data_file:
#   raw_data = data_file.readlines()
#   data = [ data.strip() for data in raw_data]
#   print(data)

# import csv

# with open("./weather_data.csv") as data_file:
#   data = csv.reader(data_file)
#   temperature = []
#   for row in data:
#     if row[1].isdigit():
#       print(int(row[1]))
#       temperature.append(int(row[1]))
#     # x = int(row[1])
#   #   
#   print(temperature)
  
import pandas as pd

data = pd.read_csv("./weather_data.csv")
print(data["temp"])