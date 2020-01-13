table = []
for i in range(26):
    row = []
    j = i
    while True:
        row.append(chr(j + 65))
        j = (j + 1) % 26
        if j == i:
            break
    table.append(row)

key = input('Enter key: ').upper()
cipher = input('Enter ciphered text: ').upper()
key_index = 0
text = []
for cipher_index in range(len(cipher)):
    char_in_key = key[key_index]
    searching_list = table[ord(char_in_key) - 65]
    char_in_cipher = cipher[cipher_index]
    if char_in_cipher != ' ':
        text.append(chr(searching_list.index(char_in_cipher) + 65))
        key_index = (key_index + 1) % len(key)
    else:
        text.append(' ')
print('Message:', ''.join(text))