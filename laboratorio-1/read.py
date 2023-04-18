from scapy.all import *
from scapy.layers.inet import *
import argparse


def caesar_decrypt(ciphertext):
    for shift in range(26):
        plaintext = ""
        for letter in ciphertext:
            if letter.isalpha():
                if letter.isupper():
                    plaintext += chr((ord(letter) - shift - 65) % 26 + 65)
                else:
                    plaintext += chr((ord(letter) - shift - 97) % 26 + 97)
            else:
                plaintext += letter
        print(f"Shift {shift}: {plaintext}")


def read_pcapng_file(filename):
    packets = rdpcap(filename)
    icmp_packets = [p for p in packets if ICMP in p]
    id_dict = {}
    for packet in icmp_packets:
        if packet[ICMP].id in id_dict:
            id_dict[packet[ICMP].id] += packet[Raw].load.decode('utf-8')[0]
        else:
            id_dict[packet[ICMP].id] = packet[Raw].load.decode('utf-8')[0]
    return id_dict


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Reads a pcapng file and extracts the first character from each ICMP packet data field grouped by ID.')
    parser.add_argument('filename', help='Path to pcapng file')
    args = parser.parse_args()

    id_dict = read_pcapng_file(args.filename)
    for key, value in id_dict.items():
        print(f'ID: {key}, Data: {value}')
        caesar_decrypt(value)