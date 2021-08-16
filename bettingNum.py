''' betting num distribution '''
from matplotlib import pyplot as plt
import pandas as pd
def betting_distribution(History, yesList, noList):
    filter_betHistory = History[(History['BetResult'] != 'Cancel') & (History['BetResult'] != 'Adjust')]
    yes_History = pd.merge(yesList, filter_betHistory, left_on=['MainAccountID'], right_on=['MainAccountID'],
                              how='inner')
    no_History = pd.merge(noList, filter_betHistory, left_on=['MainAccountID'], right_on=['MainAccountID'],
                             how='inner')
    yes_num = yes_History['MainAccountID'].count()
    no_num = no_History['MainAccountID'].count()
    # pie
    label = ['cash out user', 'the other']
    num = [yes_num, no_num]
    plt.pie(num, labels=label, autopct='%1.2f%%')
    plt.axis('equal')
    plt.title("Betting distribution")
    plt.xlabel("total amount of betting:" + str(yes_num + no_num))
    plt.savefig("result/betting_distribution.png")
    plt.close()
    # bar
    plt.title("Average betting volume per person")
    num[0] = round((yes_num/yesList['MainAccountID'].count()), 2)
    num[1] = round((no_num/noList['MainAccountID'].count()), 2)
    plt.bar(label, num, align='center')
    plt.savefig("result/betting_distribution_avg.png")
    plt.ylabel("Number of bets")
    plt.xlabel("Pre person")
    plt.close()
    return yes_History, no_History, yes_num, no_num
