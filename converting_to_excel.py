import pandas
from taking_attendence import present  # Import the 'present' list from taking_attendence.py

data = present  # Assign the imported list to a variable 'data'

def create_excel():
    # Create a DataFrame with two columns: 'index' and 'name'
    df = pandas.DataFrame({'index': range(1, len(data) + 1), 'name': data})
    
    # Write the DataFrame to an Excel file
    df.to_excel("today_attendence.xlsx", index=False)
    
    # Notify the user
    print("The Excel file has been created and stored.")


