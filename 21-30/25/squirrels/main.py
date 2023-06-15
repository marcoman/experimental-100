import pandas as pd

FILENAME = '2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'

def create_dataframe(filename):
    df = pd.read_csv(filename)
    return df

def create_list(dataseries):
    if dataseries.hasnans():
        dataseries = dataseries.dropna()
    return(dataseries.tolist())

squirrel_data = create_dataframe(FILENAME)

# print the different color types
squirrel_colors = (squirrel_data["Primary Fur Color"].unique())
squirrel_colors = [element for element in squirrel_colors if str(element) != 'nan']
print (squirrel_colors)

# given a list of colors, let's find out many squirrels exist of each
new_dict = {}
for color in squirrel_colors:
    print (color, len(squirrel_data[squirrel_data["Primary Fur Color"] == color]))
    new_dict[color] = len(squirrel_data[squirrel_data["Primary Fur Color"] == color])   
print (new_dict)

pd_new_dict = pd.DataFrame(new_dict, index=[0])
print (pd_new_dict)
pd_new_dict.to_csv('squirrel_count.csv')
