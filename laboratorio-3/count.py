import sys
import numpy

# Read input file
with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

# Output number of lines
print(f"The file '{sys.argv[1]}' has {len(lines)} lines.")

