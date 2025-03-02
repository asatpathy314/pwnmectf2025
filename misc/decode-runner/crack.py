from pwn import *

def decrypt_morse_like(cipher):
    pass

def decrypt_baudot(binary_string):
    # Baudot code dictionary
    baudot_dict = {
        '00000': ('null', 'null'),
        '00100': ('espace', 'espace'),
        '10111': ('Q', '1'),
        '10011': ('W', '2'),
        '00001': ('E', '3'),
        '01010': ('R', '4'),
        '10000': ('T', '5'),
        '10101': ('Y', '6'),
        '00111': ('U', '7'),
        '00110': ('I', '8'),
        '11000': ('O', '9'),
        '10110': ('P', '0'),
        '00011': ('A', '-'),
        '00101': ('S', 'BELL'),
        '01001': ('D', '$'),
        '01101': ('F', '!'),
        '11010': ('G', '&'),
        '10100': ('H', '#'),
        '01011': ('J', "'"),
        '01111': ('K', '('),
        '10010': ('L', ')'),
        '10001': ('Z', '"'),
        '11101': ('X', '/'),
        '01110': ('C', ':'),
        '11110': ('V', ';'),
        '11001': ('B', '?'),
        '01100': ('N', ','),
        '11100': ('M', '.'),
        '01000': ('CR', 'CR'),
        '00010': ('LF', 'LF'),
        '11011': ('SWITCH', 'SWITCH')
    }

    # Split the binary string into 5-bit chunks
    chunks = binary_string.split(" ")

    decoded = []

    for chunk in chunks:
        if chunk in baudot_dict:
            decoded.append(baudot_dict[chunk][0])

    return ''.join(decoded)

def decrypt_guitar(cipher):
    def chord_notation_to_name(notation):
        chord_dict = {
        "xx0232": "D", "022100": "E", "x32010": "C", "x02220": "A",
        "320003": "G", "133211": "F", "x24442": "B"
        }
        return chord_dict.get(notation, "Unknown chord")
    
    plain = []
    for notation in cipher.split(" "):
        chord_name = chord_notation_to_name(notation)
        plain.append(chord_name)
    return ''.join(plain)


def decrypt_trithemius(cipher):
    plain = []
    initial = 3
    for char in cipher:
        plain.append(chr(ord('a') + ((ord(char) - ord('a') - initial) % 26)))
        initial += 1
    return ''.join(plain)

def decrypt_morbit(cipher):
    morbit_table = {
        "1": "..",
        "2": "./",
        "3": "/-",
        "4": "//",
        "5": "-.",
        "6": "--",
        "7": "/.",
        "8": "-/",
        "9": ".-"
    }
    morse = [morbit_table[c] for c in cipher]
    return decrypt_morse(''.join(morse))

def decrypt_morse(cipher):
    encode_table = {
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
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        ".": ".-.-.-",
        ",": "--..--",
        "?": "..--..",
        " ": "SPACE",
    }
    decode_table = {v: k for k, v in encode_table.items()}
    symbols = cipher.split("/")
    return "".join(decode_table.get(x, x)  for x in symbols)

def decrypt_leetspeak(cipher):
    encode_table = {'A': '4', 'B': '8', 'E': '3', 'G': '6', 'H': '|-|', 'I': '1', 'O': '0', 'S': '5', 'T': '7', 'U': '|_|', "K": "|<"}
    decode_table = {v: k for k, v in encode_table.items()}
    plaintext = cipher
    for key in decode_table:
        plaintext = plaintext.replace(key, decode_table[key])
    return plaintext

def decrypt_chuck_norris(cipher):
    """Decodes a Chuck Norris unary encoded string."""
    binary_string = ""
    parts = cipher.split(" ")
    i = 0
    while i < len(parts):
        if parts[i] == "0":
            binary_string += "1" * len(parts[i + 1])
        elif parts[i] == "00":
            binary_string += "0" * len(parts[i + 1])
        i += 2

    decoded_text = ""
    for i in range(0, len(binary_string), 7):
        byte = binary_string[i:i + 7]
        if len(byte) == 7:  # Prevents error if the last byte is incomplete
            decoded_text += chr(int(byte, 2))
    return decoded_text

def decrypt_wabun(wabun_code):
    wabun_dict = {
        '-.---': "E", '.-...': "O", ".-": "I", '-.-': 'WA', '.-.--': "TE", 
        '-...-': "ME", ".-.-.": "N", "-.": "TA", "-.--.": "RU", "..-": "U",
        "...-": "KU", "--.--": "A", "....": "NU", ".": "HE", "--.": "RI",
        "--.-": "NE", "-.-..": "KI", ".-..-": "WI", "-..-": "MA", "...": "RA",
        "..--": "NO", "-..-.": "MO", ".-.-": "RO", "-...": "HA", "-.-.": "NI",
        "-..": "HO", "..-..": "TO", "..-.": "CHI"
    }
    
    decoded_text = ''
    for code in wabun_code.split():
        if code in wabun_dict:
            decoded_text += wabun_dict[code]
        else:
            decoded_text += code
    
    return decoded_text.upper()

def decrypt_shankar(cipher):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = "XWYAZBCDQEFGHIKLMNOPJRSTUV"
    return "".join(normal[key.index(c)] for c in cipher)

def decrypt_military(cipher):
    return "".join(word[0] for word in cipher.split(" "))

def decrypt_gibberish(cipher):
    cipher = list(cipher)
    cipher = cipher[::-1]
    cipher = cipher[2:]
    return "".join(cipher)

if __name__ == "__main__":
    hint_engine = {
        "It looks like Morse code, but ...": lambda cipher: decrypt_morse_like(cipher),
        "He can't imagine finding himself in CTF 150 years later...": lambda cipher: decrypt_baudot(cipher),
        "Hendrix would have had it...": lambda cipher: decrypt_guitar(cipher),
        "Born in 1462 in Germany...": lambda cipher: decrypt_trithemius(cipher),
        "A code based on pairs of dots and dashes. Think of a mix of Morse code and numbers... (AZERTYUIO)": lambda cipher: decrypt_morbit(cipher),
        "1337 ...": lambda cipher: decrypt_leetspeak(cipher),
        "He can snap his toes, and has already counted to infinity twice ...": lambda cipher: decrypt_chuck_norris(cipher),
        "It looks like Morse code, but ...": lambda cipher: decrypt_wabun(cipher),
        "Did you realy see slumdog millionaire ?": lambda cipher: decrypt_shankar(cipher),
        "what is this charabia ???": lambda cipher: decrypt_gibberish(cipher),
        "NO HINT": lambda cipher: decrypt_military(cipher)
    }
    p = connect("decoderunner-780787962260a129.deploy.phreaks.fr", port=443, ssl=True)
    def process_word():
        hint_bytes = p.recvline_contains(b"hint: ", timeout=1.0)
        if hint_bytes == b'':
            hint = "NO HINT"
        else:
            hint = hint_bytes.decode('ascii').strip().split("hint: ")[1]
        cipher_bytes = p.recvline_contains(b"cipher")
        cipher = cipher_bytes.decode('ascii').strip().split("cipher: ")[1]
        decoded = hint_engine[hint](cipher)
        print(f"Hint: {hint} | Ciphertext: {cipher}")
        print(decoded)
        p.sendline(decoded.lower().encode())
    
    for i in range(100):
        process_word()
    p.interactive()