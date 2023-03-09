# Strong Pass Py
A simple Python script to generate strong passwords.

# Description
This project provides a simple command-line interface for generating strong passwords. The password generator uses a cryptographically secure random number generator to ensure that the generated passwords are extremely difficult to guess. The generated passwords can be customized to meet your specific needs by specifying the length and composition of the password.

# Getting Started
Prerequisites:
- Python 3.x
# Installing
Clone the repository to your local machine or simply download it.
Navigate to the project directory in your terminal or command prompt.
Run the command pip install -r requirements.txt to install the required packages.
Usage
To generate a password, run the command python password_generator.py. By default, this will generate a password with 12 characters, including at least one uppercase letter, one lowercase letter, one digit, and one special character.

You can customize the generated password by specifying the following options:

-l, --length: The length of the password (default: 12).
-u, --upper: Include uppercase letters in the password.
-o, --lower: Include lowercase letters in the password.
-d, --digits: Include digits in the password.
-s, --special: Include special characters in the password.
For example, to generate a password with 16 characters, including uppercase letters and digits, run the command python password_generator.py -l 16 -u -d.
