import sys

# Read input file
with open(sys.argv[1], 'r', encoding='latin-1') as f:
    lines = f.readlines()

# Modify each line and filter out invalid lines
modified_lines = []
for line in lines:
    if line[0].isalpha():
        modified_line = line.strip().capitalize() + '0'
        modified_lines.append(modified_line)

# Write output file
with open(sys.argv[2], 'w') as f:
    f.writelines('\n'.join(modified_lines))

