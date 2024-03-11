class UsernameView:
    def __init__(self):
        pass

    def get_user_input(self):
        # Get user input for adjective and noun
        adjective = input("Enter an adjective: ")
        noun = input("Enter a noun: ")
        return adjective, noun

    def display_encoded_username(self, encoded_username):
        print("Encoded Username:", encoded_username)

    def display_decoded_username(self, decoded_username):
        print("Decoded Username:", decoded_username)
