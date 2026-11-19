import pandas as pd
import re
import os

try:
    df = pd.read_excel("Datapractice.xlsx")

    excel_list = []
    email_set = set()

    for i in df["Text"]:
        if pd.notna(i):
            emails = str(i).split(";")

            for email in emails:
                email = email.strip()

                if re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
                    if email.lower() not in email_set:
                        print(email)
                        excel_list.append(email)
                        email_set.add(email.lower())

    new_df = pd.DataFrame(excel_list, columns=["Email Id"])

    output_file = "output_data.xlsx"
    count = 2

    while os.path.exists(output_file):
        output_file = f"output_data_{count}.xlsx"
        count += 1

    new_df.to_excel(output_file, index=False)

    print("Excel file created successfully!")
    print("File name:", output_file)
    print("Total unique emails:", len(excel_list))

except FileNotFoundError:
    print("The original Excel file was not found.")

except KeyError:
    print("The column 'Text' was not found in the Excel file.")