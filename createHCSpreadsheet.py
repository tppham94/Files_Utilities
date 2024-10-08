import openpyxl
import pandas as pd 

def createExcelSpreadsheet():
    workbook = openpyxl.Workbook()
    # Select active default sheet 
    sheet = workbook.active
    # Save workbook to a file 
    workbook.save("test.xlsx")
    print("Excel file created successfully !")

createExcelSpreadsheet()
