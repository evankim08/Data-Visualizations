#PLOT 2: LINE GRAPH (MURDER RATES)

import matplotlib
from matplotlib import pyplot as plt

import numpy as np
import json

with open('crime.json','r') as text:
    crimerates = text.read()

crime = json.loads(crimerates)

miamix = []
miamiy = []
tampax = []
tampay = []

for element in crime['data']:
    if element[11] == "Miami, FL" and element[12] == "Murder and nonnegligent manslaughter":
        x = element[10]
        y = element[13]
        miamix.append(x)
        miamiy.append(y)
    
    elif element[11] == "Tampa, FL" and element[12] == "Murder and nonnegligent manslaughter":
        x = element[10]
        y = element[13]
        tampax.append(x)
        tampay.append(y)

#Building dictionaries from the two lists, so we can manipulate order without interfering with data pairings
miamikeys = miamix
miamivalues = miamiy
miamidictionary = dict(zip(miamikeys, miamivalues))

tampakeys = tampax
tampavalues = tampay
tampadictionary = dict(zip(tampakeys, tampavalues))

#Reorder the dictionary from the earliest date to the most recent date so that data pairings remain intact, and build information for the axes
miami_xaxis = sorted(miamidictionary)
miami_yaxis = [float(miamidictionary[element]) for element in miami_xaxis]

tampa_xaxis = sorted(tampadictionary)
tampa_yaxis = [float(tampadictionary[element]) for element in tampa_xaxis]

#Plot the line graph, using the two data sources

plt.xlabel('Year')
plt.ylabel('Number of Murder Cases')
plt.title('Miami, FL vs. Tampa, FL Murder Rates (2005-2014)')
plt.plot(miami_xaxis, miami_yaxis, color = '#D9514EFF', marker = 'o' , linewidth = 3, label = 'Miami')
plt.plot(tampa_xaxis, tampa_yaxis, color = '#2A2B2DFF', marker = 'o', linewidth = 3, label = 'Tampa')
plt.tight_layout()
plt.legend()
plt.savefig('floridamurderrates.jpg')

plt.show()


