import xlrd

# Function to read text file and extract checkname values
def read_text_file(file_path):
    checknames = []
    with open(file_path, 'r') as file:
        for line in file:
            if "checkname:" in line:
                # Extract the value after the first "-" following "checkname:"
                checkname = line.split("checkname:")[1].strip().split("-")[0].strip()
                checknames.append(checkname)
    return checknames

# Function to search Excel file and extract matching lines
def search_excel(excel_path, checknames):
    matched_lines = []
    workbook = xlrd.open_workbook(excel_path)
    sheet = workbook.sheet_by_name('Tech Spec Main Body')

    for row_idx in range(1, sheet.nrows):  # Start from 1 to skip header row
        row = sheet.row_values(row_idx)
        for checkname in checknames:
            if (checkname in row[2]) or (checkname in row[3]) or (checkname in row[5]):
                matched_lines.append(f"Excel Row: {row}")
                break  # Once a match is found, no need to check further for this row
    
    workbook.release_resources()  # Close workbook to release memory
    return matched_lines

# Function to write results to a text file
def write_results_to_file(matched_lines, output_file_path):
    with open(output_file_path, 'w') as file:
        for line in matched_lines:
            file.write(line + "\n")

# Main function to orchestrate the process
def main():
    # Path to the text file
    text_file_path = 'path/to/your/textfile.txt'
    # Path to the Excel file
    excel_file_path = 'path/to/your/excelfile.xls'
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
