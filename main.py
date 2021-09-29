# CONSTANTS
MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    " ": "/",
}
OUTPUT = []


conversion_type = input("Encrypt or Decrypt (e/d)? ").upper()
inp = input("Type your message\nHERE: ").upper()
if conversion_type == "E":
    for char in inp:
        OUTPUT.append(MORSE_CODE_DICT[char])
    print(" ".join(OUTPUT))
else:
    word_list = inp.split(" ")
    words = []
    letters_list = list(MORSE_CODE_DICT.keys())
    values = list(MORSE_CODE_DICT.values())
    for _ in word_list:
        index = values.index(_)
        letter = letters_list[index]
        words.append(letter)
    print((" ").join(words))
