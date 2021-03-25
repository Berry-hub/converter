morse = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
         "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
         "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
         "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
         "Y": "-.--", "Z": "--.."}

def to_morse(word):
    for letters in word.upper():
        for letter, code in morse.items():
            if letter == letters:
                print(code, end="|")

def from_morse(code):
    new_code = code.split("|")
    for symbols in new_code:
        for letter, symbol in morse.items():
            if symbols == symbol:
                print(letter, end="")


#to_morse()

#from_morse()
