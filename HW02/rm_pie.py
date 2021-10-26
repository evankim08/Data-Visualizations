#Generate two plots, one from each of your datasets, satisfying the following requirements:
# I. You may select any time of plot that you want (e.g., line, bar, scatter, etc.), but you must select two different plots.
# II. At least one of your plots must contain two different data sources. (For example, two different lines in a line graph, or two different sets of bars in a bar chart).
# III. The plots should have properly labeled x and y axes, and a legend (only needed for the plot containing multiple data sources).
# IV. The tic labels for both the x and y axes should appear in a reasonable order (e.g. sorted), and they must be legible.
import matplotlib
from matplotlib import pyplot as plt

import numpy as np
import json

with open('rmcharacters.json') as text:
    rmcharacters = text.read()

rick = json.loads(rmcharacters)

#PLOT 1 : PIE CHART

statuslist = []
for item in rick['results']:
    statuslist.append(item['status'])

x = statuslist.count("Alive")
y = statuslist.count("Dead")
z = statuslist.count("unknown")

numstatuslist = [x,y,z]
labels = ["Alive", "Dead", "Unknown"]
explode = [0,0.1,0]
colors = ['#A9F3FD','#02AFC5','#FAFD7CFF']

plt.pie(numstatuslist, labels = labels, colors=colors, explode=explode, shadow = True, startangle=90, autopct="%1.1f%%", wedgeprops={'edgecolor': 'black'})

plt.title("Status of Characters in Rick and Morty")
plt.savefig('rickandmortycharacterstatus.jpg')
plt.show()



