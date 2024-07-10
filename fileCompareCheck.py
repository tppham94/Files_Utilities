import xlrd
import re

# Function to read text file and extract checkname values
def read_text_file(file_path):
    checknames = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if "checkname:" in line:
                # Extract the value after "checkname:"
                match = re.search(r'checkname:\s*(.*)', line)
                if match:
                    checkname = match.group(1).strip()
                    # Check the rest of the line for values after "CD.x.x.xx:"
                    for j in range(i + 1, len(lines)):
                        if re.match(r'.*CD\.\d+\.\d+\.\d+:.*', lines[j].strip()):
                            # Extract the value after "CD.x.x.xx:"
                            match_cd = re.search(r'CD\.\d+\.\d+\.\d+:\s*(.*)', lines[j].strip())
                            if match_cd:
                                checkname += " " + match_cd.group(1).strip()
                        else:
                            checkname += " " + lines[j].strip()  # Append rest of the line
                            if lines[j].strip() == '':
                                break  # Stop reading at end of row
                checknames.append((i + 1, checkname))  # Store line number along with checkname
    return checknames

# Function to search Excel file and extract matching lines
def search_excel(excel_path, checknames):
    matched_lines = []
    workbook = xlrd.open_workbook(excel_path)
    sheet = workbook.sheet_by_name('Tech Spec Main Body')

    for row_idx in range(1, sheet.nrows):  # Start from 1 to skip header row
        row = sheet.row_values(row_idx)
        for line_num, checkname in checknames:
            # Check if checkname matches in any of columns C (index 2), D (index 3), or F (index 5)
            if (checkname in str(row[2])) or (checkname in str(row[3])) or (checkname in str(row[5])):
                matched_lines.append(f"Line {line_num}: {checkname}")  # Save the line from text file
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
