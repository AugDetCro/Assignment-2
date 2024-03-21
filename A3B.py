import pandas as pandas

if __name__ == '__main__':
    # 1. Read the csv file 'data.csv' to pull data from it
    print("===========================\n1. Read the csv file 'data.csv' to pull data from it (internal)\n")
    dataFrame = pandas.read_csv("C:/Users/augie/Downloads/data.csv/data.csv")

    # 2. Show the basic statistical desc. about the data
    print("===========================\n2. Show the basic statistical desc. about the data")

    print("Description of 'data.csv':\n", dataFrame.describe(), "\n")

    # 3. Check if the data has null values; 3a replace said values with mean
    print("===========================\n3. Check if the data has null values; 3a replace said values with mean")

    meanCalories = dataFrame["Calories"].mean()
    meanDuration = dataFrame["Duration"].mean()
    meanPulse = dataFrame["Pulse"].mean()
    meanMaxPulse = dataFrame["Maxpulse"].mean()

    dataFrame.fillna({"Calories" : meanCalories}, inplace = True)
    dataFrame.fillna({"Duration" : meanDuration}, inplace = True)
    dataFrame.fillna({"Pulse" : meanPulse}, inplace = True)
    dataFrame.fillna({"Maxpulse" : meanMaxPulse}, inplace = True)

    print(dataFrame, "\n")

    # 4. Select two columns and aggregate the data using 'min', 'max', 'count', and 'mean'
    print("===========================\n4. Select two columns and aggregate the data using 'min', 'max', 'count', and 'mean'")

    print(dataFrame.groupby("Calories").agg({"Pulse": ['min', 'max', 'count', 'mean']}), "\n")

    # 5. Filter the frame to 500 < 'Calories' < 1000
    print("===========================\n5. Filter the frame to 500 < 'Calories' < 1000")

    print(dataFrame.loc[(dataFrame["Calories"] > 500) & (dataFrame["Calories"] < 1000)], "\n")

    # 6. Filter the frame to 'calories > 500' and 'pulse < 100'
    print("===========================\n6. Filter the frame to 'calories > 500' and 'pulse < 100'")

    print(dataFrame.loc[(dataFrame["Calories"] > 500) & (dataFrame["Pulse"] < 100)], "\n")

    # 7. Create a new dataFrame_modified with all the data except 'Maxpulse'
    print("===========================\n7. Create a new dataFrame_modified with all the data except 'Maxpulse'")
    
    dataFrame_modified = pandas.DataFrame().assign(Duration = dataFrame["Duration"], Pulse = dataFrame["Pulse"], Calories = dataFrame["Calories"])
    print(dataFrame_modified, "\n")

    # 8 8. Delete Maxpulse from the original frame
    print("===========================\n8. Delete Maxpulse from the original frame")
    
    del dataFrame["Maxpulse"]
    print(dataFrame, "\n")

    # 9. Convert 'Calories' to an integer
    print("===========================\n9. Convert 'Calories' to an integer")
    
    dataFrame["Calories"] = dataFrame["Calories"].astype(int)
    print(dataFrame)