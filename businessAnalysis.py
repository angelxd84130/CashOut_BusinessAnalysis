from dataProcessing import getData

''' analysis both event tracking & betting history data and output result plots '''
Event, History = getData()

# count people
from bettingPopulation import population_distribution
yesList, noList, yes_population, no_population = population_distribution(History)

# count time[sec]
from bettingTime import time_distribution
time_distribution(Event, yesList, noList)

# count betting
from bettingNum import betting_distribution
yesHistory, noHistory, yes_Num, no_Num = betting_distribution(History, yesList, noList)

# count device
from bettingDevice import device_distribution
device_distribution(History, yesList, noList)

# count SportCode
from bettingSportCode import sportCode_distribution
sportCode_distribution(History, yesList, noList)