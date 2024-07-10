import openpyxl

# Function to extract checkname value
def extract_checkname(line):
    return line.split("checkname:")[1].strip()

# Input and output file paths
input_file = 'input.txt'  # Replace with your input text file path
output_file = 'output.xlsx'  # Replace with your desired output Excel file path

# Create a workbook and select the active sheet
wb = openpyxl.Workbook()
sheet = wb.active

# Read the text file line by line
with open(input_file, 'r') as file:
    row_index = 1
    for line in file:
        if "checkname:" in line:
            checkname_value = extract_checkname(line)
            sheet.cell(row=row_index, column=1, value=checkname_value)
            row_index += 1

# Save the workbook
wb.save(output_file)
