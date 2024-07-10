import openpyxl

# Function to read file and extract checknames
def read_text_file(file_path):
    checknames = []
    with open(file_path, 'r') as file:
        for line in file:
            if "checkname:" in line:
                # Extract values
                checkname = line.split("checkname:")[1].strip()
                checknames.append(checkname)
    return checknames

# Function to search Excel file and extract matches 
def search_excel(excel_path, checknames):
    matched_lines = []
    wb = openpyxl.load_workbook(excel_path)
    sheet = wb["Tech Spec Main Body"]

    for row in sheet.iter_rows(min_row=2, values_only=True):
        if row[2] in checknames and row[3] in checknames and row[5] in checknames:
            matched_lines.append(row)
    
    wb.close()
    return matched_lines

