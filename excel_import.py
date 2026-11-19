import pandas as pd

df = pd.read_excel("Datapractice.xlsx")

excel_list = []

for i in df.values:
    if "@" in str(i):
     print(i)
     excel_list.append(i)

new_df = pd.DataFrame(excel_list, columns=["Email Id"])

new_df.to_excel("Output_data.xlsx", index=False)
