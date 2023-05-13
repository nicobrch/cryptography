import pycrack
import sys

# Create a WEP key instance
wep_key = pycrack.WEPKey()

# Load the WEP 4-way handshake from the file
with open(sys.argv[1], 'rb') as f:
    handshake_data = f.read()

# Set the WEP key instance to use the handshake data
wep_key.set_handshake(handshake_data)

# Try to crack the password
password = wep_key.crack()

# Print the password if it was found
if password:
    print(f'Password found: {password}')
else:
    print('Password not found.')

