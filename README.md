# AES Encrypted Random Username Generator

This is a simple Python application that generates a random username by combining an adjective and a noun, encrypts it using the AES (Advanced Encryption Standard) algorithm, and then decrypts it to display the original username. It follows the MVC (Model-View-Controller) design pattern.

## Usage

1. Clone the repository.

2. Navigate to the project directory.

   ```bash
   cd aes-username-generator
    ```

3. Install the required library:

   ```bash
    pip install pycryptodome
    ````

4. Run the controller.py file:

   ```bash
   python controller.py
   ```

5. Follow the prompts to enter an adjective and a noun when asked. It will then generate a random username, encrypt it, and display the encoded and decoded usernames.

## Structure

- Model (model.py): Contains the logic for AES encryption and decryption.
- View (view.py): Handles user input and displays the encoded and decoded usernames.
- Controller (controller.py): Orchestrates the interaction between the model and view, handling user input and displaying output.

## Notes

- Make sure to keep your AES key secure.
- Feel free to modify the lists of adjectives and nouns in the username_controller.py file to suit your needs.
This application was created as a simple demonstration of AES encryption and decryption in Python using the pycryptodome library.

Contributions:
Contributions are welcome! If you have any suggestions or improvements, please feel free to create an issue or a pull request.

## License

This project is licensed under the MIT License.
