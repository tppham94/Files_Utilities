import openpyxl
import pandas as pd 

# List of sheet test 
sheet_names = ['Prod1', 'Prod2', 'Prod3']

# Might not need this one to be double checked 
def createExcelSpreadsheet():
    workbook = openpyxl.Workbook()
    # Select active default sheet 
    sheet = workbook.active
    # Save workbook to a file 
    workbook.save("test.xlsx")
    print("Excel file created successfully !")

# Creates excel sheet with multiple sheets as needed 
def generateSheetsFromList():
    with pd.ExcelWriter('multiple_sheets_example.xlsx', engine='openpyxl') as writer:
        for sheet_name in sheet_names:
            # Create a simple DataFrame for each sheet (you can customize this as needed)
            df = pd.DataFrame({
                'Column1': [1, 2, 3],
                'Column2': ['A', 'B', 'C']
            })
        
            # Write the DataFrame to the specified sheet
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    print("Excel file created with multiple sheets.")

generateSheetsFromList()