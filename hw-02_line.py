import json
import matplotlib.pyplot as plt
import os

india_gdp = []
files_india = ['india_gdp.json']
for file_india in files_india:
    with open(file_india, encoding='ascii') as f_india:
        text_india = f_india.read()
        india_gdp += json.loads(text_india)

y_india=[]
for dict in india_gdp[1]:
    y_india.append(dict['value'])

x_india=[]
for year_india in range(2020, 1959, -1):
    x_india.append(year_india)

china_gdp = []
files_china = ['china_gdp.json']
for file_china in files_china:
    with open(file_china, encoding='ascii') as f_china:
        text_china = f_china.read()
        china_gdp += json.loads(text_china)

y_china=[]
for dict in china_gdp[1]:
    y_china.append(dict['value'])

x_china=[]
for year_china in range(2020, 1959, -1):
    x_china.append(year_china)


# plot the data
plt.xlabel('Years')
plt.ylabel('Gross Domestic Product (units in ten trillions)')
plt.title('GDP of India vs China Over Time')
plt.plot(x_india, y_india, label = 'India\'s GDP')
plt.plot(x_china, y_china, label = 'China\'s GDP')
plt.legend()
plt.savefig('china_india_gdp_comparison.png')



