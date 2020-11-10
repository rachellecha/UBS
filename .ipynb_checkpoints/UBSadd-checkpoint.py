import pandas as pd

data = pd.read_csv('UBSdata.csv')

for index, row in data.iterrows():
    if "Atlantic" in row["full_name"]:
        data.at[index, "museums"] = 21
    if "Bergen" in row["full_name"]:
        data.at[index, "museums"] = 20
    if "Burlington" in row["full_name"]:
        data.at[index, "museums"] = 15
    if "Camden" in row["full_name"]:
        data.at[index, "museums"] = 17        
    if "Cape" in row["full_name"]:
        data.at[index, "museums"] = 18
    if "Cumberland" in row["full_name"]:
        data.at[index, "museums"] = 18
    if "Essex" in row["full_name"]:
        data.at[index, "museums"] = 18
    if "Gloucester" in row["full_name"]:
        data.at[index, "museums"] = 6
    if "Hudson" in row["full_name"]:
        data.at[index, "museums"] = 14
    if "Hunterdon" in row["full_name"]:
        data.at[index, "museums"] = 12
    if "Mercer" in row["full_name"]:
        data.at[index, "museums"] = 28
    if "Middlesex" in row["full_name"]:
        data.at[index, "museums"] = 16
    if "Monmouth" in row["full_name"]:
        data.at[index, "museums"] = 34
    if "Morris" in row["full_name"]:
        data.at[index, "museums"] = 29
    if "Ocean" in row["full_name"]:
        data.at[index, "museums"] = 27
    if "Passaic" in row["full_name"]:
        data.at[index, "museums"] = 15
    if "Salem" in row["full_name"]:
        data.at[index, "museums"] = 4
    if "Somerset" in row["full_name"]:
        data.at[index, "museums"] = 16
    if "Sussex" in row["full_name"]:
        data.at[index, "museums"] = 17
    if "Union" in row["full_name"]:
        data.at[index, "museums"] = 11
    if "Warren" in row["full_name"]:
        data.at[index, "museums"] = 10

data.to_csv(r'/Users/rachellecha/Desktop/UBS/UBSdata.csv', index = False)