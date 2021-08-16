import pandas as pd
import glob

''' convertFile from excel to csv '''

# folder path
files = glob.glob("data/*.xlsx")

for file in files:
    # load excel file
    df = pd.read_excel(file)
    # get start/ end date from file name
    startDate = file.split("\\")[-1][:10]
    endDate = file.split("\\")[-1][11:21]
    print(startDate, endDate)
    # save as csv file
    df.to_csv("data/"+startDate+"_"+endDate+".csv", index=False)
