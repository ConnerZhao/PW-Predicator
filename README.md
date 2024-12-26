# Password Strength Detector
Protect yourself from modern-day threats with strong passwords!

This project offers a user-friendly graphical user interface (GUI) to analyze the strength of user-provided passwords and a script for user to build and train their own model.

Existing ML Model is trained based off of a dataset containing password and its relative strength. Sourced from Kaggle.

# Features:

Strong Password:
![Example of Strong Password](https://github.com/ConnerZhao/PW-Predicator/blob/main/data/StrongPW.png?raw=true)

Weak Password:
![Example of Weak Password](https://github.com/ConnerZhao/PW-Predicator/blob/main/data/WeakPW.png?raw=true)

**What Makes a Strong Password?**

- Length: At least 12 characters, ideally 16 or more. Shorter passwords are significantly easier to crack.
- Complexity: A mix of uppercase and lowercase letters, numbers, and symbols for enhanced protection.
- Uniqueness: Use a different password for every online account. Reusing passwords puts multiple accounts at risk if one is compromised.
- No Personal Information: Avoid birthdays, addresses, or information readily available on social media (e.g., pet names) to prevent identity theft attempts.
- Avoid Sequences: Steer clear of consecutive letters or numbers (e.g., "qwerty," "123456")
- Common Passwords are a No-Go: Avoid using well-known words like "password" or repeated characters (e.g., "aaaaaa").

**Getting Started**:

- Clone or download the repository.

- Install the required Python modules (tkinter, pandas, joblib, sklearn)

- Uncomment the model training section (if desired) and train the model according to the instructions.

- Run the script to launch the password strength detector.

**Note**:

This project is for educational purposes only. Please do not use it for storing real passwords in plain text.
Implement secure password hashing and storage practices in real-world applications.
Disclaimer: The model training section is provided for educational purposes and may require additional refinement for real-world use.
