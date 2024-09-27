import os 

def write_file_names_with_extension(folder_path, output_file):
    try:
        # Get list of files in specific folder
        files = os.listdir(folder_path)

        # Filter directories and keep files only 
        file_names = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

        # Write file name with extension to an output file
        with open(output_file, 'w') as f:
            for file_name in file_name:
                f.write(file_name + '\n')

        print(f"File names written to {output_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

folder_path = 'C:\SCS\Active Records\Network\9. September 2024\CPPIB\Received 2024'
output_file = 'file_list.txt'
write_file_names_with_extension(folder_path, output_file)