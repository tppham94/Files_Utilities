import xlrd
import re

def read_text_file(file_path):
    checknames = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if "checkname:" in line:
                checkname = None
                # Find CD.x.x.xx: value on the same line
                cd_match = re.search(r'CD\.\d+\.\d+\.\d+:\s*(.*)', line)
                if cd_match:
                    checkname = cd_match.group(1).strip()
                    # Continue reading the rest of the line for additional parts
                    for j in range(i + 1, len(lines)):
                        if lines[j].strip() == '':
                            break
                        else:
                            checkname += " " + lines[j].strip()
                if checkname:
                    checknames.append((i + 1, checkname))  # Store line number and value after CD.x.x.xx:
            print(checknames)
    return checknames

def search_excel(excel_path, checknames):
    matched_lines = []
    workbook = xlrd.open_workbook(excel_path)
    sheet = workbook.sheet_by_name('Tech Spec Main Body ')

    for row_idx in range(1, sheet.nrows):  # Start from 1 to skip header row
        row = sheet.row_values(row_idx)
        for line_num, checkname in checknames:
            if (checkname in str(row[2])) or (checkname in str(row[3])) or (checkname in str(row[5])):
                matched_lines.append(f"Line {line_num}: {checkname}")
                break  # Once a match is found, no need to check further for this checkname

    workbook.release_resources()
    return matched_lines

def write_results_to_file(matched_lines, output_file_path):
    with open(output_file_path, 'w') as file:
        for line in matched_lines:
            file.write(line + "\n")

def main():
    # Paths to your text file, Excel file, and output text file
    text_file_path = 'C:/SCS/Active Records/Network/June 2024/CPPIB/Scripts/CPPIB_Cisco_IOS_policy_updated.txt'
    excel_file_path = 'C:/SCS/Active Records/Network/June 2024/CPPIB/Scripts/CPPIB Cisco IOS-XE Tech Spec DRAFT February24-2023.xlsx'
    output_file_path = 'C:/SCS/Active Records/Network/June 2024/CPPIB/Scripts/RESULTS.txt'

    # Read checknames from the text file
    checknames = read_text_file(text_file_path)

    # Search Excel file for matching rows
    matched_lines = search_excel(excel_file_path, checknames)

    # Write results to output text file
    write_results_to_file(matched_lines, output_file_path)

    print(f"Results written to {output_file_path}")

if __name__ == "__main__":
    main()
