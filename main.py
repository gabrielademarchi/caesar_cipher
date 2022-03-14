from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift):
    cipher_text = ""
    for char in text:
        if char in alphabet:
            char_index = alphabet.index(char)
            new_index = char_index + shift
            if new_index > 26:
                new_index -= 26
            cipher_text += alphabet[new_index]
        else:
            cipher_text += char
    print(f'The encoded text is:\n{cipher_text}')


def decrypt(text, shift):
    cipher_text = ""
    for char in text:
        if char in alphabet:
            char_index = alphabet.index(char)
            new_index = char_index - shift
            if new_index < 0:
                new_index += 26
            cipher_text += alphabet[new_index]
        else:
            cipher_text += char
    print(f'The decoded text is:\n{cipher_text}')


print(logo)
end_run = False

while not end_run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    if direction == 'encode':
        encrypt(text, shift)
    else:
        decrypt(text, shift)

    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        end_run = True
        print("Goodbye")
