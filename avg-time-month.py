import datetime
import glob
import pandas as pd
import matplotlib.pyplot as plt

''' analyze 2021-6-1 to 2021-07-31 eventTracking data '''

files = glob.glob("data/*.xlsx")
yes_population = 0
no_population = 0
yes_history_population = 0
no_history_population = 0
yes_bet = 0
no_bet = 0
yes_time = 0
no_time = 0

def convertTime(column):

    sec = 0
    for i in column:
        if type(i) in (int, float):
            sec += i
        elif type(i) == datetime.time:
            # print(i, pd.to_timedelta(str(i)).total_seconds())
            sec += pd.to_timedelta(str(i)).total_seconds()
    return sec


def countTime(eventTracking):
    today_bet_view = convertTime(eventTracking[eventTracking['eventName'] == 'today_bet_view']['actionValue1'])
    streaming_time = convertTime(eventTracking[eventTracking['eventName'] == 'streaming_time']['actionValue1'])
    lmt_time = convertTime(eventTracking[eventTracking['eventName'] == 'lmt_time']['actionValue1'])
    outright_bet_view = convertTime(eventTracking[eventTracking['eventName'] == 'outright_bet_view']['actionValue1'])
    inner_livebet_view = convertTime(eventTracking[eventTracking['eventName'] == 'inner_livebet_view']['actionValue1'])
    unsettled_bet_view = convertTime(eventTracking[eventTracking['eventName'] == 'unsettled_bet_view']['actionValue1'])
    settled_bet_view = convertTime(eventTracking[eventTracking['eventName'] == 'settled_bet_view']['actionValue1'])
    pre_bet_view = convertTime(eventTracking[eventTracking['eventName'] == 'pre_bet_view']['actionValue1'])
    playing_video_stream = convertTime(
        eventTracking[eventTracking['eventName'] == 'playing_video_stream']['actionValue6'])
    total = today_bet_view + streaming_time + lmt_time + outright_bet_view + inner_livebet_view \
            + unsettled_bet_view + settled_bet_view + pre_bet_view + playing_video_stream

    return total

mergeEvent = []
mergeHistory = []
for file in files:
    # load eventTracking data (5 days/ a set)
    eventTracking = pd.read_excel(file)
    # get start/ end date from file name
    startDate = file.split("\\")[-1][:10]
    endDate = file.split("\\")[-1][11:21]
    # filter bettingHistory data by date
    print(startDate, endDate)
    bettingData = pd.read_csv("data/bettingHistory/" + startDate + '_' + endDate + '_bettingHistory.csv',
                              encoding='utf-8')
    mergeEvent.append(eventTracking)
    mergeHistory.append(bettingData)
Event = pd.concat(mergeEvent)
History = pd.concat(mergeHistory)

# reduce unusable columns
bettingHistory = History[['MainAccountID', 'BetResult']]
# split bettingHistory into 2 datasets
yesPerson = bettingHistory[(bettingHistory['BetResult'] == 'Cash Out')]
yesPerson = yesPerson[['MainAccountID']].drop_duplicates(keep='first')  # 注單用戶
allPerson = bettingHistory[['MainAccountID']].drop_duplicates(keep='first')
noPerson = pd.concat([allPerson, yesPerson], ignore_index=True).drop_duplicates(keep=False)

    
# count people
yes_history_population += yesPerson['MainAccountID'].count()
no_history_population = noPerson['MainAccountID'].count()

# count time[sec]
yes_eventTracking = pd.merge(yesPerson, eventTracking, left_on=['MainAccountID'], right_on=['uid'], how='inner')
no_eventTracking = pd.merge(noPerson, eventTracking, left_on=['MainAccountID'], right_on=['uid'], how='inner')
# print(yes_eventTracking['uid'].count(), no_eventTracking['uid'].count(), eventTracking['uid'].count())
yes_time += countTime(yes_eventTracking)
no_time += countTime(no_eventTracking)
yes_population += yes_eventTracking[['uid']].drop_duplicates(keep='first')['uid'].count()
no_population += no_eventTracking[['uid']].drop_duplicates(keep='first')['uid'].count()

# count betting
filter_betHistory = bettingHistory[(bettingHistory['BetResult'] != 'Cancel') & (bettingHistory['BetResult'] != 'Adjust')]
yes_betHistory = pd.merge(yesPerson, filter_betHistory, left_on=['MainAccountID'], right_on=['MainAccountID'], how='inner')
no_betHistory = pd.merge(noPerson, filter_betHistory, left_on=['MainAccountID'], right_on=['MainAccountID'], how='inner')
yes_bet = yes_betHistory['MainAccountID'].count()
no_bet = no_betHistory['MainAccountID'].count()

# result
print("有使用兌現功能總人數:", round(yes_history_population, 3))
print("無使用兌現功能總人數:", round(no_history_population, 3))
print("有使用兌現功能用戶占整體用戶量:",  round(yes_history_population/(yes_history_population+no_history_population), 3))
print("有使用兌現功能用戶人數是無使用該功能用戶:", round(yes_history_population/no_history_population, 3))
print("有使用兌現功能總投注量:",  round(yes_bet, 3))
print("無使用兌現功能總投注量:",  round(no_bet, 3))
print("有使用兌現功能用戶占整體投注量:",  round(yes_bet/(yes_bet+no_bet), 3))
print("有使用兌現功能的平均投注量:",  round(yes_bet/yes_population, 3))
print("無使用兌現功能的平均投注量:",  round(no_bet/no_population, 3))
print("有使用兌現功能的埋點人數:",  round(yes_population, 3))
print("無使用兌現功能的埋點人數:",  round(no_population, 3))
print("有使用兌現功能的投注瀏覽時間:",  round(yes_time, 3))
print("無使用兌現功能的投注瀏覽時間:",  round(no_time, 3))
print("有使用兌現功能用戶占整體瀏覽量:",  round(yes_time/(yes_time+no_time), 3))
print("有使用兌現功能用戶瀏覽量是無使用該功能用戶:", round(yes_time/no_time, 3))
print("有使用兌現功能平均上線時間:",  round(yes_time/yes_population, 3))
print("無使用兌現功能平均上線時間:",  round(no_time/no_population, 3))

