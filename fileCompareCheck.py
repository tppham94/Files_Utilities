import openpyxl

# Function to read text file and extract checkname values
def read_text_file(file_path):
    checknames = []
    with open(file_path, 'r') as file:
        for line in file:
            if "checkname:" in line:
                # Extract the value after "checkname:"
                checkname = line.split("checkname:")[1].strip()
                checknames.append(checkname)
    return checknames

# Function to search Excel file and extract matching rows
def search_excel(excel_path, checknames):
    matched_lines = []
    wb = openpyxl.load_workbook(excel_path)
    sheet = wb["Tech Spec Main Body"]

    for row in sheet.iter_rows(min_row=2, values_only=True):
        if row[2] in checknames and row[3] in checknames and row[5] in checknames:
            matched_lines.append(row)
    
    wb.close()
    return matched_lines

# Function to write results to a text file
def write_results_to_file(matched_lines, text_file_path):
    with open(text_file_path, 'w') as file:
        for line in matched_lines:
            file.write(f"Excel Row: {line}\n")
            # Optionally add more information from the text file if needed

# Main function to orchestrate the process
def main():
    # Path to the text file
    text_file_path = 'path/to/your/textfile.txt'
    # Path to the Excel file
    excel_file_path = 'path/to/your/excelfile.xlsx'
    # Path to the output text file
    output_file_path = 'output.txt'

    # Read checknames from the text file
    checknames = read_text_file(text_file_path)

    # Search Excel file for matching rows
    matched_lines = search_excel(excel_file_path, checknames)

    # Write results to output text file
    write_results_to_file(matched_lines, output_file_path)

    print(f"Results written to {output_file_path}")

if __name__ == "__main__":
    main()