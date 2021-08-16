''' Population distribution '''
from matplotlib import pyplot as plt
import pandas as pd

def population_distribution(History):
    # split bettingHistory into 2 datasets: users use cash out function or not
    yesList = History[(History['BetResult'] == 'Cash Out')]
    yesList = yesList[['MainAccountID']].drop_duplicates(keep='first')  # 注單用戶
    allList = History[['MainAccountID']].drop_duplicates(keep='first')
    noList = pd.concat([allList, yesList], ignore_index=True).drop_duplicates(keep=False)
    yes_population = yesList['MainAccountID'].count()
    no_population = noList['MainAccountID'].count()
    label = ['cash out user', 'the other']
    num = [yes_population, no_population]
    plt.pie(num, labels=label, autopct='%1.2f%%')
    plt.axis('equal')
    plt.title("User distribution")
    plt.xlabel("total amount of user:"+str(yes_population+no_population))
    plt.savefig("result/user_distribution.png")
    plt.close()
    return yesList, noList, yes_population, no_population
