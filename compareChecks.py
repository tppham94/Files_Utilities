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
