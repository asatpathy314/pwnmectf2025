import datetime

def generate_key(seed, length):
    key = []
    state = seed
    for _ in range(length):
        state = (state * 1103515245 + 12345) & 0x7fffffff
        rand_val = (state >> 16) & 0x7fff  # Simulate rand() from C LCG
        key.append(rand_val % 127)
    return key

# Read ciphertext
with open('flag.enc', 'rb') as f:
    ciphertext = f.read()
n = len(ciphertext)

# May 2024 timestamp range
start = int(datetime.datetime(2024, 5, 1).timestamp())
end = int(datetime.datetime(2024, 6, 1).timestamp()) - 1

# Iterate seeds and check for valid flag
for seed in range(start, end + 1):
    key = generate_key(seed, n)
    plain = bytes([c ^ k for c, k in zip(ciphertext, key)])
    if plain.startswith(b'PWNME{') and plain.endswith(b'}'):
        print(f"Decrypted flag: {plain.decode()}")
        break

