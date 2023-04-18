import operator
from scapy.all import *
from scapy.layers.inet import *
import argparse

# Letter frequencies for Spanish language
spanish_freq = {
    'a': 0.115,
    'b': 0.022,
    'c': 0.047,
    'd': 0.057,
    'e': 0.141,
    'f': 0.009,
    'g': 0.01,
    'h': 0.007,
    'i': 0.062,
    'j': 0.004,
    'k': 0.001,
    'l': 0.049,
    'm': 0.031,
    'n': 0.067,
    'o': 0.086,
    'p': 0.025,
    'q': 0.009,
    'r': 0.068,
    's': 0.08,
    't': 0.05,
    'u': 0.024,
    'v': 0.009,
    'w': 0.001,
    'x': 0.002,
    'y': 0.01,
    'z': 0.005
}

def calculate_score(plaintext):
    """Calculates the score of a plaintext based on the letter frequency of Spanish language."""
    score = 0
    letter_count = {}
    for letter in plaintext:
        if letter.isalpha():
            if letter.lower() in letter_count:
                letter_count[letter.lower()] += 1
            else:
                letter_count[letter.lower()] = 1

    for letter, frequency in spanish_freq.items():
        if letter in letter_count:
            score += letter_count[letter] * frequency

    return score

def caesar_decrypt(ciphertext):
    scores = {}
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
        score = calculate_score(plaintext)
        scores[shift] = score
        print(f"Shift {shift}: {plaintext}")

    best_shift = max(scores.items(), key=operator.itemgetter(1))[0]
    print("\nBest possible answer:")
    print(f"\033[92mShift {best_shift}: {caesar_shift(ciphertext, best_shift)}\033[0m")

def caesar_shift(ciphertext, shift):
    """Shifts a ciphertext by a given number of positions."""
    plaintext = ""
    for letter in ciphertext:
        if letter.isalpha():
            if letter.isupper():
                plaintext += chr((ord(letter) - shift - 65) % 26 + 65)
            else:
                plaintext += chr((ord(letter) - shift - 97) % 26 + 97)
        else:
            plaintext += letter
    return plaintext


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
