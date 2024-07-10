import re

def remove_spaces_after_checkname(input_file):
    output_lines = []
    with open(input_file, 'r') as f:
        for line in f:
            match = re.search(r'(checkname:)\s*(\S.*)', line, re.IGNORECASE)
            if match:
                updated_line = match.group(1) + ' ' + match.group(2) + '\n'
                output_lines.append(updated_line)
            else:
                output_lines.append(line)

    output_file = input_file.replace('.txt', '_updated.txt')  # Create output filename
    with open(output_file, 'w') as f:
        f.writelines(output_lines)

    print(f"Updated file saved as: {output_file}")

# Example usage:
input_file = 'your_text_file.txt'  # Replace with your actual file path
remove_spaces_after_checkname(input_file)
