def process_lines(input_line, output_file, template):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            #strip white space from line
            line_content = line.strip()
            # Replace 'xxx' in template with line content
            new_line = template.replace('xxx', line_content)
            # Write new line to output file
            outfile.write(new_line + '\n')

# Define path for input and output 
input_file = 'C:/Users/Tan-PhatPham/Desktop/GoM_Pull_List_Sept_2024.txt'
output_file = 'C:/Users/Tan-PhatPham/Desktop/new_GoM_List.txt'

# Define template string
template = r"\\laptop-mv7bvpb0\scs\filest~1\gom\xxx.txt text~'xxx'" 

# Process the lines 
process_lines(input_file, output_file, template)