''' SportCode distribution '''
from matplotlib import pyplot as plt
import pandas as pd
def sportCode_distribution(History, yesList, noList):
    filter_betHistory = History[(History['BetResult'] != 'Cancel') & (History['BetResult'] != 'Adjust')]
    yes_History = pd.merge(yesList, filter_betHistory, left_on=['MainAccountID'], right_on=['MainAccountID'], how='inner')
    no_History = pd.merge(noList, filter_betHistory, left_on=['MainAccountID'], right_on=['MainAccountID'], how='inner')
    yes_num = yes_History['MainAccountID'].count()
    no_num = no_History['MainAccountID'].count()
    # pie
    label = ['Soccer_CashOut', 'Basketball_CashOut', 'eSport_CashOut', 'Others_CashOut',
             'Soccer', 'Basketball', 'eSport', 'Others']
    # yes
    yes_Soccer = yes_History[(yes_History['SportCode'] == 1)]['MainAccountID'].count()
    yes_Basketball = yes_History[(yes_History['SportCode'] == 2)]['MainAccountID'].count()
    yes_eSport = yes_History[(yes_History['SportCode'] == 111)]['MainAccountID'].count()
    yes_Others = yes_History[(yes_History['SportCode'] != 1) & (yes_History['SportCode'] != 2) & (yes_History['SportCode'] != 111)]['MainAccountID'].count()
    # no
    no_Soccer = no_History[(no_History['SportCode'] == 1)]['MainAccountID'].count()
    no_Basketball = no_History[(no_History['SportCode'] == 2)]['MainAccountID'].count()
    no_eSport = no_History[(no_History['SportCode'] == 111)]['MainAccountID'].count()
    no_Ohers = no_History[(no_History['SportCode'] != 1) & (no_History['SportCode'] != 1) & (no_History['SportCode'] != 111)]['MainAccountID'].count()
    num = [yes_Soccer, yes_Basketball, yes_eSport, yes_Others, no_Soccer, no_Basketball, no_eSport, no_Ohers]
    #separated = (.1,.1,.1,0,0,0)
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    plt.pie(num, labels=label, autopct='%1.2f%%', colors=colors)
    plt.axis('equal')
    plt.title("SportCode distribution")
    plt.xlabel("total amount of betting:" + str(yes_num + no_num))
    plt.savefig("result/betting_sportCode_distribution.png")
    plt.close()

