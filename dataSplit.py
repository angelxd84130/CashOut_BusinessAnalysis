import pandas as pd

''' split every 5 days' data into a csv file '''

bettingData = pd.read_csv("data/tmp/202107 - 複製.csv")
# date = "2021-06-"
date = "2021-07-"
startDate = ['01', '06', '11', '16', '21', '26']
#endDate = ['05', '10', '15', '20', '25', '30']
endDate = ['05', '10', '15', '20', '25', '31']


for i in range(len(startDate)):

    bettingHistory = bettingData[(bettingData['TransactionMCreateDatetime'] >= (date+startDate[i])) & (bettingData['TransactionMCreateDatetime'] <= (date+endDate[i]))]
    print("check\n", bettingHistory)
    bettingHistory.to_csv("data/"+date+startDate[i]+'_'+date+endDate[i]+'_bettingHistory.csv')
