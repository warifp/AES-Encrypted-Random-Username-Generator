import random
from model import UsernameModel
from view import UsernameView

class UsernameController:
    def __init__(self):
        self.model = UsernameModel()
        self.view = UsernameView()

    def generate_username(self):
        adjectives = ["Happy", "Silly", "Clever", "Brave", "Swift", "Witty", "Lucky", "Gentle", "Fancy", "Savvy"]
        nouns = ["Panda", "Octopus", "Wizard", "Dragon", "Jaguar", "Phoenix", "Ninja", "Samurai", "Robot", "Pirate"]

        adjective, noun = self.view.get_user_input()
        plaintext = f"{adjective}{noun}"
        key = get_random_bytes(16)
        iv, encrypted_text = self.model.encrypt(key, plaintext)
        encoded_username = f"{iv}:{encrypted_text}"
        
        self.view.display_encoded_username(encoded_username)
        return encoded_username

    def decode_username(self, encoded_username):
        iv, encrypted_text = encoded_username.split(':')
        decrypted_username = self.model.decrypt(key, iv, encrypted_text)
        
        self.view.display_decoded_username(decrypted_username)


# Main program
if __name__ == "__main__":
    controller = UsernameController()
    encoded_username = controller.generate_username()
    controller.decode_username(encoded_username)
