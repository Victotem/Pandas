'''import csv

list1 = []
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))'''

'''
temp_list = data.temp.to_list()
print(temp_list)
n=0
for x in temp_list:
    n = n + x

average= n/len(temp_list)
print(average)
'''

import pandas


data = pandas.read_csv("all_squirrels.csv")
cinnamon_count=(len(data[data["Primary Fur Color"] == "Cinnamon"]))
gray_count=(len(data[data["Primary Fur Color"] == "Gray"]))
black_count=(len(data[data["Primary Fur Color"] == "Black"]))

data_dict = {
    "Fur Color": ["Gray", "Cinnamon","Black"],
    "Count": [cinnamon_count,gray_count,black_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

