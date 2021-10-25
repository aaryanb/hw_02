import json
import matplotlib.pyplot as plt
import os


usa_gdp = []
files_usa = ['usa_gdp.json']
for file_usa in files_usa:
    with open(file_usa, encoding='ascii') as f_usa:
        text_usa = f_usa.read()
        usa_gdp += json.loads(text_usa)

x_usa=[]
for dict in usa_gdp[1]:
    x_usa.append(dict['value'])

china_gdp = []
files_china = ['china_gdp.json']
for file_china in files_china:
    with open(file_china, encoding='ascii') as f_china:
        text_china = f_china.read()
        china_gdp += json.loads(text_china)

y_china=[]
for dict in china_gdp[1]:
    y_china.append(dict['value'])

# plot the data
plt.xlabel('USA Gross Domestic Product (units in ten trillions)')
plt.ylabel('China Gross Domestic Product (units in ten trillions)')
plt.title('GDP of USA vs China')
plt.scatter(x_usa, y_china)
plt.savefig('usa_china_gdp_comparison.png')
plt.show()



