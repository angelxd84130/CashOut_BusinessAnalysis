''' Device distribution '''
from matplotlib import pyplot as plt
import pandas as pd
def device_distribution(History, yesList, noList):
    filter_betHistory = History[(History['BetResult'] != 'Cancel') & (History['BetResult'] != 'Adjust')]
    yes_History = pd.merge(yesList, filter_betHistory, left_on=['MainAccountID'], right_on=['MainAccountID'], how='inner')
    no_History = pd.merge(noList, filter_betHistory, left_on=['MainAccountID'], right_on=['MainAccountID'], how='inner')
    yes_num = yes_History['MainAccountID'].count()
    no_num = no_History['MainAccountID'].count()
    # pie
    label = ['Web_CashOut', 'Mobile_CashOut', 'APP_CashOut', 'Web', 'Mobile', 'APP']
    # yes
    yes_Web = yes_History[(yes_History['WebVersion']=='Web')]['MainAccountID'].count()
    yes_Mobile = yes_History[(yes_History['WebVersion']=='Mobile')]['MainAccountID'].count()
    yes_APP = yes_History[(yes_History['WebVersion']=='APP')]['MainAccountID'].count()
    # no
    no_Web = no_History[(no_History['WebVersion'] == 'Web')]['MainAccountID'].count()
    no_Mobile = no_History[(no_History['WebVersion'] == 'Mobile')]['MainAccountID'].count()
    no_APP = no_History[(no_History['WebVersion'] == 'APP')]['MainAccountID'].count()
    num = [yes_Web, yes_Mobile, yes_APP, no_Web, no_Mobile, no_APP]
    #separated = (.1,.1,.1,0,0,0)
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ff9999', '#66b3ff', '#99ff99']
    plt.pie(num, labels=label, autopct='%1.2f%%', colors=colors)
    plt.axis('equal')
    plt.title("Device distribution")
    plt.xlabel("total amount of betting:" + str(yes_num + no_num))
    plt.savefig("result/betting_device_distribution.png")
    plt.close()

