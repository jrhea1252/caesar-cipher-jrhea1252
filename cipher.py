# add your code here
user_input = input("Please enter a sentence: ")
shift_amount = 5

# Create translation table for wraparound
alphabet = "abcdefghijklmnopqrstuvwxyz"
shifted_alphabet = alphabet[shift_amount:] + alphabet[:shift_amount]
trans_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())

# Encrypt the user input using Caesar cipher
cipher_text = user_input.translate(trans_table)

print("Cipher text:", cipher_text)