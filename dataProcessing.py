import glob
import pandas as pd

''' merge all data in the folders '''

# set folder path
files = glob.glob("data/*.csv")

def getData():
    mergeEvent = []
    mergeHistory = []
    for file in files:
        # load eventTracking data
        eventTracking = pd.read_csv(file)
        # get start/ end date from file name
        startDate = file.split("\\")[-1][:10]
        endDate = file.split("\\")[-1][11:21]
        # filter bettingHistory data by date
        print(startDate, endDate)
        bettingData = pd.read_csv("data/bettingHistory/" + startDate + '_' + endDate + '_bettingHistory.csv',
                                  encoding='utf-8')
        mergeEvent.append(eventTracking)
        mergeHistory.append(bettingData)

    # merge file
    Event = pd.concat(mergeEvent)
    History = pd.concat(mergeHistory)

    # reduce unusable columns
    bettingHistory = History[['MainAccountID', 'BetResult', 'SportCode', 'EventCode', 'RealBetAmount', 'DeviceType', 'WebVersion', 'BetDatetime']]

    return Event, bettingHistory
