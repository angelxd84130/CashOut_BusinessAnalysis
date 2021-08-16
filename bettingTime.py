''' SportCode distribution '''
from matplotlib import pyplot as plt
from timeProcessing import countTime
import pandas as pd
def time_distribution(Event, yesList, noList):
    # pie
    yes_event = pd.merge(yesList, Event, left_on=['MainAccountID'], right_on=['uid'], how='inner')
    no_event = pd.merge(noList, Event, left_on=['MainAccountID'], right_on=['uid'], how='inner')
    yes_time = countTime(yes_event)
    no_time = countTime(no_event)
    yes_population = yes_event[['uid']].drop_duplicates(keep='first')['uid'].count()
    no_population = no_event[['uid']].drop_duplicates(keep='first')['uid'].count()
    label = ['cash out user', 'the other']
    num = [yes_time, no_time]
    plt.pie(num, labels=label, autopct='%1.1f%%')
    plt.axis('equal')
    plt.title("Browsing time distribution")
    plt.xlabel("total web browsing time:" + str(yes_time + no_time))
    plt.savefig("result/browsing_time_distribution.png")
    plt.close()
    # bar
    plt.title("Average browsing time per person")
    num[0] = round((yes_time/yes_population), 2)
    num[1] = round((no_time/no_population), 2)
    plt.bar(label, num, align='center')
    plt.ylabel("Browsing time [sec]")
    plt.xlabel("Pre person")
    plt.savefig("result/browsing_time_distribution_avg.png")
    plt.close()