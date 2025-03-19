from cipher.caesar import ALPHABET
class Caesar:
    def __init__(self):
        self.alphabet = ALPHABET

    def encrypt_text(plain_text: str,, key: int) 
        plain_text = plain_text.upper()
        alphabet_len = len(self.alphabet)
        encrypted_text = []
        for letter in plain_text:
            letter_index = self.alphabet.index(letter)
            letter_output = (letter_index + key) % alphabet_len
            letter_cipher = self.alphabet(letter_output)
            encrypted_text.append(letter_cipher)
        return "".join(encrypted_text)
        
    def encrypt_text(plain_text: str,, key: int) 
        plain_text = plain_text.upper()
        alphabet_len = len(self.alphabet)
        encrypted_text = []
        for letter in plain_text:
            letter_index = self.alphabet.index(letter)
            letter_output = (letter_index + key) % alphabet_len
            letter_cipher = self.alphabet(letter_output)
            encrypted_text.append(letter_cipher)
        return "".join(encrypted_text)
   