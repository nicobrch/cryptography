#!/usr/bin/env python3

import argparse
from scapy.layers.inet import IP, ICMP
from scapy.all import *
import time
import random


def caesar_cipher(text, shift):
    """
    Encode/decode the given text using the Caesar cipher algorithm with the given shift value.
    """
    result = ""
    for char in text:
        if char.isalpha():
            # Shift the character by the specified amount
            shifted_char = chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
            if char.isupper():
                shifted_char = shifted_char.upper()
            result += shifted_char
        else:
            result += char
    return result


def create_icmp_packet(seq_num, id, timestamp, payload):
    """
    Create an ICMP packet with the given sequence number, ID, timestamp and payload.
    """
    # Add incremental bytes
    data = b''
    data += bytes([ord(payload)])  # character in the first byte
    rnd_byte = random.randint(0, 254)
    data += bytes([rnd_byte, rnd_byte + 1])  # incremental bytes
    data += b'\x00' * 5  # five null bytes
    data += bytes([i for i in range(16, 56)])  # incremental bytes from 2 to 38

    # Create the ICMP packet with the specified payload
    icmp_packet = IP(dst=args.dest_ip) / ICMP(type="echo-request", seq=seq_num, id=id) / Raw(load=data)

    # Set the timestamp
    icmp_packet.time = timestamp

    # Calculate the checksum and set it in the packet
    icmp_packet = icmp_packet.__class__(bytes(icmp_packet))

    # Return the packet
    return icmp_packet


if __name__ == "__main__":
    # Parse the command line arguments
    parser = argparse.ArgumentParser(description="Encode text using the Caesar cipher algorithm and send it through ICMP packets, one character per packet.")
    parser.add_argument("text", help="the text to be encoded and sent through ICMP packets")
    parser.add_argument("shift", type=int, help="the shift value for the Caesar cipher algorithm")
    parser.add_argument("dest_ip", help="the destination IP address for the ICMP packets")
    parser.add_argument("last_id", type=int, help="the last ID registered ICMP packet")
    args = parser.parse_args()

    # Generate the sequence number, ID and timestamp for the ICMP packets
    seq_num = 0
    id = args.last_id + 1
    timestamp = int(time.time())

    # Encode the text using the Caesar cipher algorithm
    encoded_text = caesar_cipher(args.text, args.shift)

    # Send each character in the encoded text as a separate ICMP packet
    for char in encoded_text:
        icmp_packet = create_icmp_packet(seq_num, id, timestamp, char)
        send(icmp_packet)
        seq_num += 1
        time.sleep(0.1)

    print("Encoded text sent through ICMP packets successfully!")
