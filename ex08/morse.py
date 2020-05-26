import sys

MORSE_DICT = {
                'A': '.-', 'B': '-...', 'C': '-.-.',
                'D': '-..', 'E': '.', 'F': '..-.',
                'G': '--.', 'H': '....', 'I': '..',
                'J': '.---', 'K': '-.-', 'L': '.-..',
                'M': '--', 'N': '-.', 'O': '---',
                'P': '.--.', 'Q': '--.-', 'R': '.-.',
                'S': '...', 'T': '-', 'U': '..-',
                'V': '...-', 'W': '.--', 'X': '-..-',
                'Y': '-.--', 'Z': '--..',
                '1': '.----', '2': '..---', '3': '...--',
                '4': '....-', '5': '.....', '6': '-....',
                '7': '--...', '8': '---..', '9': '----.',
                '0': '-----'
            }

messages = sys.argv
messages.pop(0)
formatedMessages = ' '.join(messages).upper()
# remove multi whitespaces
formatedMessages = ' '.join(formatedMessages.split())
if (formatedMessages.replace(" ", "").isalnum()):
    morse = ""
    for letter in formatedMessages:
        if letter != ' ':
            morse += ' ' + MORSE_DICT[letter]
        else:
            morse += ' /'
    print(morse.strip())
else:
    print("ERROR")
