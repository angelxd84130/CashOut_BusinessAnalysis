import datetime
import pandas as pd

''' convert different time type to integer [sec] '''

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
