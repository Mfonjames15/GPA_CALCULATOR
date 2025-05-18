import string

chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
print(chars)
shift = int(input("Enter the shift value: "))

keys = chars[shift:] + chars[:shift]
print(keys)

# ENCRYPTED TEXT
plain_text = input("\nEnter the text to be encrypted: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += keys[index]

print(f"\nPLAIN TEXT IS: {plain_text}")
print(f"CIPHER TEXT IS: {cipher_text}")

# DECRYPTED TEXT
cipher_text = input("\nEnter the text to be decrypted: ")
plain_text = ""

for letter in cipher_text:
    index = keys.index(letter)
    plain_text += chars[index]

print(f"\nCIPHER TEXT IS: {cipher_text}")
print(f"PLAIN TEXT IS: {plain_text}")
