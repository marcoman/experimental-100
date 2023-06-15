import os
import pandas
import csv

temperatures = []
weather_data = []

def print_csv_data(mydata):
    for r in mydata:
        print(r)

def read_csv_data(myfile):
    ret_data = []
    with open (myfile) as f:
        data = csv.reader(f)
        for r in data:
            ret_data.append(r)
    return ret_data

def get_temperature(data):
    temp = []
    for r in data:
        if r[1] != 'temp':
            temp.append(int(r[1]))
    return temp
                
def panda_read_csv_data(myfile):
    panda_data = pandas.read_csv(myfile)
    return panda_data

weather_data = read_csv_data('weather_data.csv')
temperature_data = get_temperature(weather_data)
print (weather_data)
print (temperature_data)

pd_weather_data = panda_read_csv_data('weather_data.csv')
print (pd_weather_data)
print (pd_weather_data['temp'])
print (pd_weather_data.temp)
## Some statistical information on the temperature series
print (pd_weather_data.temp.max())
print (pd_weather_data.temp.mean())
print (pd_weather_data.temp.median())
print (pd_weather_data.temp.min())
print (pd_weather_data.temp.tolist())
print (pd_weather_data.temp.std())

# Same:
print (f"stat max: {pd_weather_data['temp'].max()}")
print (f"stat mean: {pd_weather_data['temp'].mean()}")
print (f"stat medium: {pd_weather_data['temp'].median()}")
print (f"stat min: {pd_weather_data['temp'].min()}")
print (f"stat std: {pd_weather_data['temp'].std()}")
print (f"tolist: {pd_weather_data['temp'].tolist()}")


# Filter / selectors
# Find the day with the temperature of 15
print(f"What day is the temperature 15? \n{pd_weather_data[pd_weather_data['temp'] == 15]}")
# find the row for Monday
print(f"What are the rows where the day is Monday? \n{pd_weather_data[pd_weather_data['day'] == 'Monday']}")
# find the row for the day that contains the letter T
print(f"What row has the letter T? \n{pd_weather_data[pd_weather_data['day'].str.contains('T')]}")

# get the row with the maximum temperature
print(f"What row has the max temperature? \n{pd_weather_data[pd_weather_data['temp'] == pd_weather_data['temp'].max()]}")
# print the day where the temperature is the maximum
print('what day has the max temperature? ' + pd_weather_data[pd_weather_data['temp'] == pd_weather_data['temp'].max()].day)


# Create dataframe from scratch

mydict = {
    'students': ['Amelia', 'Barbara', 'Crystal'],
    'scores': [76, 56, 65]
}

pd_mydict = pandas.DataFrame(mydict)

print (pd_mydict)
pd_mydict.to_csv('pd_mydict.csv')

