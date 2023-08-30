MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

def text_to_morse(text):
    morse_code = ''
    for char in text:
        if char.upper() in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char.upper()] + ' '
        else:
            morse_code += char
    return morse_code

def morse_to_text(morse_code):
    text = ''
    morse_code = morse_code.split(' ')
    for code in morse_code:
        if code in MORSE_CODE_DICT.values():
            for key, value in MORSE_CODE_DICT.items():
                if code == value:
                    text += key
                    break
        else:
            text += code
    return text

# Example usage
text = "HELLO WORLD"
morse_code = text_to_morse(text)
print(f"Morse code: {morse_code}")

decoded_text = morse_to_text(morse_code)
print(f"Decoded text: {decoded_text}")
