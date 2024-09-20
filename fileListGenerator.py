import os

def list_files_in_directory(directory, output_file):
    try:
        # Get list of file in path
        entries = os.listdir(directory)

        # Filter the files 
        files = [entry for entry in entries if os.path.isfile(os.path.join(directory, entry))]

        # Write list of files to output text files 
        with open(output_file, 'w') as f:
            for file in files:
                f.write(file + '\n')
        
        print(f"List files that has been written to text file {output_file}")

    except FileNotFoundError:
        print(f"The directory {directory} does not exist.")
    except Exception as e:
        print(f"An error occured: {e}")

# Specify directory you want to list and the output file
directory_to_scan = 'path/to/your/folder'
output_file_name = 'file_list.txt'

# Call function to run
list_files_in_directory(directory_to_scan, output_file_name)