from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

class UsernameModel:
    def __init__(self):
        pass

    def pad(self, text):
        return text + (AES.block_size - len(text) % AES.block_size) * chr(AES.block_size - len(text) % AES.block_size)

    def unpad(self, text):
        return text[:-ord(text[-1])]

    def encrypt(self, key, plaintext):
        cipher = AES.new(key, AES.MODE_CBC)
        padded_plaintext = self.pad(plaintext)
        ciphertext = cipher.encrypt(padded_plaintext)
        iv = base64.b64encode(cipher.iv).decode('utf-8')
        encrypted_text = base64.b64encode(ciphertext).decode('utf-8')
        return iv, encrypted_text

    def decrypt(self, key, iv, ciphertext):
        iv = base64.b64decode(iv)
        ciphertext = base64.b64decode(ciphertext)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_text = cipher.decrypt(ciphertext)
        return self.unpad(decrypted_text).decode('utf-8')
