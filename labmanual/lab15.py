"""
Experiment 15: Morse Code Translator
Question / Aim:

Write a Python program to implement a Morse Code Translator.

Program:
"""
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----',
    '2': '..---', '3': '...--',
    '4': '....-', '5': '.....',
    '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}

message = input("Enter a message: ").upper()

morse = ""

for char in message:
    if char == " ":
        morse += "/ "
    elif char in morse_code:
        morse += morse_code[char] + " "

print("Morse Code:", morse)